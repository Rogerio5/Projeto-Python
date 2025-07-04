"""Listas: Coleção odenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenadas, imutável e que permite valores duplicados
Dicionários: Coleção não ordenada, mutável e que não permite valores duplicados"""


"""# index     0         1        2
lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")"""

#chave:valor
"""dicio = {"nome": "Gabriel", "ano" : 1993, "valor_logico" : True}
print(dicio)

dicio["nome"] = "Pedro" # Retorna a troca do valor da chave Gabriel p/ Pedro
print(dicio)

dicio.update({"nome":"Ana"}) # retorna atualizando a troca do valor da chave Pedro p/ Ana
print(dicio)

dicio ["idade"] = 32 #retorna adicionando mais um valor na chave
print(dicio)

dicio.update({"estado":"Rio de Janeiro"}) #retorna adicionando mais um valor na chave
print(dicio)"""

"""#chave:valor
dados = {"nome": "Gabriel", "ano" : 1993, "valor_logico" : True}
dados.update({"estado":"Rio de Janeiro"})
print(dados)"""

"""# Função popitem, Retorna removendo o valor da chave, elimina o ultimo item apenas da versão 3.7 e acima
dados.popitem()# nas outras versões (abaixo da 3.7) essa função elimina um item aleatório
print(dados) 

dados.pop("nome")
print(dados)

del dados["ano"]
print(dados)"""
"""
for x, y in dados.items():
    print(x, y)

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)"""

#chave:valor
"""dicio = {"chave1": "Gabriel", "chave2" : 1993, "chave3" : True}
print(dicio)

dicionario = {
    "nome": "Bruna",
    "idade": 27,
    "nacionalidade": "brasileiro"
}
print(dicionario)
print(dicionario['idade'])
print(dicionario.get("idade")) 
print(dicionario.keys())
print(len(dicionario))
print(dicionario.values())

if "idade" in dicionario:
    print("A chave idade existe")

print(dicionario.items()) """#retorna chave e valor do item dicionario

"""#index      0        1        2 
tupla = ("item1", "item2", "item3")
tupla2 = ("item1", "item2", "item3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)"""

"""# index     0         1        2
lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")

#chave:valor
dicio = {
    "dicio1": {
        "nome": "Ana",
        "idade": 25,
    },
    "dicio2": {
        "nome": "Pedro",
        "idade": 38,
    },
    "dicio3": {
        "nome": "Ana julia",
        "idade": 5,
    }
}

print(dicio)
"""
