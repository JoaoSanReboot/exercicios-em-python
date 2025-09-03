#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe qual seu salário atual: '))

if salario <= 1250.00:
    salarioAumentado = salario + (salario * 0.15)

else:
    salarioAumentado = salario + (salario * 0.10)

print('Parabéns!! Você recebeu um aumento 10%, de R${:.2f} você passa a recebe R${:.2f}.'.format(salario, salarioAumentado))