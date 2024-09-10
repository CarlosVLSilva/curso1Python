# Try, except, else e finally

"""try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError.')
    print('MSG:', error)
    print('MSG:', error.__class__.__name__)
except Exception:
    print('Erro desconhecido.')
    
print('CONTINUAR')"""

# Try, except, else e finally Aula 2

try:
    print('Abrir arquivo')
    #8/0
except ZeroDivisionError: #trata exceção
    print('Dividiu zero')
except (NameError, ImportError): # Trata dois erros de uma só vez
    ...
except IndexError as e: # Captura o erro em uma instância
    ...
else:
    print('Não deu erro')
finally: # não trata exceção
    print('Fechar artquivo')