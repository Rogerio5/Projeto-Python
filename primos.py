"""
Descobrir se um numero eh primo
"""
"""
7/1 resto eh 0
7/7 resto eh 0
"""

print(30 * "-")

numero = int(input("Insira um numero para descobrir se o  mesmo eh primo: "))

if numero > 1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print("Esse nao eh primo")
            break
    else:
            print("Esse numero eh primo")
else:
    print("Esse numero nao eh primo: numero menor ou igual a 1")

print(30 * "-")
