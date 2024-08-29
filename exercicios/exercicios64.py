#  Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

numeros = [random.randint(1, 100) for _ in 
range(10)]

multiplos_de_3 = [numero for numero in numeros if numero % 3 == 0]
print("lista completa de numeros:", numeros)
print("numeros multiplos de 3:", multiplos_de_3)