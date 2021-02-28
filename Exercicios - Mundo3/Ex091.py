# Ex. 091 +=

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"    O {k} tirou {v}")
    sleep(1)

print("-" * 33)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# 'ranking' receberá o items de 'jogadores', os ordenará pelo índice 1 (o valor tirado no dado) ...
# ... e em ordem decrescente

print(" << RANKING DOS JOGADORES >>")
for i, j in enumerate(ranking):
    print(f"    {i + 1}º lugar: {j[0]} com {j[1]} pontos")
    sleep(1)
