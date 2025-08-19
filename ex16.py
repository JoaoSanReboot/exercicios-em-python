#Crie um programa que leia um número real e mostre a porção da sua inteira.

import math

num = float(input('Digite um número quebrado: '))

print('O número {} tem a parte inteira {}'.format(num, math.floor(num)))