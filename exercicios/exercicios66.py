
nomes = ['Luciano', 'Lucas', 'Matheus']

operacao = 'sim'

while operacao == 'sim':
    print(' 1 cadastre nome')
    print(' 2 atualize nome')
    print(' 3 exclua nome')
    print(' 4 listar nomes')
    opcao = int(input('Informe a ação desejada. '))

    match opcao:
        case 1:
            nome = input('que nome deseja cadastrar: ')
            nomes.append(nome)
        case 2:
            nome = input('que nome deseja atualizar? ')
            novo_nome = input('qual será o novo nome?')
            
            nomes[nomes.index(nome)] = novo_nome
        case 3:
            nome = input('Que nome deseja remover? ')
            nomes.remove(nome)
        case 4:
            for indice, nome in enumerate(nomes):
                print(f'{indice} - {nome}')
        case _:
            print('opção invalida')

        
    operacao = input('Deseja realizar outra operação? ').lower()

    if operacao == 'nao':
        break 