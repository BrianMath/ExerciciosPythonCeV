# Ex. 095 +=

# jogador = {'Nome': 'Joelson', 'Gols': [2, 1, 0, 0, 3], 'Total': 6}
jogador = {}
jogadores, gols = [], []
posGol = 0
Blue, Normal, Color, Red = "\033[34m", "\033[m", "\033[36m", "\033[31m"

while True:
    jogador['Nome'] = str(input("Nome do jogador: ")).capitalize()
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    for i in range(1, partidas + 1):
        gol = int(input(f"  Quantos gols na {i}ª partida? "))
        gols.append(gol)
    jogador['Gols'] = gols[:]  # Cópia de 'gols'
    jogador['Total'] = sum(gols)  # sum() faz a soma de algo iterável. No caso, uma lista

    jogadores.append(jogador.copy())  # Passa uma cópia do jogador atual para a lista de jogadores
    gols.clear()  # Zera a lista de gols

    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "s" in resp:
        print()
    else:
        break

print("-" * 50)

# Placar geral
print(f"{Blue}Nº  Nome          Gols            Total{Normal}")
# jogadores = [{'Nome': 'Joel', 'Gols': [0, 0, 3], 'Total': 3}, {'Nome': 'Tody', 'Gols': [2, 2, 0], 'Total': 4}]
for i in range(len(jogadores)):
    print(f"{i:<2}  {jogadores[i]['Nome']:<13} {str(jogadores[i]['Gols']):<15} {jogadores[i]['Total']:<5}")
print("-" * 50)

while True:
    quem = int(input("Deseja ver o placar de quem [-1 para sair]? "))

    if quem == -1:  # Sair
        break
    elif quem > len(jogadores) or quem < 0:  # Inválido
        print(f"{Red}Jogador não existe, tente novamente!{Normal}")
    else:  # Válido
        print(f"{Color} -- Levantamento do jogador {jogadores[quem]['Nome']} --{Normal}")
        for pos, numGols in enumerate(jogadores[quem]['Gols']):  # Tamanho da lista de gols
            print(f"   => Na partida {pos}, fez {numGols} gol(s).")
    print("-" * 50)
