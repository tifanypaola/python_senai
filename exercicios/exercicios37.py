# Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.

numero = int(input("Digite um número: "))

if numero % 2 == 0 or numero % 5 == 0:
    print("O numero é multiplo de 2 ou de 5. ")
else: 
    print("O número não é multiplo de 2 nem de 5.")

