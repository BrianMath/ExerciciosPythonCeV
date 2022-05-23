# Ex. 089 +=

boletim, notas, aluno = [], [], []
Blue, Normal, Color = "\033[34m", "\033[m", "\033[36m"

while True:
    nome = str(input("Nome: ")).capitalize()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    # As notas ficam em uma só lista
    notas.append(n1)
    notas.append(n2)
    # O nome e a lista 'notas' ficam em uma só lista
    aluno.append(nome)
    aluno.append(notas[:])
    # A lista com nomes e notas ficam em uma só lista
    boletim.append(aluno[:])
    # Apagar as outras listas
    notas.clear()
    aluno.clear()

    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "s" in resp:
        print()
    else:
        break
print("*" * 11, "RESUMO", "*" * 11)

for pos, cadaUm in enumerate(boletim):
    if pos == 0:  # Mostra o cabeçalho só na 1ª vez
        print(f"{Blue}Nº  Nome                Média{Normal}")

    media = (cadaUm[1][0] + cadaUm[1][1]) / 2  # Pega as notas do aluno atual
    print(f"{pos:<3} {cadaUm[0]:<20} {media:.1f}")
print("-" * 30)

while True:
    notaAluno = int(input("\nDeseja ver a nota de qual aluno (-1 para parar)? "))

    if notaAluno == -1:
        break

    # boletim[notaAluno] -> ['nome_do_aluno', [nota1, nota2]]
    print(f"{Color}As notas de {boletim[notaAluno][0]} são {boletim[notaAluno][1]}{Normal}")
