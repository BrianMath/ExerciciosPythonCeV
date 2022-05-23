# Ex. 098 +=

from time import sleep

Cor, Normal = "\033[1:36m", "\033[m"


def contador(start, end, step):
    # Título
    if step < 0:  # Para mostrar 'step' positivo
        print(f"{Cor}Contagem de {start} até {end} de {step * -1} em {step * -1}{Normal}")
    elif step == 0:
        print(f"{Cor}Contagem de {start} até {end} de 1 em 1{Normal}")
    else:
        print(f"{Cor}Contagem de {start} até {end} de {step} em {step}{Normal}")

    alt = 1  # Caso seja positivo
    if start > end:
        if step > 0:  # Caso a pessoa ponha o 'step' positivo para voltar, mude ele para negativo
            step *= -1
        if step == 0:  # Caso a pessoa não ponha o 'step' e estiver voltando ele é -1
            step = -1
        alt = -1  # Caso seja negativo
    elif start < end and step == 0:  # Caso a pessoa não ponha o 'step' e estiver indo ele é 1
        step = 1

    for i in range(start, end + alt, step):  # Se eu digitar 'end' = 3 quero ir até 3 e não até 2
        print(i, end=" ")
        sleep(0.4)
    print("Fim!")


# Letra a)
contador(1, 10, 1)

print("-" * 36)

# Letra b)
contador(10, 0, 2)

print("-" * 36)

# Letra c)
print(f"{Cor}Vamos personalizar a contagem agora!{Normal}")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

print("-" * 36)

contador(inicio, fim, passo)
