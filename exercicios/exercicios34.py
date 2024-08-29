# Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero = float(input("Digite um numero "))

if numero > 0:
    print("O numero é positivo.")
elif numero < 0:
    print("O numero é negativo.")
else:
    print("o numero é zero.")