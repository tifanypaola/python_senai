# Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = input("Escolha um modo de transporte (carro, bicicleta, a pé): ").lower()

velocidades = {"carro": "100 km/h", "bicicleta": "45 km/h", "a pé": "5 km/h"}

if transporte in velocidades:
    print(f"A velocidade média de um {transporte} é {velocidades[transporte]}.")
else:
    print("Modo de transporte inválido.")