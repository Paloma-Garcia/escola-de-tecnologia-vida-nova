# Exercício 1:
# Implemente uma partida de par ou ímpar:
# Pergunte ao usuário se ele prefere par ou ímpar
# Valide a entrada dele (enquanto o usuário não digitar corretamente par ou ímpar ele deve continuar perguntando) 
# Solicite ao usuário um número inteiro
# Valide a entrada do usuário (verifique se não contém letras ou caracteres não-alfanuméricos)
# Sorteie um número entre 0 e 5 para servir de número para o computador
# Verifique o resultado e imprima na tela a mensagem correspondente
# Por fim, transforme isso numa função que retorna 0 caso o jogador ganhe e 1 caso o computador ganhe

from random import randint
v = 0
while True:
    competidor = int(input("Escolha um numero: "))
    if competidor == str:
        print("Você deve digitar apenas numero de um a dez para jogar")
    computador = randint (0,10)
    total = competidor + computador 
    tipo = ""
    while tipo not in "PpIi":
        tipo = str(input("Você quer par ou impar? [P/I]")).strip().upper() [0] 
    print(f"Você jogou {competidor} e o computador {computador }. Total de {total}", end= "")
    print("Deu par" if total % 2 == 0 else "Deu impar")
    if tipo == "P":
        if  total % 2 == 0:
             print ("Você venceu!!!")
             v += 1
        else:
             print("Você perdeu!!!")
             break
    elif tipo == "I":
         if total % 2 == 1 :
             print ("Você venceu!!!")
             v += 1
         else:
              print("Você perdeu!!!")
              break
    print("Vamos jogar novamente....")
print(f"GAME OVER! Você venceu {v} vezes.")
