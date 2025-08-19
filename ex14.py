#Escreva um programa que leia a quantidade de km percorridos por um carro e quantidade de dias que ele foi alugado.
#Calcule o preço a pagar, sabendo que o preço a pagar por dia é R$60,00 e por km são R$0.15.

dias = int(input('Informe quantos dias você alguou o veículo: '))

km = float(input('Informe quantos Km foram rodados: '))

valortotal = (dias * 60.00) + (km * 0.15)

print('O valor total a pagar é R${:.2F}'.format(valortotal))