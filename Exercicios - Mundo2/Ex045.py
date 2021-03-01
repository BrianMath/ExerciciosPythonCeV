# Ex. 045

from random import choice
from time import sleep


def numParaNome(x):
    if x == 0:
        return "Pedra"
    elif x == 1:
        return "Papel"
    elif x == 2:
        return "Tesoura"


comp = choice([0, 1, 2])
print(" 0→Pedra, 1→Papel, 2→Tesoura")
print("-" * 31)
nome = str(input("Digite seu nome: ")).capitalize()
player = int(input("Escolha 0, 1 ou 2: "))

if (player < 0) or (player > 2):
    print("\nSeu jumento, não sabe ler, não?")
    print("Só pode jogar 0, 1 ou 2!")
else:
    print("\nJo")
    sleep(1)
    print("Ken")
    sleep(1)
    print("Po")

    print(f"\nComputador jogou {numParaNome(comp)}")
    print(f"{nome} jogou {numParaNome(player)}")

    # <<<Casos para ganhar>>>
    # nº iguais empatam
    # 1 ganha de 0
    # 2 ganha de 1
    # 0 ganha de 2

    if player == comp:
        print("\n*Vocês empataram!*")
    elif (player == comp + 1) or ((player == 0) and (comp == 2)):
        print("\n*Jogador ganhou!*")
    elif (comp == player + 1) or ((comp == 0) and (player == 2)):
        print("\n*Computador ganhou!*")
