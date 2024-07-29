"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual 
Argumento não nomeado recebe apenas o argumento (valor)
"""

"""def soma(x, y):
    #Definição
    print(f'{x=} + {y=}', '|', 'x + y = ', x+y)
    
soma(1, 2)
soma(y=2, x=1)"""

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter vaores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=} = ', x+y+z)
    else:
        print(f'{x=} + {y=} = ', x+y)

soma(1, 2, 0)
soma(3, 5, 2)
soma(100, 200)
