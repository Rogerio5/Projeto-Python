import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import smtplib
import os
import pandas as pd
from twilio.rest import Client  # API para WhatsApp
import stripe  # API para Pagamentos

# Configuração Twilio (WhatsApp)
TWILIO_SID = "seu_sid"
TWILIO_AUTH_TOKEN = "seu_token"
TWILIO_NUMERO = "seu_numero_twilio"
WHATSAPP_NUMERO_DESTINO = "+55XXXXXXXXXX"  # Número do paciente

# Configuração Stripe (Pagamentos)
STRIPE_SECRET_KEY = "sua_chave_secreta"
stripe.api_key = STRIPE_SECRET_KEY

# Conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()
    
    # Tabela de pacientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            telefone TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            idade INTEGER NOT NULL,
            grupo_risco TEXT NOT NULL
        )
    """)

    # Tabela de agendamentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            motivo TEXT NOT NULL,
            pagamento_status TEXT DEFAULT 'Pendente',
            FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
        )
    """)

    conn.commit()
    conn.close()

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

def enviar_whatsapp(mensagem):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_NUMERO}",
            body=mensagem,
            to=f"whatsapp:{WHATSAPP_NUMERO_DESTINO}"
        )
        messagebox.showinfo("Sucesso", "Notificação enviada via WhatsApp!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao enviar WhatsApp: {e}")

def agendar_consulta(cpf, data, hora, motivo):
    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, telefone FROM pacientes WHERE cpf = ?", (cpf,))
    paciente = cursor.fetchone()

    if not paciente:
        messagebox.showerror("Erro", "Paciente não encontrado!")
        return

    cursor.execute("""
        INSERT INTO consultas (paciente_id, data, hora, motivo)
        VALUES (?, ?, ?, ?)
    """, (paciente[0], data, hora, motivo))
    
    conn.commit()
    conn.close()

    mensagem = f"Olá {paciente[1]}, sua consulta foi marcada para {data} às {hora}. Por favor, confirme o pagamento!"
    enviar_whatsapp(mensagem)

    messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")

def processar_pagamento(cpf):
    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()

    cursor.execute("SELECT c.id, p.nome FROM consultas c JOIN pacientes p ON c.paciente_id = p.id WHERE p.cpf = ? AND c.pagamento_status = 'Pendente'", (cpf,))
    consulta = cursor.fetchone()

    if not consulta:
        messagebox.showerror("Erro", "Nenhuma consulta pendente para pagamento!")
        return

    try:
        pagamento = stripe.PaymentIntent.create(
            amount=10000,  # Valor em centavos (R$100,00)
            currency="brl",
            payment_method_types=["card"]
        )

        cursor.execute("UPDATE consultas SET pagamento_status = 'Pago' WHERE id = ?", (consulta[0],))
        conn.commit()
        conn.close()

        mensagem = f"Pagamento confirmado para sua consulta, {consulta[1]}! Obrigado por escolher nossa clínica."
        enviar_whatsapp(mensagem)

        messagebox.showinfo("Sucesso", "Pagamento realizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha no pagamento: {e}")

def criar_interface():
    janela = tk.Tk()
    janela.title("Sistema de Gestão Clínica")

    tk.Label(janela, text="CPF para consulta/pagamento:").pack()
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()

    tk.Button(janela, text="Agendar Consulta", command=lambda: agendar_consulta(entrada_cpf.get(), "15/07/2025", "10:00", "Rotina")).pack()
    tk.Button(janela, text="Processar Pagamento", command=lambda: processar_pagamento(entrada_cpf.get())).pack()
    tk.Button(janela, text="Sair", command=janela.quit).pack()

    janela.mainloop()

if __name__ == "__main__":
    conectar_bd()
    criar_interface()
