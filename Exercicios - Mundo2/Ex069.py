# Ex. 069

sex = resp = ""
idad = pesMa18 = hom = mulMe20 = 0

while True:
    print("-"*22)
    while True:
        sex = str(input("Digite seu sexo (M/F): ")).strip().upper()
        if sex == "M":
            # Número de homens
            hom += 1
            break
        elif sex == "F":
            break
        else:
            print("Opção inválida!")
    idad = int(input("Digite sua idade: "))

    # Pessoas com mais de 18 anos
    if idad > 18:
        pesMa18 += 1

    # Mulheres com menos de 20 anos
    if (idad < 20) and (sex == "M"):
        mulMe20 += 1

    while True:
        resp = str(input("\nDeseja continuar (S/N)? ")).strip().upper()
        if "S" != resp != "N":
            print("Opção inválida!")
        elif (resp == "S") or (resp == "N"):
            break
    if resp == "N":
        break

print("-"*25)
print("\n---Resumo---")
print(f"Pessoas com mais de 18 anos: {pesMa18}")
print(f"Homens cadastrados: {hom}")
print(f"Mulheres com menos de 20 anos: {mulMe20}")
