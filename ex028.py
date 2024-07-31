'''
Closure e funções que retornam outras funções

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar
    
s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Luiz')

print(s1())
print(s2())
'''

#Exercício 
#Crie funções que duplicam, triplicam e quadruplicam 
#o número recebido como parâmetro.

'''def duplicar(numero):
    return numero * 2
    
def triplicar(numero):
    return numero * 3
    
def quadruplicar(numero):
    return numero * 4'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
