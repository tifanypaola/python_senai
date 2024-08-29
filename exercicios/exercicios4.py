# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = input("Digite uma cor (vermelho, verde, azul): ").lower()
cores_mensagens = {"vermelho": "a cor do sangue", "verde": "a cor da floresta", "azul": "a cor do mar"}

if cor in cores_mensagens:
    print(cores_mensagens[cor])
else:
    print("somente vermelho, verde ou azul.")
