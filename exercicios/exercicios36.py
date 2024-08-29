# Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente. 

mes = int(input("digite um numero de 1 a 12"))
meses = [ "janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= mes <= 12:
    print(f" {meses[mes-1]}.")
else:
    print("Número Inválido. Digite um número de 1 a 12.")
