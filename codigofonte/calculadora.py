print('CALCULADORA')
print('=-=' *10)

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

menu = 0
while menu !=5:
    print('''
    [1] SOMA
    [2] DIVISÃO
    [3] MULTIPLICAÇÃO
    [4]SUBTRAÇÃO
    '''
    )
    menu = int(input('Qual opção você deseja realizar? '))
    if menu == 1:
        print('{} + {} = {}'.format(a, b, a+b))
    elif menu == 2:
        print('{} / {} = {}'.format(a, b, a/b))
    elif menu == 3:
        print('{} X {} = {}'.format(a, b, a*b))
    elif menu == 4:
        print('{} - {} = {}'.format(a, b, a-b))
    else:
        print('Opção inválida.')
    print('=-'*10)
print('Encerrando o programa...')
