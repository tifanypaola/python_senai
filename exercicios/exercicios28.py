# Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

palavra = input("Digite uma palavra: ")

if len(palavra) > 5:
    print("A palavra tem mais de 5 letras.")
else:
    print("A palavra tem 5 letras ou menos.")
