# Professor Thago Belan / Logica_programação
# Este codigo deve retornar quem ganhou a eleição, total de votos, retornasr uma mensagem caso haja impate.

Back_end = 0
Front_end = 0
Brancos = 0
Nulos = 0
Total_de_votos  = 0


print("Bem vindo a eleição Escola Vida Nova\n")
print("Olá. Tudo bem? Meu nome é Paloma Adria e eu vou conduzir a votação  hoje.\n")
print("\nTecle enter para começar:\n")


while True:
    encerrar = str(input("Para encerrar a votação digite fim:\n"))
    if encerrar == "fim":
        break

    nome = str(input("Qual seu nome?\n"))
    idade = int(input("Qual a sua idade?\n"))
    if idade :
        Total_de_votos + 1
    print("Nosso opções são:\n")

    print(
        
        """     Minhas opções de voto:        
        \nOpções.................................Votos
        \n n° 1-)Back_end........................... (b)
        \n n° 2-)Front_end.......................... (f)
        \n n° 3-)Brancos............................. (sed)
        \n n° 4-)Nulos............................... (n)
        """)

    voto = str(input("Qual sua escolha de conteudo?"))


    if voto == "b": 
        Back_end = Back_end + 1
        print("Você vê o copo meio vazio.") 
    
    if voto == "f":
        Front_end = Front_end + 1
        print("Você  vê o copo meio cheio.")

    if voto == "sed":
        Brancos = Brancos  + 1
        print("Você sabe que alguém vai ter que lavar o copo.")
          
    if voto ==  "n":
        Nulos = Nulos  + 1
        print("Acho que você não tem um copo.")

    
    print(Total_de_votos)


                    