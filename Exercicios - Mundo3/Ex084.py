# Ex. 084 +=

pessoas, pessoa = [], []

while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Massa (kg): ")))
    pessoas.append(pessoa[:])  # Coloca cópia de 'pessoa' em 'pessoas'
    pessoa.clear()  # Apaga o conteúdo de 'pessoa'

    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "s" in resp:
        print()
    else:
        print("-" * 30)
        break

# Letra a)
print(f"Foram cadastradas {len(pessoas)} pessoas")

# Letra b) e c)
maiorMassa = menorMassa = pessoas[0][1]  # Na 1ª vez, o maior e menor pesos são o mesmo ...
maiorNome = [pessoas[0][0], ]  # Necessário [, ] para virar lista e não string
menorNome = [pessoas[0][0], ]

for i in range(1, len(pessoas)):  # ... então o laço começa a partir da posição 1 (a 2ª vez)
    if pessoas[i][1] > maiorMassa:
        maiorMassa = pessoas[i][1]
        maiorNome = [pessoas[i][1], ]  # Necessário [, ] para virar lista e não string
    elif pessoas[i][1] == maiorMassa:
        maiorNome.append(pessoas[i][0])

    if pessoas[i][1] < menorMassa:
        menorMassa = pessoas[i][1]
        menorNome = [pessoas[i][0], ]  # Necessário [, ] para virar lista e não string
    elif pessoas[i][1] == menorMassa:
        menorNome.append(pessoas[i][0])

print(f"A maior massa é de {maiorMassa:.1f}kg. Essa é a massa de {maiorNome}")
print(f"A menor massa é de {menorMassa:.1f}kg. Essa é a massa de {menorNome}")
