# Ex. 100 +=

from random import randint
from time import sleep

numeros = []


def sorteia():
    print("Sorteando 5 valores:", end=" ")
    for i in range(5):
        numeros.append(randint(1, 10))
        print(numeros[i], end=" ")
        sleep(0.3)
    print()


def somaPar():
    pares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += num
    print(f"Somando os valores pares de {numeros} temos {pares}")


sorteia()
somaPar()
