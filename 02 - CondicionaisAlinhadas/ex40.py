#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final de acordo com sua média atingindo:
# Média abaixo de 5.0 - Reprovado.
# Média entre 5.0 e 6.9 - Recuperação.
# Média 7.0 ou superior - Aprovado.

print('-' * 32)
print('Calculadora de média UniEnsinoJS')
print('-' * 32)

notaum = float(input('\nDigite a nota da sua primeira prova: '))
notadois = float(input('\nDigite a nota da sua segunda prova: '))

media = (notadois + notaum) / 2

if media < 5.0:
    print('Sua média final é de {} você está \033[31mReprovado\033[m!!'.format(media))

elif media <= 6.9:
    print('Sua média final é de {} você está de \033[31mRecuperação\033[m estude mais!!'.format(media))

else:
    print('Sua média final é de {} você está \033[32mAprovado\033[m. Parabéns!!!'.format(media))