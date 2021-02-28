# Ex. 083 +=

pareAberto = 0
expInvalida = False

exp = str(input("Digite uma expressão matemática com parênteses: "))

# Verificação 1: se não houver o mesmo nº de '(' e ')', já está errado
if exp.count("(") != exp.count(")"):
    print("Expressão inválida!")
    expInvalida = True


# Verificação 2: verifica, a cada ')', se há, pelo menos, um '(' para fechá-lo
if not expInvalida:
    for i in exp:
        if i == "(":
            pareAberto += 1
        elif i == ")":
            if pareAberto > 0:
                pareAberto -= 1
            else:
                print("Expressão inválida!")
                expInvalida = True

if not expInvalida:
    print("Expressão válida!")
