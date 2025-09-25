#Refaça o ex09, mostrando uma tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Digite o número que deseja saber a tabuada: '))

for num in range(0, 11):
    valorfinal = tabuada * num
    print('{} x {} = {}'.format(tabuada,num,valorfinal))
print('Fim da Tabuada!')