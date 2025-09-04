#Escrever um programa que leia um valor em metros e converta para as demais medidas.

medida = float(input('Digite uma distância em metros:'))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A distancia em {}m corresponde as seguintes medidas:\n'
      '{}km \n'
      '{}hm \n'
      '{}dam \n'
      '{:.0f}dm \n'
      '{:.0f}cm \n'
      '{:.0f}mm \n'.format(medida,km,hm,dam,dm,cm,mm))
