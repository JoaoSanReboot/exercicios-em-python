#Crie um programa que leia o nome de quatro alunos e embaralhe a ordem de apresentação do trabalho.

from random import shuffle

n1 = str(input('Informe o nome do primeiro aluno: '))

n2 = str(input('Do segundo aluno: '))

n3 = str(input('Do terceiro aluno: '))

n4 = str(input('Do quarto aluno: '))

alunos = [n1,n2,n3,n4]

shuffle(alunos)

print('A ordem de apresentação do trabalho será: \n')
print(alunos)

