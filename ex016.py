'''
Exercício:
Exiba os índices da lista
'''
#Opção 1
lista = ['Maria', 'Helena', 'Luiz', 4, 1.5, True]
lista.append('Joao')

i = 0
for nome in lista:
    print(i, nome, type(nome))
    i = i + 1 

#Opção 2
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
