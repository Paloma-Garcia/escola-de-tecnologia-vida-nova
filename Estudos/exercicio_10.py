# Faça um programa que leia a largura e a altura da parede em metros, 
# calcule a sua área e a quantidade de tinta necessaria para pintá-la,
# Sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Qual a largura da parede?\n"))
altura = float(input("Qual a largura da parede?\n"))
area = largura * altura

print("Sua parede tem a dimensão de {}x{} e a sua area é de {} m².".format(largura, altura, area))
tinta = area / 2
print("Para pintar essa parede, você vai precisar de {}l de tinta.".format(tinta))