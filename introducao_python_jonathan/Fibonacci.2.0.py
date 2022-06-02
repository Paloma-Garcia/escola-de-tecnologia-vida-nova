
# Exercício Fibonacci 
# While
# Começando por 0 e 1, cada termo subsequente corresponde a soma dos dois anteriores.
# Esse codigo recebe um numero inteiro que representa a quantidade de numeros Fibonacci que você quer calcular, 
# A partir disso é possivel notar um loop que calcula todos os numeros que você deseja.
# Vamos lá?


numero = int(input("Olá qual a quantidade de numeros que você deseja hoje?\n Caso você digite o 0 teremos de nos despedir\n"))

x = 0
y = 1
z = x + y

while (y < numero):
 print(x)
z = y + x
x = y
y = z