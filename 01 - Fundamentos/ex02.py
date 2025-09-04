#Fundamentos primitivos.

num1 = int (input('Digite um valor inteiro para efetuar a soma: \n'))

num2 = int (input('Digite outro valor inteiro para efetuar a soma: \n'))

valorTotal = num1 + num2

#print('A soma entre', num1, 'e', num2, 'é igual:', valorTotal)

#Utilizando o .format para melhorar a qualidade do código.

print('A soma entre {} e {} é igual: {}'.format(num1,num2, valorTotal))