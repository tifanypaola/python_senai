# Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia = int(input("Digite um número de 1 a 7 para o dia da semana: "))
dias_semana = {1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira", 4: "Quarta-feira", 5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado"}

if dia in dias_semana: 
    print(f"{dias_semana[dia]}.")
else:
    print("Número inválido. Por favor, digite um número de 1 a 7.")
