nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Por favor, digite mais de uma letra.')


'''if len(nome) <= 4:
    print('Esse é um curto nome.')
elif len(nome) >= 5 and len(nome) <= 6:
    print('É um nome comum.')
else: 
    print('Seu nome é muito grande.')'''