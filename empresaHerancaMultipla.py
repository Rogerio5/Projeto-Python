class Funcionario:
    def trabalhar(self):
        print("Funcionário está trabalhando...")

class FrontEnd(Funcionario):
    def trabalhar(self):
        print("Desenvolvendo interface do usuário (Front-End).")

class BackEnd(Funcionario):
    def trabalhar(self):
        print("Gerenciando servidores e banco de dados (Back-End).")

class FullStack(FrontEnd, BackEnd):
    def trabalhar(self):
        print("Desenvolvendo aplicação completa (Full-Stack).")

# Criando um objeto da classe FullStack
ana = FullStack()
ana.trabalhar()

