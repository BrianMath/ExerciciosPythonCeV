# Ex. 104 +=

def leiaInt(frase):
    print("-" * 30)
    while True:
        numInt = str(input(frase))

        if numInt.isnumeric():
            return numInt
        else:
            print("\033[31mERRO! Digite um número inteiro!\033[m")


# Programa principal
n = leiaInt("Digite um número: ")
print(f"\nVocê digitou o número {n}")
