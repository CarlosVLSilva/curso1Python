entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0 
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'Esse número {entrada_int} é {par_impar_texto}.')
else:
    print('Você não digitou um número inteiro.')