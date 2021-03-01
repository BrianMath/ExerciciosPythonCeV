# Ex. 064

flag = cont = add = 0

while flag != 999:
    flag = int(input("Digite um número inteiro: "))
    cont += 1
    add += flag
print(f"\nVocê digitou {cont - 1} número(s).")
print(f"A soma dele(s) é {add - 999}.")
