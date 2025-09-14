#Faça um programa que leia o ano de nascimento de uma jovem e infomre, de acordo com sua idade:
# Se ela ainda vai se alistar ao serviço militar.
# Se é hora de se alistar.
# Se já passou o tempo de alistamento.
#Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('-' * 45)
print('Seja Bem-Vindo ao Serviço Militar Obrigatório')
print('-' * 45)
jovemidade = int(input('\nInforme seu ano de nascimento: '))


if jovemidade == 18:
    print('O Sr. está na idade de alistamento obrigatório. Verifique a agenda e se apresente a unidade militar mais próxima.')

elif jovemidade < 18:
    prazo =  18 - jovemidade
    print('O Sr. ainda não está na idade do alistamento obrgatório. Faltam {} anos para seu alistamento.'.format(prazo))

else:
    prazo = jovemidade - 18
    print('O Sr. JÁ PASSOU {} ANOS DO PRAZO. FAÇA O FAVOR DE SE APRESENTAR IMEDIATAMENTE A UNIDADE MAIS PRÓXIMA!!!!!'.format(prazo))