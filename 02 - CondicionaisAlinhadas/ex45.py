#Crie um programa que faça o computador jogar jokenpô com você.

from time import sleep
from random import randint

print('\nVamos jogar Jokenpô ?\n')
print('Escolha uma das opções abaixo:\n')
print(' [ 0 ] - PEDRA')
print(' [ 1 ] - PAPEL')
print(' [ 2 ] - TESOURA')

opcao = int(input('\nQual sua jogada? '))

if opcao in [0, 1, 2]:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!\n')
    sleep(1)

    jogadas = ['Pedra', 'Papel', 'Tesoura']

    computadorescolha = randint(0, 2)

    print('Você escolheu \033[35m{}.\033[m'.format(jogadas[opcao]))
    print('E o Computador escolheu \033[34m{}.\033[m'.format(jogadas[computadorescolha]))

    if computadorescolha == opcao:
        print('\nEmpatamos!')

    elif (opcao - computadorescolha) % 3 == 2:
        print('\n\033[31mGanhei de você Noob XD!!\033[m')

    else:
        print('\n\033[32mParábens você ganhou!!\033[m')

else:
    print('Opção inválida! Aprende a brincar.')