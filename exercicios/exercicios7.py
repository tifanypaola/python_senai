# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = float(input("Digite uma nota de 0 a 10: "))

if nota < 4:
    print("Baixa")
elif 4 <= nota < 7:
    print("Média")
else:
    print("Alta")

    