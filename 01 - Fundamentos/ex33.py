#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Informe três números: \n')

num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
num3 = int(input('Terceiro número:'))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('O maor valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))