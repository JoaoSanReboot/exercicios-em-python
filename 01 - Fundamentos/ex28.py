#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário,
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

robo = randint(0,5)

print('-=-' * 20)
jogador = int(input('Em qual número entre 0 a 5 eu estou pensando? '))

print('-=-' * 20)
print('\n PROCESSANDO... \n')
sleep(1)
print('-=-' * 20)

if jogador == robo:
    print('Paranéns! Você acertou o número que pensei era {} mesmo.'.format(robo)) 
else:
    print('Boa tentativa, mas o número corrreto era {}. Você perdeu!'.format(robo))
print('-=-' * 20)