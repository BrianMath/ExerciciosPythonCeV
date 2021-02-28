from UtilidadesCeV import moeda
from UtilidadesCeV import dado

preco = dado.leiaDinheiro("Digite o preço: R$")
por100_mais = float(input("Digite a porcentagem de aumento: "))
por100_menos = float(input("Digite a porcentagem de diminuição: "))

moeda.resumo(preco, por100_mais, por100_menos)
