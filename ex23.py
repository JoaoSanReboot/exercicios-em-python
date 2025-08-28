#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex:
# 1834 - Unidade:4, Dezena:3, Centena:8, Milhar:1

num = int(input('Informe um número: '))

u = num % 10

d = num // 10 % 10

c = num // 100 % 10

m = num // 1000 % 10

print('Analisando o número {} \n'
      'Unidade: {} \n'
      'Dezena: {} \n'
      'Centena: {} \n'
      'Milhar: {} \n'.format(num,u,d,c,m))
