#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#Primeiro valor é maior
#Segundo valor é maior
#Não existe valor maior, os dois são iguais.

numum = int(input('Digite o valor do primeiro número: '))
numdois = int(input('\nDigite o valor do segundo número: '))

if numum > numdois:
    print('O primeiro valor é o maior.')

elif numdois > numum:
    print('O segundo valor é o maior.')

else:
    print('Ambos são valores iguais não há um número maior.')