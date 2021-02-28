# Ex. 092 +=

from datetime import datetime

# pessoa = {'Nome': 'Pedro', 'Idade': 30, 'CTPS': 1234}
pessoa = {}
pessoa['Nome'] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
pessoa['Idade'] = datetime.today().year - ano
pessoa['CTPS'] = int(input("CTPS: "))

if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = float(input("Salário: R$"))
    # (35 - (2020 - 2000)) + 30 = (35 - 20) + 30 = 15 + 30 = 45 quando me aposentar
    pessoa['Aposentadoria'] = (35 - (datetime.today().year - pessoa['Contratação'])) + pessoa['Idade']

print("-" * 30)

for k, v in pessoa.items():
    if k == "Salário":
        print(f"{k}: R${v:.2f}")
        continue  # 'continue' pula para o próximo valor sem terminar o laço
    print(f"{k}: {v}")
