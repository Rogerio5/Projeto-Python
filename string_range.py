"""
#       0123456
nome = "chicago"
print(nome[0]) # imprime cada letra
print(nome) # imprime a palavra
"""
"""
for x in range(10): # imprime de 0 a 9
    print(x)
"""
"""
nome = "chicago \n" # separar entre linhas
nome2 = "queens"

print(nome)
print(nome2)
"""
"""
nome = "chicago"
nome2 = "queens"

print(nome, end="@") # juntar as palavras e adiciona @
print(nome2)
"""
"""
nome = "chicago"
nome2 = "queens"

print(nome, end=" ") #as palavras na mesma linha, e contem uma separação
print(nome2)  
"""
"""
nome = "chicago"

for x in nome:
    print(x)   # imprimirá a palavra em vertical
"""
"""
nome = "chicago"

for x in nome:
    print(x, end=" ") # imprimirá a palavra em horizontal
"""
x = 5 
y = 0 

x, y = y, x # imprimirá invertido

print(x)
print(y)
