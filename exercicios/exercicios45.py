# Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

maior = None

for i in range(5):
    numero = int(input(f"digite o numero {i + 1}: "))
if maior is None or numero > maior:
    print(f"o maior numero inserido é: {maior}")
