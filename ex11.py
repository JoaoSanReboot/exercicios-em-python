#Faça um algoritmo que leia um valor e mostre seu novo valor com 5% de desconto.

produto = float(input('Digite o valor do produto: R$'))

valorfinal = produto - (produto * 5 / 100)

print('O valor informado de {} com o 5% de desconto aplicado fica no valor de {:.2f}'.format(produto,valorfinal))