# Ex. 081

valores = []

while True:
    valores.append(int(input("Digite um número: ")))

    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "s" in resp:
        print()
    else:
        print()
        break

print("-" * 40)

# Letra a)
print(f"Foi(ram) digitado(s) {len(valores)} número(s)")
print("-" * 15)

# Letra b)
valores.sort(reverse=True)
print(f"A lista, em ordem decrescente, é {valores}")
print("-" * 15)

# Letra c)
if 5 in valores:
    print("O valor 5 foi digitado na lista")
else:
    print("O valor 5 NÃO foi digitado na lista")
