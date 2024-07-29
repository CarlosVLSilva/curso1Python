'''
Cálculo do primeiro dígito do CPF:

Coletar a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

EX: 746.824.890-70 (74682489070)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
   
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O primeiro dígito do CPF é 7
'''

cpf = '74682489070'
nove_digitos = cpf[0:9] #fatiamento
contador_regressivo1 = 10

resultado1 = 0
for digito in nove_digitos:
    resultado1 = resultado1 + int(digito) * contador_regressivo1
    contador_regressivo1 -= 1
primeiro_digito = (resultado1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)

dez_digitos = cpf[0:10]
contador_regressivo2 = 11

'''
Cálculo do segundo dígito do CPF:

Coletar a soma dos 9 primeiros digitos do CPF
MAIS O PRIMEIRO DÍGITO
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11

EX: 746.824.890-70 (74682489070)
   11  10  9  8  7  6  5  4  3  2
*  7   4   6  8  2  4  8  9  0  7
   77  40  54 64 14 24 40 36 0  14
   
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O segundo dígito do CPF é 0
'''

resultado2 = 0 
for digito in dez_digitos:
    resultado2 = resultado2 + int(digito) * contador_regressivo2
    contador_regressivo2 -= 1
segundo_digito = (resultado2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(segundo_digito)

