# Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = input("Digite o tipo de combustível (gasolina, etanol, diesel): ").lower()

precos = {"gasolina": "R$ 6,50", "etanol": "R$ 4,50", "diesel": "R$ 5,50"}

if combustivel in precos:
    print(f"O preço do {combustivel} é {precos[combustivel]} por litro.")
else:
    print("tipo de combustível inválido.")