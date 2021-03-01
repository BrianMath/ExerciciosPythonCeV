# Ex. 068

from random import randint

numJog = numComp = vit = 0

while True:
    # Escolher Par ou Impar
    while True:
        jog = str(input("\nJogue ímpar ou par (I/P): ")).strip().upper()
        if "P" != jog != "I":
            print("Opção Inválida!")
        else:
            break

    # Escolher número
    print("-"*20)
    numJog = int(input("Jogue um número: "))
    numComp = randint(0, 100)
    print("-"*20)

    # Análise
    print(f"Você jogou {numJog}, e o computador, {numComp}")
    if ((numJog + numComp) % 2 == 0) and (jog == "P"):
        print("\n\033[32mPARABÉNS, VOCÊ GANHOU!\033[m")
        vit += 1
        print("-"*23)
    elif ((numJog + numComp) % 2 == 0) and (jog == "I"):
        print("\n\033[31mQUE PENA, O COMPUTADOR GANHOU!\033[m")
        break
    elif ((numJog + numComp) % 2 != 0) and (jog == "I"):
        print("\n\033[32mPARABÉNS, VOCÊ GANHOU!\033[m")
        vit += 1
        print("-"*23)
    elif ((numJog + numComp) % 2 != 0) and (jog == "P"):
        print("\n\033[31mQUE PENA, O COMPUTADOR GANHOU!\033[m")
        break
print(f"\n\033[33mVocê venceu {vit} vez(es)\033[m")
