import moeda

preco = float(input("Digite o preço: R$"))
por100 = float(input("Digite a porcentagem: "))

print(f"\nA metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumentando {por100}% de {moeda.moeda(preco)}, temos {moeda.moeda(moeda.aumentar(preco, por100))}")
print(f"Diminuindo {por100}% de {moeda.moeda(preco)}, temos {moeda.moeda(moeda.diminuir(preco, por100))}")
