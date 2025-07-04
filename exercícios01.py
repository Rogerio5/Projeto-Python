"""

Exercícios - Python

Observação: todos os exercícios devem utilizar a função input, de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado
04 - Se o produto que você quer avaliar custa (??) reais qual será o valor do mesmo com desconto de (??)%.
05 - área de um círculo - pi = 3,141592
06 - conversão de reais para dolar 
07 - conversão de dolar para reais

"""
#Exercícios 01 - áera do retangulo

print("Exercício 01 - Calcule a area de um retangulo")
print(" ")
base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")
area = float(base) * float(altura)
print(" ")
print(f'O seu retangulo possui area: {area} unidades de medida')