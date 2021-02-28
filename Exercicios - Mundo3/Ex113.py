# Ex. 113 +=

def leiaInt(msg):
    while True:
        try:
            nInt = int(input(msg))
        except (TypeError, ValueError):
            print("\033[31mErro: digite um número inteiro válido!\033[m")
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu não digitar esse número\033[m")
            return 0
        else:
            return nInt


def leiaFloat(msg):
    while True:
        try:
            nFloat = float(input(msg))
        except (TypeError, ValueError):
            print("\033[31mErro: digite um número real válido\033[m")
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu não digitar esse número\033[m")
            return 0
        else:
            return nFloat


# Programa principal
numInt = leiaInt("Digite um número inteiro: ")
print("-" * 30)
numFloat = leiaFloat("Digite um número real: ")

print(f"""\nValor inteiro: {numInt}
Valor real: {numFloat}""")
