"""#Paradigma imperativa
#imperate

#variáveis, atribuições e principalmente sequência
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

#bloco externo
nome = "Gabriel" #variável global
# Quando termina uma função precisa quebrar duas linhas para não ocorrer um erro

def minha_funcao():
    #bloco interno *bloco interno de uma função é conhecido como corpo da função
    nome = "Ana"  #variável local
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("impressão do bloco interno da condição if")
    for x in tupla:
        print(x)


print(nome) # executa apenas o bloco externo 
minha_funcao() # executa apenas o bloco interno
"""
"""
lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
print(lista)
print("retorno da função pop: ", retorno)
"""
"""def par_impar():
    numero = 20
    if (numero % 2) == 0:
        return "numero par"
    return "numero impar"

print(par_impar())"""


