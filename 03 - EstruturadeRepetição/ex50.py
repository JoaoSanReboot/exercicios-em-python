#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar desconsidere-o.

valorfinal = 0

print('Digite seis números inteiros e farei a soma somente dos números pares.')

for laco in range(1, 7):
    numero = int(input('\nDigite o {}º número: '.format(laco)))
    if numero % 2 == 0:
        valorfinal += numero
print('Somando somente os números pares indicados chegamos no valor {}, correto?'.format(valorfinal))