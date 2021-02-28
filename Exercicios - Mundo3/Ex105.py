# Ex. 105 +=

def notas(*n, sit=False):
    """
    --> Função de gerenciamento de notas
    :param n: uma ou mais notas dos alunos
    :param sit: (opcional) mostra ou não a situação da turma
    :return: dicionário com informações sobre a turma
    """
    alunos, infoAlunos = [*n], dict()

    infoAlunos['Total'] = len(alunos)
    infoAlunos['Maior'] = max(alunos)
    infoAlunos['Menor'] = min(alunos)
    infoAlunos['Média'] = round(sum(alunos) / len(alunos), 2)
    if sit:
        if infoAlunos['Média'] >= 7:
            infoAlunos['Situação'] = "Boa"
        elif infoAlunos['Média'] >= 6:
            infoAlunos['Situação'] = "Razoável"
        else:
            infoAlunos['Situação'] = "Ruim"

    return infoAlunos


# Programa principal
info = notas(7.8, 6, 4.6, 9.8, 10, 8.2, sit=True)
print(info)
