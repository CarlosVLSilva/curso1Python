nome = input("Qual seu nome? ")
altura = float(input("Qual a sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura * altura)

print(f"{nome} tem {altura}m de altura, pesa {peso} quilos e seu IMC é {imc:.3f}")
print()
print('{} tem {}m de altura, pesa {} quilos e seu IMC é {:.3f}'.format(nome, altura, peso, imc))
