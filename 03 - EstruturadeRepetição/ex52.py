#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número e vou te dizer se ele é Primo ou não: \n'))

tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print('\n\nO número {} foi dívisível {} vezes'.format(num, tot))

if tot == 2:
    print('Por está razão ele \033[32mé\033[m um número Primo!')
else:
    print('Por está razão ele \033[31mnão\033[m é um número Primo')