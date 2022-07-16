# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

# Considere U$$: 1,00 = R$: 5,38


real = float(input("Olá! Quanto de dinheiro você tem na sua carteira\n? R$:"))
dolar = real / 5.38


print("Com R${:.2f},você pode comprar U$${:.2f}".format(real, dolar))