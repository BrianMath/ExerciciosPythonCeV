# Ex. 075

numeros = []
for i in range(4):
	numeros.append(int(input(f"Digite o {i + 1}º número: ")))
tuplaNums = tuple(numeros)

# Letra a)
print("-"*30)
print(f"O número 9 apareceu {tuplaNums.count(9)} vez(es).")

# Letra b)
if 3 in tuplaNums:
	print(f"O primeiro número 3 foi digitado na posição {tuplaNums.index(3) + 1}.")
else:
	print("Nenhum número 3 foi digitado.")

# Letra c)
numsPares = []
for j in range(4):
	if tuplaNums[j] % 2 == 0:
		numsPares.append(tuplaNums[j])

print(f"Foi(ram) digitado(s) o(s) seguinte(s) número(s) par(es): {tuple(numsPares)}")
