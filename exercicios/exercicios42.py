#  Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

soma = 0

for i in range(5):
    numero = int(input(f"digite o numero {i +1}: "))
soma += numero
print(f"A soma dos números é: {soma} ")