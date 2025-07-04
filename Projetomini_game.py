

from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def Opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador = esc_jogador.lower()
    if esc_jogador in ["pedra", "papel", "tesoura"]:
        return esc_jogador
    else:
        print("Opção inválida. Tente novamente.")
        return Opcao_jogador()

def Opcao_Maquina():
    return choice(["pedra", "papel", "tesoura"])

while True:
    print("-" * 30)
    esc_jogador = Opcao_jogador()
    esc_maquina = Opcao_Maquina()
    print(f"Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}.")

    if (esc_jogador == "pedra" and esc_maquina == "tesoura") or \
       (esc_jogador == "papel" and esc_maquina == "pedra") or \
       (esc_jogador == "tesoura" and esc_maquina == "papel"):
        print("Resultado: Você Ganhou!")
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        print("Resultado: Empate!")
    else:
        print("Resultado: Você Perdeu!")
        maq_vitorias += 1

    print("-" * 30)
    print(f"Vitórias do Jogador: {jogador_vitorias}")
    print(f"Vitórias da Máquina: {maq_vitorias}")
    print("-" * 30)

    jogar_novamente = input("Você quer jogar novamente? [s/n]: ").lower()
    if jogar_novamente not in ["s", "sim"]:
        break

