"""
Paradigma Imperativo - Fortran - Sequência, Decisão e a Interação
Paradigma estruturado - C -structs
Paradigma Procedural - Python
"""

def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente

#Reúso e Coesão

# Paradigma orientada à objetos


"""
Conceitos Estruturais

Classe - Um conjunto de objetos com as mesmas características
Objeto - Representação do Mundo real como um tipo de dadod de uma classe
Construtor - É uma função criada implicitamente com o mesmo nome da classe
Atributo - São as variaveis de uma classe
"""

class Paciente:

    def __init__(self, nome, idade, cpf, email):
        print("Acessei o construtor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

# reúso e Coesão
# Acoplamento, herança, poliformismo, GAP semântico


"""
Simulação de eventos Discretos -> Paradigma Orientado à objetos

Relação -> Destacndo funções e variáveis

------------------------------------

Conceitos Estruturais

- Classe

Classe é uma estrutura que abstrai um conjunto de objetos com características similares. Definindo o comportamento dos seus objetos através das estruturas:

1 - Atributos
2 - Métodos

A classe define um tipo de dado abstrato

"""
# Abstração
# reúso e Coesão
# Acoplamento, herança, poliformismo, GAP semântico

"""
Conceitos fundamentais

- Abstração

Processo pelo qual se isolam atributos de um objetivo, considerando os que certos grupos de objetos tenham em comum.

- Reúso

Não existe pior prática em programação do que repetir código

"""
