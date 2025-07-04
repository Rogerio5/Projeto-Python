"""Exercícios: 
01- Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas 
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global 
deve ser impresso o resultado retornado por estas funções.  
a) Uma função que receba X e Y como entrada e retorne o maior deles;  
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles; 
02- Escreva uma função de potenciação, em que os dados de entrada são: base e 
expoente (inteiros). 
03- Crie uma calculadora que consiga executar as funções destacadas da calculadora 
padrão do windows 10."""

"""Exercicio 1 
A)

def maior_numero(x, y):
    # Retorna o maior entre x e y
    return max(x, y)

# Lendo os valores do usuário
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Chamando a função e imprimindo o resultado
print("O maior número é:", maior_numero(x, y))
"""
"""
Exercício 1
b)

def media_aritmetica(x, y):
    #Retorna a média aritmética entre x e y
    return (x + y) / 2

# Lendo os valores do usuário
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Chamando a função e imprimindo o resultado
print("A média aritmética é:", media_aritmetica(x, y))
"""
"""
EXERCÍCIO 2 

def potenciacao(base, expoente):
    # Retorna a potência da base elevada ao expoente
    return base ** expoente  # Operador de potência em Python

# Lendo os valores do usuário
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Chamando a função e imprimindo o resultado
print(f"{base} elevado a {expoente} é igual a {potenciacao(base, expoente)}")
"""

import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz de número negativo!"
    return math.sqrt(x)

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x, base=10):
    if x <= 0:
        return "Erro: Logaritmo de número menor ou igual a zero!"
    return math.log(x, base)

def fatorial(x):
    if x < 0:
        return "Erro: Fatorial de número negativo!"
    return math.factorial(x)

# Interface simples
print("Escolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potenciação")
print("6. Raiz quadrada")
print("7. Seno")
print("8. Cosseno")
print("9. Tangente")
print("10. Logaritmo")
print("11. Fatorial")

opcao = int(input("Digite o número da operação desejada: "))

if opcao in [1, 2, 3, 4, 5]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacoes = [soma, subtracao, multiplicacao, divisao, potencia]
    print("Resultado:", operacoes[opcao - 1](num1, num2))

elif opcao in [6, 7, 8, 9, 10, 11]:
    num = float(input("Digite o número: "))
    if opcao == 10:
        base = float(input("Digite a base do logaritmo (padrão é 10): "))
        print("Resultado:", logaritmo(num, base))
    else:
        operacoes = [raiz_quadrada, seno, cosseno, tangente, logaritmo, fatorial]
        print("Resultado:", operacoes[opcao - 6](num))

else:
    print("Opção inválida!")

