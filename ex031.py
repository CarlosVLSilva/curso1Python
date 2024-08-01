'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

'''pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 50
}
'''
# print(len(pessoa)) #encurtado de print(pessoa.__len__())
# print(list(pessoa.keys()))

'''for chave in pessoa:
    print(chave)'''
    
# print(list(pessoa.values()))
# print(list(pessoa.items()))

'''pessoa.setdefault('idade', None)
print(pessoa['idade'])'''

'''import copy # shallowcopy e deepcopy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = d1.copy()
# d2 = copy.deepcopy(d1) # deepcopy

d2['c1'] = 1000
d2['l1'] = 999999

print(d1)
print(d2)'''

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Otávio',
}
#print(p1['nome'])
#print(p1.get('nome', 'Não existe'))
#nome = p1.popitem()
#print(nome)
#print(p1)

p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
print(p1)
