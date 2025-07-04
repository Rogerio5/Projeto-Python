"""
Python - Comandos de controle condicional

if , else e elif -> (else if)

"""
"""
#Exemplo 1

x = 5
y = 8

if y > x:
    print("y eh maior do que x")
    print("Código dentro do bloco condicional if")
print("Código fora do bloco condicional")
print(x>y)
"""
"""
x = 3
y = 3

if y > x:
    print("y eh maior do que x")
elif y < x:
    print("y eh menor do que x")
elif y == x:
    print("x eh igual y")
print("Código fora do bloco condicional")
print(x>y)
print(x<y)
print(y == x)
"""
a = 8
b = 5
c = 2

"""if b > a: print("b eh maior que a")
print("codigo fora do bloco if")"""

"""print("B") if b > a else print("A") # Operador ternário, Expressões condicionais"""

if a > b:
    print("A")
    if a > c:
        print("A")



