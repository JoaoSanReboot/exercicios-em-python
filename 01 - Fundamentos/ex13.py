#Crie um algoritmo que leia uma temperatura e converta para fahrenheit.

temperatura = float(input('Informe a temperatura em °C:'))

temperaturaF = 32 + (temperatura * 1.8)

print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'. format(temperatura,temperaturaF))