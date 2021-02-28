# Ex. 103 +=

def ficha(nomeJog="<desconhecido>", numGols=0):

    print(f"Jogador {nomeJog} fez {numGols} gol(s)")


# Programa principal
nome = str(input("Nome do jogador: "))
gols = str(input("Nº de gols: "))

# Validação
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "":
    ficha(numGols=gols)
else:
    ficha(nome, gols)
