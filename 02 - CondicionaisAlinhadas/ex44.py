#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição do pagamento:
# À vista dinheiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# Em até 2x no cartão: Preço normal.
# Em 3x ou mais no cartão: 20% de juros.

print('=' * 10, '| Lojas JS |', '=' * 10)

valorTotal = float(input('Informe o valor total das suas compras: '))

print('=' * 25)
print('Escolha uma das formas de pagamento abaixo:')
print('[ 1 ] À vista dinheiro/cheque.')
print('[ 2 ] À vista cartão.')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão.')

opcao = int(input('Qual das opções? '))

if opcao == 1:

    desconto = valorTotal * 0.10
    valorFinal = valorTotal - desconto
    print('O valor de R${:.2f} com desconto de 10% À vista fica por \033[32mR${:.2f}.\033[m'.format(valorTotal, valorFinal))

elif opcao == 2:

    desconto = valorTotal * 0.05
    valorFinal = valorTotal - desconto
    print('O valor de R${:.2f} com desconto de 5% À vista fica por \033[32mR${:.2f}.\033[m'.format(valorTotal, valorFinal))

elif opcao == 3:
    
    parcela = (valorTotal / 2)
    print('Em até duas vezes o valor total fica R${:.2f}, com parcelas de R${:.2f}.'.format(valorTotal, parcela))

elif opcao == 4:

    quantidadeparcela = int(input('Qauntas vezes deseja fazer: '))
    valorFinal = valorTotal + (valorTotal * 0.20)
    parcela = (valorFinal / quantidadeparcela)
    print('Em até {} vezes o valor total fica \033[31mR${:.2f}.\033[m, com parcelas de R${:.2f} com juros.'.format(quantidadeparcela, valorFinal, parcela))

else:
    print('Insira uma das opções validas do sistema.')