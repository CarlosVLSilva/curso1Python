# Empacotamento e desempacotamento de dicionários 

a, b = 1, 2 
a, b = b, a
# print(a, b)

# a, b = pessoa.values()
# print(a, b)

# for chave, valor in pessoa.items():
#     print( chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_args_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_args_nomeados(nome='Joana', qLq=123)
# mostro_args_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_args_nomeados(**configuracoes)
