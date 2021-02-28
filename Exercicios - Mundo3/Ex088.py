# Ex. 088 +=

from random import randint
from time import sleep

nums, jogos = [], []
jogoAtual = 1

print("-" * 30)
print("      Jogos da Mega-Sena      ")
print("-" * 30)

nJogos = int(input("\nQuantos jogos deseja sortear? "))

print(f"\n<<<<< Sorteando {nJogos} jogos >>>>>")

for i in range(1, nJogos + 1):
    while len(nums) <= 6:
        num = randint(1, 60)

        if num not in nums:
            nums.append(num)

    nums.sort()
    jogos.append(nums[:])
    nums.clear()

for j in range(nJogos):
    print(f"Jogo nº{jogoAtual}: {jogos[j]}")
    jogoAtual += 1
    sleep(1)

print("\033[33m<<<<< Boa sorte! >>>>>")
