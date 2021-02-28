# Ex. 101 +=

def voto(ano):
    from datetime import date

    print("-" * 30)
    idade = date.today().year - ano

    print(f"Com {idade} anos:", end=" ")
    if 60 > idade >= 18:
        print("Voto OBRIGATÓRIO")
    elif 60 <= idade or 16 <= idade < 18:
        print("Voto OPCIONAL")
    else:
        print("NÃO vota")


anoNasc = int(input("Em que ano você nasceu? "))
voto(anoNasc)
