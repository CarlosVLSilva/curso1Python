# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

# print(list(range(10)))
'''lista = []
for numero in range(10):
    lista.append(numero)'''
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento de  dados em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
    ]

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    for produto in produtos
    ]

# print(novos_produtos)
# print(*novos_produtos)
lista = [n for n in range(10)]
print(lista)
