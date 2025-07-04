"""

ESTRUTURAS DE REPETIÇÃO - loops

while
for
do while*

"""
"""
a = 1
x = 0

print(a)
print(x)

x = a + 1
print(x)
"""
"""
a = 0

print(a)
a = a + 1
print(a)
"""
"""
Exemplo de utilização do break
a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    if a == 3:
        break # Comando break faz quebrar o loop 
    a = a + 1

print("Resultado final de a: ", a)
print(a <= 5)
"""

a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print("a não eh menor ou igual a 5. Valor de a: {a}")