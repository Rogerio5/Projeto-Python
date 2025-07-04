class Pessoa:

    # (superclasse) - classe mãe, classe pai

    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Classe Pessoa")

    def imprimir_nome(self):
        return self.nome

class Aluno(Pessoa):

    # (subclasse) - classe filha, classe filho

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []
        print("Classe Aluno")

    def estudar(self):
        return "estudando..."
    
class Professor(Pessoa):

    def __init__(self):
        self.nome = None
        self. data_nascimento = None
        self.cpf = None
        self.rg = None

        self.disciplinas = None

    def lecionar(self):
        return "Ensinando..."

aluno1 = Aluno('Ana')
print(aluno1.imprimir_nome())


Professor1 = Professor('Marcos')
print(Professor1.imprimir_nome())
"""
print(type(aluno1))
print(type(Professor1))"""
print(aluno1.estudar())
print(Professor1.lecionar())
        