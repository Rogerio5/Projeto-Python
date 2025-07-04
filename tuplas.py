"""lista = ["item1", "item2", "item3"]
print(lista)
print(len(lista))
print(type(lista))

print("------"*10)
# index    0         1        2 
tupla = ("item1", "item2", "item3")
print(tupla)
print(len(tupla))
print(tupla[2])

print(tupla.count("item10"))
"""

tupla = ("item1",)
tupla2 = ("a", "b")
"""tupla3 = tupla * 3""" # Retorna 3 x a palavra 'item'
tupla = "item1", "item2", "item3"
print(tupla)

(x, *y) = tupla # retorna separação dos itens X e Y
print("x:", x)
print("y:", y)

"""(x, y, z) = tupla
print("x:", x)
print("y:", y)
print("z:", z)"""


"""for x in tupla:
    print(x)

for x in range(len(tupla)): # Retorna as posições dos elementos
    print(x,tupla[x])"""

