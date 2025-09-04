#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por km
#para viagens até 200km e R$0,45 para viagens mais longas.

quilometragem = int(input('Qual a distância da sua viagem planejada em quilometros? '))

if quilometragem <= 200:
    valor = quilometragem * 0.50
else:
    valor = quilometragem * 0.45

print('Sua viagem de {:.1f}km está prestes a começar.'.format(quilometragem))
print('O valor total da sua passagem será de R${:.2f}.'.format(valor))