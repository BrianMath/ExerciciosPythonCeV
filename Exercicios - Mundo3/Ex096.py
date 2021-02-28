# Ex. 096 +=

def area(larg, comp):
    print(f"O terreno de dimensões {larg} m x {comp} m tem {larg * comp:.2f} m²")
    # Dica de português: quase sempre tem que pôr um espaço entre a unidade e a medida. Horas são exceção: 15h30min20s
    # Nesse caso, espaço entre 'larg' e a unidade metros (m), assim como 'comp' e a área


print("-" * 23)
print(f"{'Cálculo de área':^23}")
print("-" * 23)

larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(larg, comp)
