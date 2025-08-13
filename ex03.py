n1 = input('Digite algo: \n')

print('O tipo primitivo deste valor é', type(n1))

print('Só tem espaços?', n1.isspace())

print('É um número?', n1.isnumeric())

print('É alfabético?', n1.isalpha())

print('É alfanúmerico?', n1.isalnum())

print('Está em maiúsculo?', n1.isupper())

print('Está em minúsculo?', n1.islower())

print('Está capitalizada:', n1.istitle())

#Praticando a sintaxe is.

#Detalhe: Verifiquei que a sintaxe isalnum deveria acusar o EX: P A M O N H A 0 1 ser alfanúmerico, porém ele retorna como false? Será que por conta dos espaços? 
#(Analisar posteriormente)