# exercício básico para desenvolvedor back end
"""

Exercícios - Trocar variáveis

"""
# trocando variaveis em python

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

# Criaremos uma variavel temporaria

temp = x
x = y
y = temp

print(f"O valor de x depois da troca: {x}")
print(f"O valor de y depois da troca: {y}")
