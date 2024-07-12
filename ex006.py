'''
hora = int(input('Digite a hora atual (0 - 23): '))

if hora < 12:
    print('Bom dia!')
elif hora >= 12 and hora < 18:
    print('Boa tarde!')
elif hora >= 18 and hora < 24:
    print('Boa noite')
else:
    print('Valor incorreto. Tente novamente.')
'''

entrada = input('Digite a hora atual (0 - 23): ')

try:
    hora = int(entrada)
    if hora < 12:
        print('Bom dia!')
    elif hora >= 12 and hora < 18:
        print('Boa tarde!')
    elif hora >= 18 and hora < 24:
        print('Boa noite')
    else:
        print('Valor incorreto.')
except: 
    print('Por favor, digite somente números inteiros.')