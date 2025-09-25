#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)

valor = 0

termo = int(input('\nPrimeiro termo:'))
razao = int(input('\nRazão:'))
print('\n')

for num in range(1, 11):
    valor = termo + (num - 1) * razao
    print('{} '.format(valor), end='-> ')
print('Acabou!')