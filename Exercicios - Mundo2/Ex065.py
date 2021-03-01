# Ex. 065

qnt = soma = 0
lista = []

while True:
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
    soma += num
    qnt += 1

    continuar = str(input("Deseja continuar (S/N)? ")).upper()
    if continuar == "N":
        break

    print("-" * 15)

print(f"\nMédia dos números: {soma / qnt:.2f}")
print(f"Maior n°: {max(lista)}; Menor n°: {min(lista)}")
