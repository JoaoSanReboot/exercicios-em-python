#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

value = 0
contador = 0

for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
           value += c
           contador = contador + 1
print('A soma dos {} números ímpares múltiplos de três é igual a {}'.format(contador,value))