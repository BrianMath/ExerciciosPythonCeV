# Ex. 076

itens = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Mochila", 120.32)

print("≈"*40)
print("ITENS E PREÇOS".center(40))
print("≈"*40)

for i in range(0, len(itens), 2):
	print("{0:.<30}R$ {1:>6.2f}".format(itens[i], itens[i + 1]))

print("_"*40)
