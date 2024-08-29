# Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".


while True:
    palavra = input("digite uma palavra(ou sair para encerrar): ")
    if palavra.lower() == "sair":
        print("voce encerrou o programa. até logo!")
        break
    else:
        print(f"voce digitou: {palavra}")