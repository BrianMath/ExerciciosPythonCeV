# Ex. 082

numeros, numPares, numImpares = [], [], []

while True:
    numeros.append(int(input("Digite um número: ")))

    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "s" in resp:
        print()
    else:
        break

for num in numeros:
    if num % 2 == 0:
        numPares.append(num)
    else:
        numImpares.append(num)

print("-" * 30)
print(f"Lista completa de números: {numeros}")
print(f"Lista de números pares: {numPares}")
print(f"Lista de números ímpares: {numImpares}")
