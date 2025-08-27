#Crie um programa que leie o nome completo de uma pessoa e mostre:
# 1º O nome com todas as letras maiúsculas.
# 2º O nome com todas as letras minúsculas.
# 3º Quantas letras ao todo (sem considerar espaços).
# 4º Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: \n'))

# 1º
nomeMaiusculo = nome.upper()

# 2º
nomeMinusculo = nome.lower()

# 3º
nomeSemEspaco = nome.replace(" ", "")

nomeSemEspaco = len(nomeSemEspaco)

# 4º
nomeLetras = nome.split()

print('Seu nome em maiúsculas é:', nomeMaiusculo)
print('Seu nome em minúsculas é', nomeMinusculo)
print('Seu nome tem ao todo {} letras'.format(nomeSemEspaco))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomeLetras[0], len(nomeLetras[0])))