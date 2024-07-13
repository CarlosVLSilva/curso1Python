"""Calculadora com WHILE"""
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-*/): ')
    
    numeros_validos = None
    float_numero1 = 0
    float_numero2 = 0
    
    try:
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)
        numeros_validos = True
        
    except:
        numeros_validos = None
    
    if numeros_validos is None: 
        print('Um ou ambos números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-*/'
    
    if len(operador > 1):
        print('Digite apenas um operador.')
        continue
    
    if operador not in operadores_permitidos:
        print('O operador digitado é inválido.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo.')
    if operador == '+':
        print(f'{float_numero1}+{float_numero2}= ', float_numero1 + float_numero2)
    elif operador == '-':
        print(f'{float_numero1}-{float_numero2}= ', float_numero1 - float_numero2)
    elif operador == '*':
        print(f'{float_numero1}*{float_numero2}= ', float_numero1 * float_numero2)
    elif operador == '/':
        print(f'{float_numero1}/{float_numero2}= ', float_numero1 / float_numero2)
    else:
        print('Não deveríamos chegar até aqui.')

    sair = input('Quer sair? [s]im ').lower().startswith('s')
    
    if sair is True:
        break
