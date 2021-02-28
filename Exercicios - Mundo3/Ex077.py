# Ex. 077

palavras = ("macaco", "dinheiro", "cidade", "paralelepipedo", "anticonstitucionalissimamente",
            "pneumoultramicroscopicossilicovulcanoconioticos")

for palavra in palavras:                                                        # Pega cada palavra de uma vez só
	print(f"A palavra {palavra} tem a(s) seguinte(s) vogal(ais): ", end="")
	for letra in palavra:                                                       # Pega cada letra de uma vez só
		if letra in "aeiou":                                                    # Se a letra for vogal, imprima-a
			print(letra, end=" ")
	print("\n")                                                                 # Quebra de linha
