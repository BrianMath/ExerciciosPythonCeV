# Módulo 'moeda'

def aumentar(num, p, formatado=False):
    """
    --> Calcula um aumento de p% sobre o número fornecido
    :param num: Número qualquer
    :param p: Porcentagem que será aumentada do número
    :param formatado: (opcional) Informa se o usuário deseja ver o número com a formatação de moeda
    :return: Retorna o número fornecido + p%
    """
    porcentagem = p / 100
    resp = num + (num * porcentagem)

    return resp if formatado is False else moeda(resp)


def diminuir(num, p, formatado=False):
    """
    --> Calcula uma diminuição de p% sobre o número fornecido
    :param num: Número qualquer
    :param p: Porcentagem que será diminuída do número
    :param formatado: (opcional) Informa se o usuário deseja ver o número com a formatação de moeda
    :return: Retorna o número fornecido - p%
    """
    porcentagem = p / 100
    resp = num - (num * porcentagem)

    return resp if formatado is False else moeda(resp)


def dobro(num, formatado=False):
    """
    --> Calcula o dobro do número fornecido
    :param num: Número qualquer
    :param formatado: (opcional) Informa se o usuário deseja ver o número com a formatação de moeda
    :return: Retorna o dobro do número fornecido
    """
    resp = num * 2

    return resp if formatado is False else moeda(resp)


def metade(num, formatado=False):
    """
    --> Calcula a metade do número fornecido
    :param num: Número qualquer
    :param formatado: (opcional) Informa se o usuário deseja ver o número com a formatação de moeda
    :return: Metade do número fornecido
    """
    resp = num / 2

    return resp if formatado is False else moeda(resp)


def moeda(num, simbolo="R$"):
    """
    --> Formata um número float no formato de dinheiro
    :param num: Número float
    :param simbolo: (opcional) Símbolo da moeda desejada
    :return: String do número com um símbolo e duas casas decimais separados por ','
    """
    resp = f"{simbolo}{num:.2f}".replace(".", ",")
    return resp
