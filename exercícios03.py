"""
Exercícios: 

1 - Escreva um programa para calcular as somas:
 S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1  # Exercício de Soma 1
 S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos) # Exercício de Soma 2
 S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos  # Exercício de Soma 3
"""
"""
# Exercício de Soma 1 
from socket import SOMAXCONN
SOMAXCONN 
S = 3/40 + 32/39 + 33/38 + 34/37 + 340/1;  
numeradores = [3, 32, 33, 34, 340]
denominadores = [40, 39, 38, 37, 1]
Soma = 0
for x in range(len(numeradores)):
    Soma += numeradores[x] / denominadores[x]
    print(f"Soma: {Soma}")

Foi calculado o resultado da expressão S = 3/40 + 32/39 + 33/38 + 34/37 + 340/1;
CÁLCULO                            SOMA
1. 3/40 = 0,075                    0,075 + 0,8205 = 08955
2. 32/39 = 0,8205                  0,8955 + 0,8684 = 1,7639
3. 33/38 = 0,8684                  1,7639 + 0,9189 = 2,6828
4. 34/37 = 0,9189                  2,6828 + 340 = 342,6828 
5. 340/1 = 340

RESULTADO
O resultado da expressão é aproximadamente 342,68
"""
#//////////////////////////////////////////////////////////////////////////////////
"""
Exercício de Soma 2

1º Exemplo 
soma = 0
numerador = 480
denominadores = [2, 22]

for x in range(20):
    if x < 2:
        soma += numerador / denominadores [x]
        numerador -= 5
    else: 
        soma += numerador / (denominadores[1] + x - 1)
        numerador -= 5

print(f"Soma: {soma}" )
"""
"""
2º Exemplo

soma = 0 
numerador = 480
denominador = 2

soma += numerador / denominador
numerador = 475
denominador = 22
soma += numerador / denominador 
numerador = 470
denominador = 23

for x in range(18):
    soma += numerador / denominador
    numerador -= 5
    denominador += 1

print(f"Soma: {soma}")
"""
""""
# 3º Exemplo

soma = 480/2 + 475/22
numerador = 470 
denominador = 23

for x in range(18):
    soma += numerador / denominador
    numerador -= 5 
    denominador += 1

print(f"Soma: {soma}")
"""


"""
Foi calculado o resultado da expressão  S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
CÁLCULO                                                     SOMA
1.  480/2 = 240             11. 430/31 = 13,87              240 + 21,59 = 261,59              413,40 + 13,28 = 426,68
2.  475/22 = 21,59          12. 425/32 = 13,28              261,59 + 20,43 = 282,02           426,68 + 12,73 = 439,41    
3.  470/23 = 20,43          13. 420/33 = 12,73              282,02 + 19,38 = 301,40           439,41 + 12,21 = 451,62    
4.  465/24 = 19,38          14. 415/34 = 12,21              301,40 + 18,40 = 319,80           451,62 + 11,71 = 463,33   
5.  460/25 = 18,40          15. 410/35 = 11,71              319,80 + 17,50 = 337,30           463,33 + 11,25 = 474,58
6.  455/26 = 17,50          16. 405/36 = 11,25              337,30 + 16,67 = 353,97           474,58 + 10,81 = 485,39
7.  450/27 = 16,67          17. 400/37 = 10,81              353,97 + 15,89 = 369,86           485,39 + 10,39 = 495,78
8.  445/28 = 15,89          18. 395/38 = 10,39              369,86 + 15,17 = 385,03           495,78 + 10    = 505,78
9.  440/29 = 15,17          19. 390/39 = 10                 385,03 + 14,50 = 399,53           505,78 + 9,62  = 515,4
10. 435/30 = 14,50          20. 385/40 = 9,63               399,53 + 13,87 = 413,40

RESULTADO
O resultado da expressão é aproximadamente 515,4
""" 
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

# Exercício de Soma 3
soma = 0 
numerador = 1
denominador = 2

soma += numerador / denominador

numerador = 3
denominador = 23

soma += numerador / denominador

for x in range(13):
    numerador = 2 * numerador + 1
    denominador += 2
    soma += numerador / denominador

print(f"Soma: {soma}")
"""
"""
Foi calculado o resultado da expressão  S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)
CÁLCULO                                                      SOMA
1.  1/2 = 0,5             11. 2047/41 = 49,9268              0,5 + 0,1304 = 0,6304                  105,6698 + 95,2326 = 200,9024
2.  3/23 = 0,1304         12. 4095/43 = 95,2326              0,6304 + 0,28 = 0,9104                 200,9024 + 182,0222 = 382,9246
3.  7/25 = 0,28           13. 8191/45 = 182,0222             0,9104 + 0,5556 = 1,466                382,9246 + 348,5745 = 348,5745
4.  15/27 = 0,5556        14. 16383/47 = 348,5745            1,466 + 1,0689 = 2,5349                731,4991 + 668,7143 = 1400,213
5.  31/29 = 1,0689        15. 32767/49 = 668,7143            2,5349 + 2,0323 = 4,5672         
6.  63/31 = 2,0323                                           4,5672 + 3,8485 = 8,4157           
7.  127/33 = 3,8485                                          8,4157 + 7,2857 = 15,7014          
8.  255/35 = 7,2857                                          15,7014 + 13,8108 = 29,5122           
9.  511/37 = 13,8108                                         29,5122 + 26,2308 = 55,743          
10. 1023/39 = 26,2308                                        55,743 + 49,9268 = 105,6698

RESULTADO
O resultado da expressão é aproximadamente 1400,213
"""
"""
soma = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + 63/31 + 127/33 + 255/35 +  511/37 + 1023/39  + 2047/41 + 4095/43 + 8191/45 + 16383/47 + 32767/49 
print(f"Soma: {soma}")"""

