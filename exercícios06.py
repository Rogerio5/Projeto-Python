"""Exercicios 01 - Criar um módulo em python capaz de registrar dados de pacientes.
 Dados: nome completo, e-mail, cpf, rg, telefone, data de nascimento
 Atenção: Seu código deve ser capaz de calcular a idade do paciente. Em caso da idade ser
 maior ou igual a 65 anos, este paciente deve ter seus dados salvos em um arquivo com a
 informação que este paciente é do grupo de risco. Caso o paciente tenha idade menor que
 65, os dados deste paciente devem ser registrados no mesmo arquivo sem a informação do
 grupo de risco.
 Ao final do código, o programa deve imprimir todos os pacientes e solicitar uma confirmação
 para registrar um novo paciente no arquivo.
 # Não se esqueça de implementar o if __name__ == '__main__'
 """
"""
import datetime
import os

class Paciente:
    def __init__(self, nome, email, cpf, rg, telefone, data_nascimento):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        hoje = datetime.date.today()
        nascimento = datetime.datetime.strptime(self.data_nascimento, "%d/%m/%Y").date()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def formatar_dados(self):
        grupo_risco = "Grupo de risco" if self.idade >= 65 else "Não pertence ao grupo de risco"
        return f"{self.cpf},{self.nome},{self.email},{self.rg},{self.telefone},{self.data_nascimento},{self.idade},{grupo_risco}\n"

def definir_arquivo(idade):
    return "grupo_risco.txt" if idade >= 65 else "pacientes.txt"

def registrar_paciente():
    nome = input("Nome completo: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    telefone = input("Telefone: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")

    paciente = Paciente(nome, email, cpf, rg, telefone, data_nascimento)

    arquivo = definir_arquivo(paciente.idade)

    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(paciente.formatar_dados())

    print("\nPaciente registrado com sucesso!")
    print(paciente.formatar_dados())

def mostrar_pacientes(filtrar_grupo=None):
    arquivos = ["grupo_risco.txt", "pacientes.txt"]

    for arquivo in arquivos:
        if filtrar_grupo and arquivo != filtrar_grupo:
            continue

        if os.path.exists(arquivo):
            print(f"\nLista de pacientes ({arquivo}):")
            with open(arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    print(linha.strip())
        else:
            print(f"\nNenhum paciente registrado em {arquivo}.")

def buscar_paciente():
    cpf_busca = input("Digite o CPF do paciente a ser buscado: ")
    arquivos = ["grupo_risco.txt", "pacientes.txt"]
    
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    if cpf_busca in linha:
                        print("\nPaciente encontrado:")
                        print(linha.strip())
                        return
    print("\nPaciente não encontrado.")

def remover_paciente():
    cpf_remover = input("Digite o CPF do paciente a ser removido: ")
    arquivos = ["grupo_risco.txt", "pacientes.txt"]

    for arquivo in arquivos:
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            
            with open(arquivo, "w", encoding="utf-8") as f:
                for linha in linhas:
                    if cpf_remover not in linha:
                        f.write(linha)

    print("\nPaciente removido com sucesso!")

def editar_paciente():
    cpf_editar = input("Digite o CPF do paciente a ser editado: ")
    arquivos = ["grupo_risco.txt", "pacientes.txt"]

    for arquivo in arquivos:
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            
            paciente_encontrado = None
            for linha in linhas:
                if cpf_editar in linha:
                    paciente_encontrado = linha.strip().split(",")

            if paciente_encontrado:
                print(f"\nPaciente encontrado: {linha.strip()}")
                paciente_encontrado[1] = input("Novo nome completo: ")
                paciente_encontrado[2] = input("Novo e-mail: ")
                paciente_encontrado[4] = input("Novo telefone: ")

                novo_registro = ",".join(paciente_encontrado) + "\n"

                with open(arquivo, "w", encoding="utf-8") as f:
                    for linha in linhas:
                        if cpf_editar not in linha:
                            f.write(linha)
                    f.write(novo_registro)

                print("\nPaciente atualizado com sucesso!")
                return
            else:
                print("\nPaciente não encontrado.")
                return

if __name__ == "__main__":
    while True:
        print("\n1 - Registrar paciente")
        print("2 - Mostrar todos pacientes")
        print("3 - Mostrar apenas grupo de risco")
        print("4 - Buscar paciente por CPF")
        print("5 - Editar paciente")
        print("6 - Remover paciente")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_paciente()
        elif opcao == "2":
            mostrar_pacientes()
        elif opcao == "3":
            mostrar_pacientes("grupo_risco.txt")
        elif opcao == "4":
            buscar_paciente()
        elif opcao == "5":
            editar_paciente()
        elif opcao == "6":
            remover_paciente()
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
"""


