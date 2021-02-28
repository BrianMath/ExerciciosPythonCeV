# Módulo 'moeda'

def aumentar(num, p):
    """
    --> Calcula um aumento de p% sobre o número fornecido
    :param num: Número qualquer
    :param p: Porcentagem que será aumentada do número
    :return: Retorna o número fornecido + p%
    """
    porcentagem = p / 100
    resp = num + (num * porcentagem)
    return resp


def diminuir(num, p):
    """
    --> Calcula uma diminuição de p% sobre o número fornecido
    :param num: Número qualquer
    :param p: Porcentagem que será diminuída do número
    :return: Retorna o número fornecido - p%
    """
    porcentagem = p / 100
    resp = num - (num * porcentagem)
    return resp


def dobro(num):
    """
    --> Calcula o dobro do número fornecido
    :param num: Número qualquer
    :return: Retorna o dobro do número fornecido
    """
    resp = num * 2
    return resp


def metade(num):
    """
    --> Calcula a metade do número fornecido
    :param num: Número qualquer
    :return: Metade do número fornecido
    """
    resp = num / 2
    return resp
