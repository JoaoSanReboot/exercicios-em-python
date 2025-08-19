#Faça um programa que leia o comprimento dos catetos de um triangulo retângulo e calcule o comprimento da hipotenusa.

import math

catetooposto = int(input('Digite o comprimento do cateto oposto: '))

catetoadjacente = int(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = math.hypot(catetooposto, catetoadjacente)

print('A soma do cateto oposto {} e do cateto adjacente {} ao quadrado é igual a hipotenusa de: {:.2f}'.format(catetooposto,catetoadjacente,hipotenusa))