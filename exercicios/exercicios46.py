# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

total = int()
media = float()
for i in range(1, 6):
    numero = int(input(f'Informe o numero {i}:'))
    total += numero

media = total / 5
print('a media é:', media)