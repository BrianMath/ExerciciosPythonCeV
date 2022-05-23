# Ex. 080

valores = []

for i in range(1, 6):
    numEntrou = False
    num = int(input(f"Digite o {i}º número: "))

    for j in range(len(valores)):  # Verifica se 'num' é menor que cada valor de 'valores'
        if num < valores[j]:  # Se for menor, ...
            valores.insert(j, num)  # ... 'num' entra na posição do número maior, ...
            print(f"O valor {num} foi inserido na posição {j}")
            numEntrou = True  # ... confirma que entrou ...
            break  # ... e para de verificar, finalizando o laço

    if not numEntrou:  # Se 'num' não for menor que qualquer valor de 'valores' ...
        valores.append(num)  # ... significa que ele é o maior, portanto, deve ir para o final
        print(f"O valor {num} foi para o final")

    print()

print("-" * 45)
print(f"Lista em ordem crescente: {valores}")
