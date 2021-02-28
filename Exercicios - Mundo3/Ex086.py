# Ex. 086 +=

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i}, {j}]: "))

print("-" * 30)

for linha in matriz:
    for coluna in linha:
        print(f"[{coluna:^5}]", end=" ")
    print()
