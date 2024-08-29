#  Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

num1 = float(input("digite o primeiro número."))
num2 = float(input("Digite o segundo número."))
num3 = float(input("Digite o terceiro número."))

if num1 == num2 == num3:
   print("Todos os números são iguais.")
else:
    print("Os números não são iguais.")
