#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Souza - Primeiro: Ana, último: Souza

nome = str(input('Digite seu nome:')).strip()

nomeSplitado = nome.split()

print('Seu primeiro nome é {} e seu último nome é {}, correto?'.format(nomeSplitado[0], nomeSplitado[-1]))
