#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O Programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# OBS: Neste exercício inclui a taxa de juros fixa para ficar algo mais interessante e prático.

from time import sleep

print('-' * 48)
print('Seja Bem-vindo ao impréstimo Imobiliário BancoJS')
print('-' * 48)
print('Vamos calcular o valor do seu empréstimo e verificar a disponibilidade do crédito. \n')

imovel = float(input('Qual valor do seu ímovel: \n'))
renda = float(input('Qual sua renda atual: \n'))
ano = int(input('Em quantos anos deseja finalizar as prestações: \n'))

print('\nCalculando...\n')
sleep(2)

valormensal = (1 + 0.04) ** (1/12) - 1

valorprestacao = imovel * valormensal / (1 - (1 + valormensal) ** - (ano * 12))

if valorprestacao > renda * 0.30:
    print('Infelizmente não será possível iniciar o crédito com o BancoJS visto que o valor da prestação excede 30% do seu salário.')
else:
     print('É possível iniciar o crédito com as condiçoes indicadas!! Vamos evoluir juntos com o BancoJS.')