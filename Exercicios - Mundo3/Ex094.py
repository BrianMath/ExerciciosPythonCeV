# Ex. 094 +=

pessoas, mulheres, pesAcimaMedia = [], [], []
idades = 0
Red, Normal = "\033[31m", "\033[m"

while True:
    nome = str(input("Nome: ")).capitalize()
    while True:  # Análise de erro: 'sexo' só pode ser F ou M
        sexo = str(input("Sexo [F/M]: ")).upper()
        if sexo in "FM":
            break
        else:
            print(f"{Red}Resposta inválida, tente novamente!{Normal}")

    idade = int(input("Idade: "))
    idades += idade  # Para letra b)
    if sexo == "F":  # Para letra c)
        mulheres.append(nome)

    pessoas.append(dict(Nome=nome, Sexo=sexo, Idade=idade))  # Cria dicionário -> {'Nome': João, 'Sexo': M, 'Idade': 13}

    while True:  # Análise de erro: 'resp' só pode ser S ou N
        resp = str(input("Deseja continuar [s/n]? ")).upper()
        if "N" in resp:
            break
        elif "S" in resp:
            print()
            break
        else:
            print(f"{Red}Resposta inválida, tente novamente!{Normal}")
    if "N" in resp:  # Sai do primeiro laço
        break

print("-" * 50)

# Letra a)
print(f"- Foram cadastradas {len(pessoas)} pessoas")

# Letra b)
media = idades/len(pessoas)
print(f"- Média de idade: {media:.2f}")

# Letra c)
print(f"- As mulheres cadastradas são: {mulheres}")

# Letra d)
# pessoas = [{'Nome': Zé, 'Sexo': M, 'Idade': 60}, {'Nome': Tereza, 'Sexo': F, 'Idade': 30}]
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] > media:
        pesAcimaMedia.append(pessoas[i])

print("- Pessoas com idade acima da média: ")
for j in range(len(pesAcimaMedia)):
    for k, v in pesAcimaMedia[j].items():
        if k == 'Idade':  # Como 'Idade' é a última chave, após o par não precisa de ;
            print(f"{k}: {v}")
            continue
        print(f"{k}: {v};", end=" ")
