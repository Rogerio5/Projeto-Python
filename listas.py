"""
lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista2 = lista2 + lista3 # junção da lista2 com lista3
print(lista2)

lista4 = [True, False]
print(lista4)
# index    0        1      2      3    4  -> 5 elementos
lista5 = [True, "chicago", 2.5, False, 4]
print(lista5)

print(type(lista2))

print(lista5[1])  # imprimirá o primeiro elemento

print(lista5[-1])  # Imprimirá o ultimo elemento

# SCILING
# Essa função que utilizamos :: é (Sciling)
print(lista5[1:]) # retorna do index que dstacamos até o fim da lista
print(lista5[:3]) # retorna do começo da lista até o index -1
print(lista5[1:4]) # retona do index destacado até o index -1

nome = "terra"

print(nome5[::])
"""
"""

lista1 = [2.0 , 3.5, 4.7]
print(lista1)

lista2 = [1, 5, 9, 11, 15]
print(lista2)

# index     0        1        2
lista3 = ["Nome", "Nome2", "Nome3"]

print(len(lista3))

# tamanho da lista - função len
print(len(lista1))
print(len(lista2))

# Funções que só podem ser utilizados com tipos de dados numéricos

print(sum(lista1)) # Somatório dos elementos da nossa lista
x = 2.0 + 3.5 + 4.7
print(x)

print(max(lista2)) # retorna o elemento de valor máximo da lista
print(max(lista1))

print(min(lista2)) # retorna o elemento de valor mínimo da lista
print(min(lista1))


nome = "Cuso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list("Curso de Python")
print(lista8)

elemento = 8

if elemento in lista7:
    print("Este elemento esta dentro da lista")
"""
"""
# index     0        1        2
lista = ["gato", "cachorro", "peixe", "cavalo", "tubarão", "gifara"]
print(lista)

print(type(lista))
print(lista[1])

lista[1] = 'cavalo'
print(lista)

lista[1:4] = ["águia", "morcego", "elefante"]
print(lista)"""
"""
lista[1:2] = ["águia", "elefante"] # Adicinado 2 elementos em uma lista
print(lista)

print(lista[1])
print(lista[2])
print(lista[3])

lista[1:5] = ["tubarão"]
print(lista)
"""
"""
# Exemplo

# index     0        1        2
lista = ["carro", "barco", "avião"]
print(lista)

lista.insert(0, "bicicleta")

print(lista)

lista.append(["bicicleta", "navio"]) # 4 elementos
lista.extend(["bicicleta", "navio"]) # 5 elementos

print(lista)
print(len(lista)) # Verifica a quantidade da lista

for x in range(len(lista)):
    print(x, lista[x])

"""
"""texto = "meunome@gmail.com"
lista2 = list(texto)
print(lista2)

texto = texto.split('@') # retira @ da lista
print(texto)"""
 

"""
# index     0        1        2
lista = ["carro", "barco", "avião"]
print(lista)"""

# lista.pop() # Remove o elemento da lista
# lista.remove("barco") # Remove o elemento da lista
#del lista[0]
"""
carrinho_de_compras = ["pão", "carne", "verduras", "alface"]
carrinho_de_compras.sort() """# retorna em ordem crescente ou alfabética

# carrinho_de_compras.clear()

"""print(carrinho_de_compras)

for x in range(len(carrinho_de_compras)):
    print(x, carrinho_de_compras[x])"""


"""lista = [1, 50, 23, 67, 100]
print(lista)

#lista.sort(reverse = True) # retorna de forma crescente
lista.reverse() # Retrona invertido a lista
print(lista)"""


"""lista = ["Ana", "Pedro", "Marta", "Clarice", "Beatriz", "Ana Clara"]
print(lista)

lista.sort(key = str.lower)
print(lista)""" # retorna em ondem alfabética

"""lista = ["a", "b", "c",]
lista2 = [1, 4, 6]"""

"""lista = lista + lista2 
print(lista)""" # Soma da lista e lista 2 (concatenou)
"""lista.extend(lista2) 
print(lista)""" # Soma da lista e lista 2 (concatenou)
"""for x in lista2: 
    lista.append(x) # Soma da lista e lista 2 (concatenou)

print(lista)"""

lista = ["a", "b", "c",]
print(lista)

lista2 = lista.copy()
print(lista2) 

"""lista2 = lista
print(lista2)"""

lista.append("d")
lista2.append("e")

print(lista)
print(lista2) 

