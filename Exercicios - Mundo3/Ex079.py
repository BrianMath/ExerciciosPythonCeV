# Ex. 079

num = []

while True:
    n = int(input("Digite um número: "))
    num.append(n) if n not in num else print("Já tenho esse nº. Não vou adicionar!")

    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "s" in resp:
        print()
    else:
        break

num.sort()
print("-" * 60)
print(f"Os valores digitados, em ordem crescente, foram {num}")
