# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input("Digite o número do mês (1 a 12): "))

if mes in [12, 1, 2]:
    estacao = "verão"
elif mes in [3, 4, 5]:
    estacao = "outono"
elif mes in [6, 7, 8]:
    estacao = "inverno"
elif mes in [9, 10, 11]:
    estacao = "primavera"
else:
    estacao = "m inválido."

print(f"a estação do ano é {estacao}.")
