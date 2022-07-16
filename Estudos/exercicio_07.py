# Faça um programa que leia o valor em metros e exiba convertido em centimetros e milimetros.

medida = float ("Digite uma distancia em metros:\n")
cm = medida * 100
mm = medida * 1000

print( "O valor de {}m corresponde a {:.0f}cm e {:.0f}mm.".format(medida, cm, mm))