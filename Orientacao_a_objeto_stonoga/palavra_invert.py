# Neste exercício o usuario deve digitar uma palavra e o código devolve-la invertida.
# Professor Rafael Stonoga / Orientação a Objeto

print("Olá!") 

palavra = input("Qual palavra deseja inverter hoje?")

palavra_invertida = ''


for letra in palavra:
    palavra_invertida = letra + palavra_invertida 

    print(palavra_invertida)
