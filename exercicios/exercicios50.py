# Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.

# numero = int(input("Digite um numero. "))

# for i in range(numero, 0, -1):
#     print(i)

soma = 0 

for i in range(10):
    numero = float(input(f"digite o numero {i + 1}:  "))
    soma += numero

media = soma / 10
print(f" a media dos numeros é: {media}")
