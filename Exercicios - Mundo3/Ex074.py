# Ex. 074

from random import randint

numeros = []
for i in range(5):
    numeros.append(randint(1, 20))
tuplaNums = tuple(numeros)

print(f"Números sorteados: {tuplaNums}")
print(f"Maior valor: {max(tuplaNums)}")
print(f"Menor valor: {min(tuplaNums)}")
