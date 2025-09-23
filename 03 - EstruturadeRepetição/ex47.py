#Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50.

for c in range (1,51):
    valor = c % 2
    if valor == 0:
        print(c)
    