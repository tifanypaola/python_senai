# Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

numeros = []
for i in range(5):
   numero = float(input(f"Insira o número {i + 1} ")) 
   numeros.append(numero)
maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"o maior número da lista é: {maior_numero}")
print(f"o menor número da lista é: {menor_numero}")