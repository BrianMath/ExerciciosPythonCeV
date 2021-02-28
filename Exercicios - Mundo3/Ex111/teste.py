from UtilidadesCeV import moeda

preco = float(input("Digite o preço: R$"))
por100_mais = float(input("Digite a porcentagem de aumento: "))
por100_menos = float(input("Digite a porcentagem de diminuição: "))

moeda.resumo(preco, por100_mais, por100_menos)
