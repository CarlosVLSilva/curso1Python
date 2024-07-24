#Imprecisão do ponto flutuante
import decimal 

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7') 
n3 = n1 + n2
print(n3) #float
print(f'{n3:.2f}') #string
print(round(n3, 2)) #float

