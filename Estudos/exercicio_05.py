# Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e a raiz quadrada.
# Modo 1:
numero = int(input("Digite um numero:\n"))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print("O dobro {} é {}.".format(numero, dobro))
print("O triplo {} é {}.".format(numero, triplo))
print("A raiz quadrada de {} é {:.2f}.".format(numero, raiz_quadrada))


# Modo 2:
# numero = int(input("Digite um numero :\n"))
# print("O dobro {} é {}.".format(numero, numero*2))
# print("O triplo {} é {}.".format(numero, numero*3))
# print("A raiz quadrada de {} é {:.2f}.".format(numero, numero**(1/2)))

# Modo 3:
# numero = int(input("Digite um numero :\n"))
# print("O dobro {} é {}.".format(numero, numero*2))
# print("O triplo {} é {}.".format(numero, numero*3))
# print("A raiz quadrada de {} é {:.2f}.".format(numero, pow(numero,(1/2))))