# Ex. 004

a = input("Digite algo: ")
print(f"O tipo primitivo de 'algo' é {type(a)}")
print("Só tem espaços?", a.isspace())
print("É um número?", a.isnumeric())
print("É alfabético?", a.isalpha())
print("É alfanumérico?", a.isalnum())
print("Está em maiúsculas?", a.isupper())
print("Está em minúsculas?", a.islower())
print("Está capitalizado?", a.istitle())
