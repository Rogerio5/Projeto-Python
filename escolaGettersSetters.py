class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self._idade = idade
        self.matricula = matricula
        self.notas = None

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

# Criando um objeto aluno1
aluno1 = Aluno('josé', 15, 123456)

# Modificando o nome corretamente
print(aluno1.nome)  # Saída: josé
aluno1.nome = 'joseph'
print(aluno1.nome)  # Saída: joseph

