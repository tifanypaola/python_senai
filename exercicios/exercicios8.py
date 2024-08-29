#  Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado_civil = input("Qual o seu estado civil (solteiro, casado, divorciado, viúvo): ").lower()

if estado_civil == "solteiro":
    print("solteiro.")
elif estado_civil == "casado":
    print("casado.")
elif estado_civil == "divorciado":
    print("divorciado.")
elif estado_civil == "viúvo":
    print("viúvo.")
else:
    print("Estado civil inválido.")