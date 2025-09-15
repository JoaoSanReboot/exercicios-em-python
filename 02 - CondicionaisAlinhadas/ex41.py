#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos - Mirim.
# Até 14 anos - Infantil.
# Até 19 anos - Junior.
# Até 20 anos = Sênior.
# Acima - Master.

from datetime import date

print('-' * 53)
print('Seja Bem-Vindo(a) A Confederação Nacional de Natação!')
print('-' * 53)
ano = int(input('Informe seu ano de nascimento para verificarmos sua categoria: '))

anoatual = date.today().year
idade = anoatual - ano

if idade <= 9:
    print('\nSua categoria é \033[34mMirim.\033[m')
elif idade <= 14:
    print('\nSua categoria é \033[35mInfantil.\033[m')
elif idade <= 19:
    print('\nSua categoria é \033[36mJunior.\033[m')
elif idade <= 25:
    print('\nSua categoria é \033[31mSenior.\033[m')
else:
    print('\nSua categoria é \033[32mMaster.\033[m')