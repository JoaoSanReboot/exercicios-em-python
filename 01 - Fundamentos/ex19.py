#Crie um programa que leia o nome de quatro alunos e sorteie um nome entre eles para determinada função.

import random

nomes = []

aluno1 = str(input('Informe o nome do primeiro aluno: \n'))
nomes.append(aluno1)

aluno2 = str(input('Informe o nome do segundo aluno: \n'))
nomes.append(aluno2)

aluno3 = str(input('Informe o nome do terceiro aluno: \n'))
nomes.append(aluno3)

aluno4 = str(input('Informe o nome do quarto aluno: \n'))
nomes.append(aluno4)

sorteado = random.choice(nomes)

print('O aluno escolhido para limpar a sala de aula é o {}'.format(sorteado))