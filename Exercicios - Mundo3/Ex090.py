# Ex. 090 +=

pessoa = {'Nome': str(input("Nome: "))}  # Declarei o dicionário com a 1ª chave e recebendo 1º valor
pessoa['Média'] = float(input(f"Qual a média de {pessoa['Nome']}? "))  # 'pessoa' na chave 'Média' (criada aqui)

if pessoa['Média'] >= 7:
    pessoa['Situação'] = "Aprovado"  # Nova chave 'Situação' criada
elif 5 <= pessoa['Média'] < 7:
    pessoa['Situação'] = "Em recuperação"
else:
    pessoa['Situação'] = "Reprovado"

print("-" * 30)

for c, v in pessoa.items():  # 'c' é a chave; 'v' é o valor
    print(f"{c} é igual a {v}")
