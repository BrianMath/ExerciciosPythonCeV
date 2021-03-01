# Ex. 066

cont = soma = 0

while True:
    num = int(input("Digite um número (999 para parar): "))
    if num != 999:
        cont += 1
        soma += num
    else:
        break

print(f"\nN° digitados: {cont}")
print(f"Soma dos n°: {soma}")
