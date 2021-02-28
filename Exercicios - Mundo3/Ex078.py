# Ex. 078

num, posMin, posMax = [], [], []

for i in range(1, 6):
    num.append(int(input(f"Digite o {i}º número: ")))

for pos, i in enumerate(num):
    if num[pos] == max(num):
        posMax.append(pos)

    if num[pos] == min(num):
        posMin.append(pos)


print(f"\nO maior valor é {max(num)} e está na(s) posição(ões) {posMax}")
print(f"O menor valor é {min(num)} e está na(s) posição(ões) {posMin}")
