#Faça um programa que leia altura e largura de uma parede em metros, e calcule a sua área e a quantidade para pintá-la.
#Sabendo que cada litro de tinta rende 2m².

Lp = float(input('Informe a largura da parede:'))

Ap = float(input('Informe a altura da parede:'))

Ar = Lp * Ap

Tinta = Ar / 2

print('Sua parede tem {}x{} e sua área é de {:.3f}m². \n' \
'Para pintar está parede será necessario utilizar {:.3f}l'.format(Lp,Ap,Ar, Tinta))