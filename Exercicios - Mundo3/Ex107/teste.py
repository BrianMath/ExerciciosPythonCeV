import moeda

preco = float(input("Digite o preço: R$"))
por100 = int(input("Digite a porcentagem: "))

print(f"\nA metade de R${preco} é R${moeda.metade(preco)}")
print(f"O dobro de R${preco} é R${moeda.dobro(preco)}")
print(f"Aumentando {por100}% de R${preco}, temos R${moeda.aumentar(preco, por100)}")
print(f"Diminuindo {por100}% de R${preco}, temos R${moeda.diminuir(preco, por100)}")
