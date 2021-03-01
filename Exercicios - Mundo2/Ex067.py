# Ex. 067

while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    if num >= 0:
        print("-"*20)
        for cont in range(1, 11):
            print(f"{num} x {cont:>2} = {num*cont}")
        print("-"*20)
        print("")
    else:
        break
print("\nPrograma finalizado!")
