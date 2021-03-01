# Ex. 070

from math import inf

tot = prodMa1000 = 0
prodMaBara = inf
nomProdMaBara = resp = ""

print("-"*25)
print("     LOJAS AFRICANAS")
print("-"*25)
while True:
    print("")
    prod = str(input("Digite o nome do produto: "))
    prec = float(input("Digite o preço do produto: R$"))

    # Total da compra
    tot += prec

    # Produtos que custam mais de R$1000,00
    if prec > 1000:
        prodMa1000 += 1

    # Nome do produto mais barato
    if prec < prodMaBara:
        prodMaBara = prec
        nomProdMaBara = prod
    while (resp != "S") and (resp != "N"):
        resp = str(input("Deseja continuar (S/N)? ")).strip().upper()
    if resp == "N":
        break

    # Reinicialização da resposta
    resp = ""

print("-"*25)
print("\n---Resumo---")
print(f"Total gasto na compra: R${tot:.2f}")
print(f"Produtos que custam mais de R$1000,00: {prodMa1000}")
print(f"Nome do produto mais barato: {nomProdMaBara}")
