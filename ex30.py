#Crie um programa que leia um número inteiro e mostre na tela se ele é impar ou par.

num = int(input('Informe um número aleatório que eu vou identificar se ele é Ímpar ou Par: \n'))

resultado = num % 2

if resultado == 0:
    print('O número {} é Par.'.format(num))
else:
    print('O número {} é Ímpar.'.format(num))