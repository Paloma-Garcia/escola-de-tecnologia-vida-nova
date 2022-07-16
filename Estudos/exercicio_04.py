#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

# Modo 1 declarando variaveis:
numero = int(input("Olá. Digite um número:\n"))
antecessor = numero - 1
sucessor = numero + 1

print("Analisando  o numero {}, seu antecessor é: {}, e seu sucessor é : {}".format(numero, antecessor, sucessor))

# Modo 2 economizando memoria:
# numero = int(input("Olá. Digite um número:\n"))
# print("Analisando  o numero {}, seu antecessor é: {}, e seu sucessor é : {}".format(numero, (numero-1), (numero+1)))