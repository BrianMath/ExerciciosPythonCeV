# Ex. 071

print("-"*25)
print("     Caixa Pythonico")
print("-"*25)

print('''\nCédulas disponíveis:
\033[32m[R$100,00]
[R$50,00]
[R$20,00]
[R$10,00]
[R$5,00]
[R$2,00]
[R$1,00]\033[m''')

saque = float(input("\nQual valor deseja sacar (só valores inteiros)? R$"))

# Cédulas de R$100
C100 = saque//100
saque = saque % 100

# Cédulas de R$50
C50 = saque//50
saque = saque % 50

# Cédulas de R$20
C20 = saque//20
saque = saque % 20

# Cédulas de R$10
C10 = saque//10
saque = saque % 10

# Cédulas de R$5
C5 = saque//5
saque = saque % 5

# Cédulas de R$2
C2 = saque//2
saque = saque % 2

# Cédulas de R$1
C1 = saque//1

print(f'''\nCédulas entregues:
\033[33m{C100:.0f}\033[m nota(s) de \033[32m[R$100,00]\033[m
\033[33m{C50:.0f}\033[m nota(s) de \033[32m[R$50,00]\033[m
\033[33m{C20:.0f}\033[m nota(s) de \033[32m[R$20,00]\033[m
\033[33m{C10:.0f}\033[m nota(s) de \033[32m[R$10,00]\033[m
\033[33m{C5:.0f}\033[m nota(s) de \033[32m[R$5,00]\033[m
\033[33m{C2:.0f}\033[m nota(s) de \033[32m[R$2,00]\033[m
\033[33m{C1:.0f}\033[m nota(s) de \033[32m[R$1,00]\033[m''')
