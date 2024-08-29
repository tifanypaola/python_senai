#  Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

contador = 0

for i in range(7):
    numero = int(input(f"Digite o numero {i + 1}:"))
if numero > 10:
    contador += 1
    print(f"quantidade de numeros maiores que 10: {contador}") 
