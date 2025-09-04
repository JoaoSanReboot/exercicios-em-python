#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Informe três segmentos: \n')
a = float(input('Primera reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acimas podem sim formar um trângulo!!')
else:
    print('O segmentos indicados não podem formar um triângulo.')
