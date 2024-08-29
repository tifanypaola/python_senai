# Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input("digite um numero para ver a tabuada "))

for i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")