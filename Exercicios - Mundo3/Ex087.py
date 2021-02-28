# Ex. 087 +=

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
somaPares, soma3Col = 0, 0
maiorLinha2 = []

for i in range(3):
    for j in range(3):
        num = int(input(f"Digite um valor para a posição [{i}, {j}]: "))
        matriz[i][j] = num

        if num % 2 == 0:  # Se for par
            somaPares += num

        if j == 2:  # Se estiver na 3ª coluna
            soma3Col += num

        if i == 1:  # Se estiver na 2ª linha
            maiorLinha2.append(num)

print("-" * 30)

for linha in matriz:
    for coluna in linha:
        print(f"[{coluna:^5}]", end=" ")
    print()

# Letra a)
print(f"A soma dos números pares é {somaPares}")

# Letra b)
print(f"A soma da 3ª coluna é {soma3Col}")

# Letra c)
print(f"O maior valor da 2ª linha é {max(maiorLinha2)}")
