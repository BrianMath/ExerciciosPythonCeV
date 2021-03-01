# Ex. 063

num = int(input("Quantos termos da sequência de Fibonacci deseja? "))
cont, n1, n2, n3 = 0, 0, 1, 0

print("")
while cont < num:
    if cont == num - 1:
        print(n1)
        cont += 1
    else:
        print(n1, end=" → ")
        n1 += n2
        n2 = n3
        n3 = n1
        cont += 1
