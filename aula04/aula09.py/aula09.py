
texto = 'tifany Paola Pereira Lima    '

texto2 = texto.capitalize()
# capitalize muda o primeiro caracter da string para maiusulo
print(texto.capitalize())
print(texto2)

# lower padroniza a string em minusculo

nome = 'TiFaNy PaOlA pErEiRa LiMa'
nome2 = 'tifany paola pereira lima'


if nome.lower() == nome2.lower():
     print('são iguais')
else:
    print('Não são iguais')

# UPPER padroniza uma string em maiusculas 

print(nome.upper())

# replace muda um padrão de caracteres de uma string 

silvano_sales = 'coração coração cabeção'

# silvano_sales2 = silvano_sales.replace('ç', 'c')
# silvano_sales2 = silvano_sales2.replace('ã' , 'a')

print(silvano_sales.replace('çã', 'ca'))

# strip é uma forma de remover caracteres em branco no final e no inicio de uma string

jack_stripador = '         removendo espaços de uma string      '

print(jack_stripador)
print(jack_stripador.strip())

# split divide uma string em elemenstos de uma lista 

string_espalhada = 'Tifany paola pereira lima'

print(string_espalhada)
print(string_espalhada.split())

# join transforma os elementos de uma lista em uma string 
# concatena strings

nome_lista = ['tifany', 'paola', 'pereira']

# print(' '.join(nome_lista), '\n')

dominio = 'aluno.senai.br'

# slice manipula string por indice

cidade = 'Recanto das emas, cidade do povo'

print(cidade[::-1])

palindromo = 'arara'

if palindromo.lower() == palindromo[::-1].lower():
    print('é palindromo')
else:
    print('não é palindromo')



