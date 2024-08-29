#  Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

while True:
    numero = float(input("Por favor insira um numero maior que 100: "))
    if numero > 100:
        print("obrigado! voce inseriu um numero valido")
        break
    else:
        print("numero invalido tente novamente")
