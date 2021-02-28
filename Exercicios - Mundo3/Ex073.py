# Ex. 073

times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atlético",
         "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritiba",
         "Avaí", "Ponte Preta", "Atlético-GO")

print(f"Lista de times: {times}")
print("-"*30)

print(f"Cinco primeiros times: {times[:5]}")
print("-"*30)

print(f"Quatro últimos times: {times[-4:]}")
print("-"*30)

print(f"Times em ordem alfabética: {sorted(times)}")
print("-"*30)

print(f"Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")
