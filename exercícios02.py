"""
Exercícios:

 01- Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
 acordo com os critérios:
 ● Menor de 16 anos: MENOR
 ● Entre 16 e 18 anos: EMANCIPADO
 ● Maior de 18 anos: MAIOR

 02- Implemente um programa que receba a idade de um nadador e imprima a sua
 categoria seguindo as regras

    Categoria   /    Idade
    infantil A     5 - 7 anos
    infantil B     8 - 10 anos
    juvenil  A     11 - 13 anos
    Juvenil  B     14 - 17 anos

 """
# 01 - Criar a variável 

idade = input("Quantos anos voce tem? ") 
# por estar em "" o valor é str 
if int(idade) < 16: 
    print("Menor") 
elif int(idade) > 18:
    print("Maior") 
else: print("Emancipado") 


# 02 - Buscar a idade de nadador e classificar na tabela: 

idade = input("Ola nadador! quantos anos voce tem? ") 

if int(idade) > 4 and int(idade) < 8: 
    print("Infantil A") 
elif int(idade) > 7 and int(idade) < 11: 
    print("Infantil B") 
elif int(idade) > 10 and int(idade) < 14: 
    print("Juvenil A") 
elif int(idade) > 13 and int(idade) < 18: 
    print("Juvenil B") 
else: print("Voce nao pertence ao grupo de Natacao")

