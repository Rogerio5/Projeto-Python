#Parâmetros de uma função

#Passando a valores interno para o externo
"""def minha_funcao():
    var = "maria"
    return var

var = minha_funcao()
print(var)"""

#Passando a valores externo para o interno
"""def nome_da_funcao(parametro): #parâmetro é o nome dado ao valores utilizados na definição de uma função
    #Corpo da função
    print("ola ", parametro)

nome = input("Qual o seu nome? ")
nome_da_funcao(nome) #argumento é o nome dado aos valores utilizados na chamada de uma função"""

#Argumentos Nomeados

"""def imprimir_nome(nome, sobrenome, idade):
    print("nome: ", nome)
    print("sobrenome: ", sobrenome)
    print("idade: ", idade)"""
#exemplo 1
"""imprimir_nome("Rogerio", "Sabino", 30)"""
#exemplo 2
"""imprimir_nome(nome="Rogerio", sobrenome="Sabino", idade=30)"""

# Parametros Padroes

"""def imprimir_nome(nome=None, sobrenome=None, idade=None):
    if nome != None:
        print("nome: ", nome)
        print("sobrenome: ", sobrenome)
        print("idade: ", idade)
        print("------------------")
    else:
        print("Por favor insira seus dados")

print()
imprimir_nome()
imprimir_nome("maria", "clara", 35)"""

"""def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
        print("----------------")
        print("Título:", nomeImovel)
        print("Quartos:", n_quartos)
        if vagasGaragem != None:
            print("Vagas na garagem: ", vagasGaragem)
       

print()
# Exemplos de nº de argumentos <= nº dos parâmetros
imprimir_imovel("Casa 3 Quartos - SP", 3)
imprimir_imovel("Apartamento - MG", 2, 1)"""

#EXEMPLO ARGS
# O Argumento Arbitrário *args - Essa função recebe argumentos que serão atribuídos em uma tupla
"""def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *telefones):
        print("----------------")
        print("Título:", nomeImovel)
        print("Quartos:", n_quartos)
        if vagasGaragem != None:
            print("Vagas na garagem: ", vagasGaragem)
        print("telefones", telefones)

imprimir_imovel("Loja Comercial", 2, 5, "61 5555-5555", "21 5555-5555")"""
#Exemplo
"""def imprimir_nomes(*nomes):
      print(nomes)

lista = ["Ana", "Beatriz", "Pedro", "João"]
imprimir_nomes(*lista)"""

# Argumento Arbitrário **Kwargs - Keyword Arguments
# Essa função recebe argumentos que serão atribuídos em um dicionario

# Exemplo 1
"""def imprimir_nomes(**nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")

imprimir_nomes(nome="Ana", sobrenome="Julia")"""
# Exemplo 2
def imprimir_nomes(nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")

dicio = {'nome':'Ana', 'sobrenome':'Julia'}
imprimir_nomes(dicio)