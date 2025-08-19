#Faça um algoritmo que leia um salário e calcule o novo valor com a porcentagem de aumento aplicada.

salario = float(input('Qual é o salário do Funcionário? R$'))

salarionovo = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R${:.2F}, com 15% de aumento, passa a receber R${:.2F}.'.format(salario,salarionovo))