import os 

palavra_secreta = 'agua'
letras_certas = ''
cont = 0

while True:
    digito = input('Digite uma letra: ')
    cont += 1
    
    if len(digito) > 1:
        print('Por favor, digite apenas uma letra.')
        print('-----------------------------------')
        continue
    
    if digito in palavra_secreta: 
        letras_certas += digito
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Parabéns! Você ganhou!')
        print('A palavra secreta era', palavra_secreta)
        print('Tentativas: ', cont)
        letras_certas = ''
        cont = 0
