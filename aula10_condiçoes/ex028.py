from random import randint
computador = randint(0, 5)#Pensando
print('PROCESSANDO...')
print('Vou pensar em um numero de 0 a 5, tente adivinhar...')
print('PROCESSANDO...')

jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Você acertou! parabens')
else:
    print('Você errou! Que pena!')
print('O numero que eu pensei foi {}'.format(computador))
