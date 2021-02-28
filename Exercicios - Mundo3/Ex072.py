# Ex. 072

nExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
            "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

num = int(input("Digite um número entre 0 e 20: "))
while True:
    if (num < 0) or (num > 20):
        num = int(input("Número não possível. Digite novamente: "))
    else:
        break

print(f"Você digitou o número {nExtenso[num]}")
