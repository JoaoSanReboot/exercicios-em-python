#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acida do limite. 

velocidade = int(input('DETRAN: Sabe me dizer qual a velocidade que você antingiu no trecho da BR277 ? \n'))

if velocidade > 80:

    #Calcula quantos reais de umlta será pago.
    valorMulta = (velocidade - 80) * 7

    #Informa a porcentagem da velocidade excedida.
    porcentagem = velocidade - 80
    porcentagem = porcentagem * 0.8

    print('\nDETRAN: MULTADO!! Você excedeu {:.0f}% do permitido. A velocidade máxima da via é 80Km/h'.format(porcentagem))
    print('DETRAN: Você deve pagar uma multa de R${:.2f}.'.format(valorMulta))
else:
    print('\n DETRAN: Parabéns, você está no limite da via.')