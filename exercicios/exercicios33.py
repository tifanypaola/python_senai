# Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

valor = float(input("Digite o valor do produto: "))
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print(f"O valor com 10% de desconto é: R$ {valor_com_desconto:.2f}")
