#  Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

numeros = []

for i in range(5):
    numero = float(input(f"insira o numero {i + 1}: "))
numero.append(numero)
    soma = sum(numeros)
    print("a soma de todos os numeros é: {soma} ")