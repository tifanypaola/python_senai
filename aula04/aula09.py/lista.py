
# cavaleiros = ['Seya', 'Shun', 'Shiryu', 'Yoga']

# print(cavaleiros)

# # adiciona um novo elemento ao final da lista
# cavaleiros.append('Ikki')
# print(cavaleiros)

# cavaleiros.extend(['Shina', 'Maryn'])
# print(cavaleiros)

# # inserir na lista em uma posição especifica
# cavaleiros.insert(0, 'Athena')
# print(cavaleiros)

# # remove, exlui um elemento pelo valor.
# cavaleiros.remove('Shun')
# print(cavaleiros)

# # pop - exclui o ultimo elemento da lista ou o indice informado
# elemento = cavaleiros.pop()

# cavaleiros.pop(0)
# print(cavaleiros)
# print(elemento)

# # indice -  retorna o indice da primeira ocorrencia de um valor procurado 
# print(cavaleiros.index('Yoga'))
# print(cavaleiros)

# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
# print(cavaleiros)

# # contabilizando quantidade de elementos repetidos 
# print(cavaleiros.count('Aldebaran'))

# sort ordena a lista de forma crescente 
frutas = ['morango', 'maçã', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja', 'bergamota' ]

numeros = [ 9 , 5 , 81, 100, 33, 21, 2]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

frutas.reverse()
print(frutas)
print(numeros)

del frutas[0]
print(frutas)

frutas.clear()
print(frutas)

del frutas
print(frutas)