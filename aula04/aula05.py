
# numero1 = 10
# numero2 = 10

# operador maior
# print(numero1 > numero2)
# print(numero2 > numero1)

# #operador menor
# print(numero1 < numero2)
# print(numero2 > numero1)

# print(numero1 == numero2)
# print(numero1 >= numero2)
# print(numero1 <= numero2)
# print(numero1 != numero2)

# idade = int(input('informe sua idade: \n'))

# if (idade > 120):
#     print('idade invalida')
# elif(idade >= 18):
#     print('Maior de Idade')
# elif(idade < 0):
#      print('ainda nao nasceu')
# else:
#     print('menor de idade')

# idade = int(input('informe sua idade: \n'))

# if (idade >= 18):
#     print('Pode assistir o filme')
# elif(idade >= 16): 
#     acompanhado =input('Esta acompanhado de adulto? sim ou não? \n')
#     if (acompanhado == 'sim'):
#         print('pode assistir')
#     else: 
#         print('não pode assistir')
# else: 
#     print('não pode assistir')

# idade = int(input('Informe sua idade: \n'))

# if (idade < 18):
#    acompanhado =input('Esta acompanhado de adulto sim ou não \n')
#    if (acompanhado == 'sim'):
#        print('pode assistir')
#    else:
#        print('não pode assistir')
# else:
#     print('pode assistir')

Alladin = input('Alladin apareceu? \n')
Jasmine = input('Jasmine apareceu? \n')

if not((Alladin == 'sim') or (Jasmine == 'sim')):
   print('Love a noite inteira')
else: 
    print('não rolou encontro')