# Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

import random


numero_secreto = random.randint(1, 10)

print("Bem vinde ao jogo de adivinhação!")
print("tente adivinhar o numero secreto entre 1 e 10.")

while True:
    palpite = int(input("Digite seu palpite: "))
    print("Parabéns! voce adivinhou o numero secreto.")
    break
else:
    print("Palpite incorreto. tente denovo.")
