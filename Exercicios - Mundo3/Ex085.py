# Ex. 085 +=

parImpar = [[], []]

for i in range(1, 8):
    num = int(input(f"Digite o {i}º número: "))

    if num % 2 == 0:
        parImpar[0].append(num)
    else:
        parImpar[1].append(num)

print("-" * 30)
parImpar[0].sort()
parImpar[1].sort()
print(f"Os números pares são: {parImpar[0]}")
print(f"Os números ímpares são: {parImpar[1]}")
