# Ex. 093 +=

# jogador = {'Nome': 'Joelson', 'Gols': [2, 1, 0, 0, 3], 'Total': 6}
jogador = {}
gols = []
posGol = 0

jogador['Nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for i in range(1, partidas + 1):
    gol = int(input(f"Quantos gols na {i}ª partida? "))
    gols.append(gol)
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)  # sum() faz a soma de algo iterável. No caso, uma lista

print("-" * 40)

print(f"O jogador {jogador['Nome']} jogou {partidas} partidas")
for j in range(1, partidas + 1):
    print(f"   => Na partida {j}, fez {jogador['Gols'][posGol]} gol(s).")
    posGol += 1
print(f"Foi um total de {jogador['Total']} gols.")
