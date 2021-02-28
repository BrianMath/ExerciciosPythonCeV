import moeda

preco = float(input("Digite o preço: R$"))
por100 = float(input("Digite a porcentagem: "))
formatar = str(input("Deseja formatar como moeda [S/N]? ")).upper()

if "S" in formatar:
    formatado = True
else:
    formatado = False

print(f"\nA metade de {moeda.moeda(preco)} é {moeda.metade(preco, formatado)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, formatado)}")
print(f"Aumentando {por100}% de {moeda.moeda(preco)}, temos {moeda.aumentar(preco, por100, formatado)}")
print(f"Diminuindo {por100}% de {moeda.moeda(preco)}, temos {moeda.diminuir(preco, por100, formatado)}")
