#Desenvolva uma lógica que leia o peso e altura de uma pessoa e calcule seu IMC, e mostre o seus status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.

print('---------------CALCULADORA DE IMC---------------')
peso = float(input('\nDigite seu peso (Kg): '))
altura = float(input('\nDigite sua altura (m): '))
print('\n---------------CALCULADORA DE IMC---------------')

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('\nVocê está bem Abaixo do peso. Se alimente mais e com qualidade!')

elif IMC < 25:
    print('\nVocê está no Peso ideal, parabéns permaneça cuidando da sua saúde!')

elif IMC < 30:
    print('\nVocê está com Sobrepeso, é indicado melhorar seus habitos alimenticios e se exercitar com mais frequência!!')

elif IMC < 40:
    print('\nVocê está em Obesidade, é indicado a procurar tratamento mental e permanecer cuidando/monitorando seus maus hábitos.')

else:
    print('Procura um médico pois você já está em Obesidade mórbida.')