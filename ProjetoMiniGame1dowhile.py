"""

do while

Código para adivinhar um número

"""
"""
Exemplo:
palpite = 5
numero = 9

#while palpite != numero:
    #print("Qual o numero correto ? ")
    #palpite = int(input())

print("Parabens voce acertou")
#print("voce errou")

#print(bool(3<8))
print(bool(palpite))
"""

palpite = 0
numero = 9

while True: #Nós executamos sem verificar
    print("Qual o numero correto ? ")
    palpite = int(input())
    if palpite == numero: #Estamos verificando nosso código
        print("Parabens voce acertou")
        break
    else:
        print("voce errou")
else:
    print("Erro na aplicação")
print(bool(palpite))
