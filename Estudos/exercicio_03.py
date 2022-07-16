#Faça um programa que leia palavra pelo teclado e mostre na tela seu tipo primitivo,
# e todas as informações possiveis sobre ele.

from curses.ascii import isalpha


palavra  = input("Digite uma palavra:")
print("O tipo primitivo desse valor é", type(palavra))
print("Só tem espaços?", palavra.isspace())
print("É um número?",palavra.isnumeric())
print("É alfabético?", palavra.isalpha())
print("É alfanúmerico?", palavra.isalnum())
print("Está em maiúsculas?", palavra.isupper())
print("Está em minúscula", palavra.islower())
print("Está capitalizada?", palavra.istitle())

# É visivel neste código que (palavra) é uma objeto.
# Todo obejeto tem caracteristicas e realiza funcionalidades.
# Eles tem atributos e metodos...