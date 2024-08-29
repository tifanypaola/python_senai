# Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).

while True:
    numero = int(input("Digite um numero (digite 0 para parar): "))
    if numero == 0:
        break
    soma =+ numero
    print(f"a soma dos numeros inseridos é: {soma}")