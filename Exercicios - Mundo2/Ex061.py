# Ex. 061

num = int(input("Digite o primeiro termo da progressão: "))
raz = int(input("Digite a razão da progressão: "))

print(num)
c = 0
while c < 9:
    print(num+raz)
    num += raz
    c += 1
