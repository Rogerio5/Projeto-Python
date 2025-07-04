# import random
# from random import choice
# import random as rd

"""from random import (
    random as rd
)"""

"""from random import *

# print(randint(1, 5))  
# Consegue incluir o primeiro nº e o ultimo nº do intervalo
print(randint())"""

"""Módulos - arquivos com extensão .py - ou seja - arquivos python
Pacotes - diretórios contendo conjunto de módulos - pastas com vários arquivos python"""


"""from pacote import principal, secundario

print(principal.soma(2, 3))
print(secundario.quadratica(5))"""

"""from pacote.sub_diretorio import outro as modulo

print(modulo.cubica(3))"""

"""Exmeplo:
from pacote.principal import soma

print(soma(2, 3))"""

from pacote.sub_diretorio.outro import cubica

print(cubica(2))