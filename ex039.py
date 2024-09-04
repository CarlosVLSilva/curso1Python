# Dictionary Comprehension e Set comprehension
'''produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

print(dc)
'''


# isinstance - para saber se o objeto é de determinado tipo
'''lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, set))
    
    if isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)'''


# Valores Truthy e Falsy, tipos mutáveis e imutáveis
# Mutáveis []  {}  set()
# Imutáveis ()  ""  0  0.0  None  False  range(0, 10) 
'''lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
float = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('Teste'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro}', falsy(inteiro))
print(f'{float}', falsy(float))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))'''

# dir, hasattre getattr em Python
'''string = 'Luiz'
print(string)'''

# Generator expression, Iterables e Iterators em Python
'''iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__
generator = [n for n in range(10)]
print(generator)'''