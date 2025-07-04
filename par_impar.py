"""
Como descobrir se um numero é impar ou par
"""

#num =  5 
#numero = 2

#print(5%2)

#numeros Pares 0,2,4,6,8,10,12,14...
#0/2,2/2,4/2... divisão inteira (1,0)

numero = int(input("insira um numero para saber se o mesmo eh par: "))
if (numero % 2) == 0:
    print(f"{numero} eh um numero par")
else:
    print(f"{numero} eh um numero impar")


