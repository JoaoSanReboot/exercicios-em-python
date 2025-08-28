#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Qual seu nome completo? ')).split()

nome = nome.title()

print('Silva' in nome)

