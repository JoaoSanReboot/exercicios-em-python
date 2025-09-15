#Refaça o exercício 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais.
# Isósceles: Dois lados iguais.
# Escaleno: Todos os lados diferentes.

print('Informe três segmentos: \n')
a = float(input('Primero segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:

    if a == b == c:
        print('Os segmentos indicados podem formar um triângulo Equilátero.')
    
    elif a != b != c != a:

        print('Os segmentos indicados podem formar um triângulo Escaleno.')

    else:
        print('Os segmentos indicados podem formar um triângulo Isósceles.')

else:
    print('O segmentos indicados não podem formar um triângulo.')
