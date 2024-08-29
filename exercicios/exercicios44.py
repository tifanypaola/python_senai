# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

for i in range(10):
    numero = int(input(f"Digite o número {i + 1} "))
if numero % 2 == 0:
    print(f"{numero} é par. ")