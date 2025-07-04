"""Listas: Coleção odenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenadas, imutável e que permite valores duplicados
Dicionários: Coleção não ordenada, mutável e que não permite valores duplicados
sets: Coleção não ordenados, imutável e que não permite valores duplicados"""


# Acessando os itens do meu set
"""conjunto = {"item1", "item2", "item3", "item3", "item1", "item2"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))"""

"""tupla = (3, 7, 9, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))"""

"""conj = {"item1", "item2", "item3", "item4", "item5"}

for x in conj:
    print(x)"""

"""conjunto = {4, 6, 8, 9, 1} # retorna se é verdadeiro ou falso
print(6 in conjunto)"""

"""conjunto = {"item", 6, 8, 9, 1}
print("item2" in conjunto)"""

#Adicionou elementos
"""set1 = {"item1", "item2", "item3",}
print(set1)
set1.add("item5")
print(set1)
set1.add(8)
set1.add(True)
print(set1)"""

"""set1 = {4, 5, 7, 8, 9, 1}
set1.update([1, 4, 7, 8, 9, 3]) 
print(set1)"""

"""set2 = {"item3", "item5", "item1"}
set1.update(set2)
print(set1)"""

# Removendo elementos

"""set1 = {1, 3, 4, 5, 'item5', 7, 8, 9, 'item6'}
print(set1)

set1.pop()
print(set1)

set1.remove("item5")
set1.discard("item9")
print(set1)
"""

# utilizando funções principais dos sets
"""conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

conjunto1.update(conjunto2)
print(conjunto1)"""

conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

# retorna os valores da chave que são iguais ou se repetem
"""conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3) 

conjunto1.intersection_update(conjunto2)
print(conjunto1)"""

# retorna os valores da chave que são diferentes e não se repetem
conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(conjunto3)

conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

#Diagrama de Venn