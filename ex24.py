#Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Informe o nome de uma cidade: ')).strip()

cidade = cidade.capitalize()

print('Santo' in cidade)

 