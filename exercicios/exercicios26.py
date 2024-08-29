# Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % 5 == 0 and num2 % 5 == 0:
    print("Ambos os números são múltiplos de 5.")
else:
    print("Pelo menos um dos números não é múltiplo de 5.")

