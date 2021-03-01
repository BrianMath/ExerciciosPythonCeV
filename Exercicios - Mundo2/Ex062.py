# Ex. 062

num = int(input("Digite o primeiro termo da progressão: "))
raz = int(input("Digite a razão da progressão: "))

print(num)
c, limit = 0, 9
while c < limit:
    print(num+raz)
    num += raz
    if c == limit-1:
        limit += int(input("Quantos termos a mais você quer? "))
    c += 1
