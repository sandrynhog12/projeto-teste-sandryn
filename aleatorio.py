# Acertando nº aleatório


import random
valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input('Chute um número: '))
    if chute < valor_aleatorio:
        print('Seu chute foi abaixo do nº aleatório')
    elif chute > valor_aleatorio:
        print('Chute acima do nº aleatório ')
    elif valor_aleatorio == chute:
        acertou = True
        print("Número correto")    