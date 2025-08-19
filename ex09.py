#Escreve um programa que leia a quantia de dinheiro de uma pessoa e mostre quantos kwanzas ela pode comprar.

real = float(input('Qual saldo atual da sua carteira? \n R$'))
kz = real / 0.0059

print('Com R${} você pode comprar Kz{:.2f}'.format(real, kz))