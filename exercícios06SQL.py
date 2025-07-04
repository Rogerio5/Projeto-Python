"""Exercicios 01 - Criar um módulo em python capaz de registrar dados de pacientes.
 Dados: nome completo, e-mail, cpf, rg, telefone, data de nascimento
 Atenção: Seu código deve ser capaz de calcular a idade do paciente. Em caso da idade ser
 maior ou igual a 65 anos, este paciente deve ter seus dados salvos em um arquivo com a
 informação que este paciente é do grupo de risco. Caso o paciente tenha idade menor que
 65, os dados deste paciente devem ser registrados no mesmo arquivo sem a informação do
 grupo de risco.
 Ao final do código, o programa deve imprimir todos os pacientes e solicitar uma confirmação
 para registrar um novo paciente no arquivo."""


import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import smtplib
import os
import pandas as pd

# Configuração do e-mail (SMTP)
EMAIL_REMETENTE = "seuemail@gmail.com"
SENHA_EMAIL = "suasenha"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

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

def enviar_email(destinatario, assunto, mensagem):
    try:
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_EMAIL)
        email_msg = f"Subject: {assunto}\n\n{mensagem}"
        servidor.sendmail(EMAIL_REMETENTE, destinatario, email_msg)
        servidor.quit()
        messagebox.showinfo("Sucesso", "E-mail enviado!")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível enviar o e-mail: {e}")

def registrar_paciente(nome, email, cpf, telefone, data_nascimento):
    idade = calcular_idade(data_nascimento)
    grupo_risco = "Grupo de risco" if idade >= 65 else "Não pertence ao grupo de risco"

    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO pacientes (nome, email, cpf, telefone, data_nascimento, idade, grupo_risco)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, cpf, telefone, data_nascimento, idade, grupo_risco))
        conn.commit()
        messagebox.showinfo("Sucesso", "Paciente registrado com sucesso!")
        
        # Envio de e-mail de confirmação
        enviar_email(email, "Cadastro realizado", f"Olá {nome}, seu cadastro na clínica foi realizado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "CPF já registrado!")
    finally:
        conn.close()

def agendar_consulta(cpf, data, hora, motivo):
    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()

    # Buscar paciente
    cursor.execute("SELECT id, nome, email FROM pacientes WHERE cpf = ?", (cpf,))
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

    # Envio de e-mail de lembrete
    enviar_email(paciente[2], "Consulta Agendada", f"Olá {paciente[1]}, sua consulta foi marcada para {data} às {hora}.")

    messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")

def gerar_relatorio_excel():
    conn = sqlite3.connect("clinica.db")
    pacientes = pd.read_sql_query("SELECT * FROM pacientes", conn)
    consultas = pd.read_sql_query("SELECT * FROM consultas", conn)
    conn.close()

    # Exportação para Excel
    writer = pd.ExcelWriter("relatorio_clinica.xlsx", engine='xlsxwriter')
    pacientes.to_excel(writer, sheet_name="Pacientes", index=False)
    consultas.to_excel(writer, sheet_name="Consultas", index=False)
    writer.save()

    messagebox.showinfo("Sucesso", "Relatório exportado para Excel!")

def criar_interface():
    janela = tk.Tk()
    janela.title("Sistema de Gestão Clínica")

    tk.Label(janela, text="Nome:").pack()
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()

    tk.Label(janela, text="E-mail:").pack()
    entrada_email = tk.Entry(janela)
    entrada_email.pack()

    tk.Label(janela, text="CPF:").pack()
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()

    tk.Label(janela, text="Telefone:").pack()
    entrada_telefone = tk.Entry(janela)
    entrada_telefone.pack()

    tk.Label(janela, text="Data de Nascimento (DD/MM/AAAA):").pack()
    entrada_data_nascimento = tk.Entry(janela)
    entrada_data_nascimento.pack()

    def salvar_paciente():
        registrar_paciente(
            entrada_nome.get(),
            entrada_email.get(),
            entrada_cpf.get(),
            entrada_telefone.get(),
            entrada_data_nascimento.get()
        )

    tk.Button(janela, text="Registrar Paciente", command=salvar_paciente).pack()
    tk.Button(janela, text="Agendar Consulta", command=lambda: agendar_consulta(entrada_cpf.get(), "15/07/2025", "10:00", "Rotina")).pack()
    tk.Button(janela, text="Exportar para Excel", command=gerar_relatorio_excel).pack()
    tk.Button(janela, text="Sair", command=janela.quit).pack()

    janela.mainloop()

if __name__ == "__main__":
    conectar_bd()
    criar_interface()
