# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

'''def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return

    """yield 1 # pausa a função aqui
    #return 'acabou'
    print('Continuando...')
    yield 2 # pausa a função aqui
    print('Mais uma vez...')
    yield 3 # pausa a função aqui
    print('Vamos terminar')
    return 'Acabou'"""
    
gen = generator(maximum=614)
for n in gen:
    print(n)'''
#-----------------------------------------------------------
# Yield from
def gen1():
    print('Começo')
    yield 1
    yield 2
    yield 3
    print('Fim do Gen1')
    
def gen3():
    print('Começo')
    yield 10
    yield 20
    yield 30
    print('Fim do Gen3')
    
def gen2(gen):
    print('Começo')
    yield from gen1()
    yield 4
    yield 5
    yield 6
    print('Fim do Gen2')

g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
