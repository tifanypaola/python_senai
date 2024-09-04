# Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

quantidade = int(input('quantas vezes voce quer que a mensagem seja exibida? '))

mensagem = "Oi."
contador = 0 
while contador < quantidade:
    print(mensagem) 
contador += 1