#Escreva um programa que leia um número inteiro e qualquer peça para o usúario escolher qual base será usada para conversão:
# 1 para Binário.
# 2 para Octal.
# 3 para Hexadecimal.

baseum = int (input('Digite um número inteiro: '))
print('\n Escolha uma das bases abaixo para efetuar a conversão: \n')
print('[ 1 ] Converter para Binário. \n')
print('[ 2 ] Converter para Octal. \n')
print('[ 3 ] Converter para Hexadecimal. \n')
opcao = int (input('Digite uma das opções acima: '))

if opcao == 1:

    basebinario = bin(baseum)[2:]
    print('O número {} convertido para Binário é igual a {}.'.format(baseum, basebinario))

elif opcao == 2:

    baseoctal = oct(baseum)[2:]
    print('O número {} convertido para Octal é igual a {}.'.format(baseum, baseoctal))

elif opcao == 3:

    basehexa = hex(baseum)[2:]
    print('O número {} convertido para Octal é igual a {}.'.format(baseum, basehexa))

else:
    print('\n Você não digitou nenhuma das opções indicadas, por gentileza realize novamente a atividade.')