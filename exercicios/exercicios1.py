#  Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").

numero = input("Digite um número de 1 a 3: ")
numeros_palavras = {"1": "um", "2": "dois", "3": "três"}

if numero in numeros_palavras:
    print(f"{numero} '{numeros_palavras[numero]}'.")
else:
    print("Número inválido. Por favor, digite um número de 1 a 3.")