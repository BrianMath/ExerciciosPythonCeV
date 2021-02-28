def leiaDinheiro(texto):
    """
    --> Confere se o valor digitado é dinheiro
    :param texto: Texto do input
    :return: Preço validado
    """
    while True:
        num = str(input(texto)).replace(",", ".").strip()

        if num.isalpha() or num == "":
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
            continue
        break

    num = float(num)
    return num
