# Ex. 099 +=

def maior(nums):  # nums é uma lista
    print(f"Foi(ram) digitado(s) {len(nums)} número(s)")
    if len(nums) > 0:
        print(f"    -> {nums}")
        print(f"O maior valor é {max(nums)}")
    else:
        print("Não há um maior valor")


valores = []
while True:
    resp = str(input("Deseja continuar [s/n]? ")).lower()
    if "n" in resp:
        break

    valores.append(float(input("Digite um número: ")))
    print()

print("-" * 40)

maior(valores)
