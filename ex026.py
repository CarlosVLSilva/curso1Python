# Exercícios com funções 

# Crie uma função que multiplica todos os argumentos não 
# nomeados recebidos.
# Retorne o total para uma variável e mostre o valor da 
# variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total += numero
    return total

entrada_numeros = 1, 2, 3, 4, 5
multiplicacao = multiplica(*entrada_numeros)
print(multiplicacao)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par' 
    return f'{x} é ímpar'

print(par_impar(x))
