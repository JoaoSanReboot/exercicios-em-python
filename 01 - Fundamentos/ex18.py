#Crie um programa que leia um ângulo qualquer e mostre o valor de seno, cosseno e tangente deste ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(angulo))

cos = cos(radians(angulo))

tan = tan(radians(angulo))

print('O ângulo {} possuí as seguintes medidas trigonométricas:\n'
      'Seno: {:.2f} \n'
      'Cosseno: {:.2f} \n'
      'Tangente: {:.2f} \n'.format(angulo,sen,cos,tan))
    