# Ex. 102 +=

def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número
    :param n: número cujo fatorial será calculado
    :param show: (opcional) mostra ou não o cálculo do fatorial
    :return: O fatorial de um número n
    """
    from math import factorial

    print("-" * 30)
    if show:
        for i in range(n, 0, -1):
            if i == 1:
                print(i, end=" = ")
            else:
                print(i, end=" x ")
    print(factorial(n))


# Programa principal
num = int(input("Número cujo fatorial deseja: "))
ver = str(input("Deseja ver o cálculo do fatorial [S/N]?")).upper()
if ver == "S":
    ver = True

fatorial(num, ver)
