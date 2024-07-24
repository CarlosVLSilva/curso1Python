#split e join com list e str
#split = divide uma string
#join = une uma string

frase = '      Olha só que coisa    ,      interessante    '
lista_palavras_cruas = frase.split()

lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())
    
'''print(lista_palavras_cruas)
print(lista_palavras)'''
palavras_unidas = ' '.join(lista_palavras)
print(palavras_unidas)
