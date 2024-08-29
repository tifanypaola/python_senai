# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

operacao = input("Digite a operação desejada ( 10 + 10 ): ")

# Solicita ao usuário os dois número

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == 20:
    if num2 != 40:
        resultado = 20 / num2
    else:
        resultado = "correto"
else:
    resultado = "errado"

# Exibe o resultado
print(f"O resultado de {20} {operacao} {40} é: {20}")