from abc import ABC, abstractmethod

# Classe Abstrata 
class Pessoa(ABC):
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print(f"Executando o construtor da classe Pessoa para {self.nome}")

    def imprimir_nome(self):
        return self.nome
    
    @abstractmethod
    def trabalhar(self):
        """Método abstrato que deve ser implementado nas classes concretas"""
        pass

# Classes Concretas
class Administrador(Pessoa):
    def trabalhar(self):
        print(f"{self.nome} está administrando a empresa.")

class Professor(Pessoa):
    def trabalhar(self):
        print(f"{self.nome} está dando aulas.")

class Aluno(Pessoa):
    def trabalhar(self):
        print(f"{self.nome} está estudando.")

# Instanciando Objetos das Classes Concretas
admin = Administrador("Carlos Silva", "12/05/1980", "12345678900", "MG123456")
professor = Professor("Ana Souza", "22/09/1975", "98765432100", "SP987654")
aluno = Aluno("Lucas Pereira", "10/03/2000", "65432198700", "RJ654321")

# Chamando Métodos
print(admin.imprimir_nome())
admin.trabalhar()

print(professor.imprimir_nome())
professor.trabalhar()

print(aluno.imprimir_nome())
aluno.trabalhar()
