from random import randint
computador = randint(0,5)  #faz o computador "PENSAR"
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5, Tente adivinhar')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? '))  #Jogador tenta adivinhar
if jogador == computador:
    print('PARABENS!Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))