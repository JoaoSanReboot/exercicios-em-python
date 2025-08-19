#Desenvolver um programa que leia duas notas de um aluno e calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota da sua prova:'))

n2 = float(input('Digite a segunda nota da sua prova:'))

total = (n1 + n2) / 2

print('A média entre {} e {} é igual a {}'.format(n1,n2, total))