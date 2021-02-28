# Ex. 097 +=

def escreva(msg):
    print("-" * (len(msg) + 2))  # O nº de '-' será do len(msg) + os 2 espaços de cada lado do texto
    print(f" {msg} ")            # Coloquei um espaço em cada lado do texto para parecer que está dentro
    print("-" * (len(msg) + 2))


texto = str(input("Texto: "))
escreva(texto)
