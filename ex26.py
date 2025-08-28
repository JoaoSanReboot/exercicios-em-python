#Faça um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece pela primera vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase aleatória: ')).strip()

frase = frase.upper()

print('Na sua frase a letra A aparece {} vezes.'. format(frase.count('A')))
print('Na sua frase a letra A aparece pela primeira vez na posição {}.'. format(frase.find('A')+1))
print('Na sua frase a letra A aparece pela útlima vez na posição {}.'. format(frase.rfind('A')+1))

