#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
#Com uma pause de um segundo entre eles.

from time import sleep


value = int(input('Vamos acender os fogos? Digite 1 para começara contagem:'))

if value == 1:
    for c in range(9, -2, -1):
        print(c + 1)
        sleep(1.5)
    print('🎆🎆🎆')
else:
    print('Amigo. Dígito errado.')