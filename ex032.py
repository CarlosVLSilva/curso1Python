# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
        
    res = input('Escolha uma opção: ')
    
    acertou = False
    res_int = None
    qtd_opcoes = len(opcoes)
    
    if res.isdigit():
        res_int = int(res)
        
    if res_int is not None:
        if res_int >= 0 and res_int < qtd_opcoes:
            if opcoes[res_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        print('Acertou!')
    else:
        print('Errou!')
    
    print()
print('Total de acertos: ', qtd_acertos)
