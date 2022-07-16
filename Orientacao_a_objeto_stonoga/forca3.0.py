# Jogo da forca professor Rafael Stonoga
# Jogando forca usando uma estrutura de dados


import random

# Lista de palavras disponível na forca

palavras = ["amora",  "banana",  "caju",  "damasco", "embaúba",  "figo", "graviola", "hilocéreo",  "ingá", 
"jaca", "kiwi", "laranja",  "manga",  "noz",  "oiti", "pitaia",  "quina",  "romã", "sapucaia", "tangerina",
 "uva", "vergamota",  "wampi",  "xixá",  "yuzu",  "zimbro","anta",  "baleia",  "cachorro",  "dromedario",  "elefoa",  "flamingo",  "gaivota",  "hipopotamo",  "iguana",  
"jiboia",  "kookaburra", "leopardo",  "morça", "narval", "orangotango", "pantera", "quati", "rouxinol", "salamandra",  "tarantula",
 "ursa", "veado",  "wallaby", "xaréu",  "yak",  "zorrilho",
"amígdala",  "brônquios",  "cérebro",  "diafragma",  "epidídimo", "faringe",  "gengivas", "hipotálamo",  "íris",  
"jejuno", "linfonodo", "laringofaringe",  "mandíbula", "nefrónio",  "orofaringe",  "panturrilha", "quiasma", "retinas",  "sacro", "tonsila",
  "úvea",  "ventrículos", "vesícula", "véniculas",  "veia", "variz"]


palavra = random.choice(palavras)

print("bem vindo ao jogo da forca!\n")
print("O objetivo deste jogo é o de adivinhar qual a palavra que está oculta. Você terá seis tentativas, e na setima (terá uma ultima chance)  se errar será enforcado\n")
print("Nesta versão de forca você poderá se divertir. A palavra será escolhida randomicamente. pode variar entre: frutas (fácil), animais (médio), partes do corpo humano (difícil)\n")
print("Boa sorte!!!!!")



tentativas = 0

chances = 5
chance_extra = 1
letras_escolhidas = []
maquiagem = ["_"] * len(palavra)
print(maquiagem)

while tentativas < chances and ''.join(maquiagem) != palavra :
    letra = input ("\nDigite sua letra por favor:\n")
    while letra in letras_escolhidas :
        print("\n\nVocê tem perca de memória recente? Você já escolheu essa letra")
        letra = input("Fala outra letra ai ramelão")
    letras_escolhidas.append(letra)

    if letra in palavra:
        print("\n\nVocê quer um: playstation,playstation,playstation!!!!!!")
        for index in range(len(palavra)) :
            if letra == palavra[index] :
               maquiagem[index] = letra
    else:
        print("\n\nMas ganhou um: jogo da vida")
        tentativas = tentativas + 1

    print("\nVocê já utilizou", tentativas, "tentativas equivocadas e ainda tem",
     chances - tentativas, "tentativas" )

    print("\nSua palavra se encontra desta maneira :")
    print(maquiagem)

    print("\nVocê já tentou as seguintes letras:\n")
    for item in letras_escolhidas : 
        print(item, end=" ")
    

if tentativas == chances :
    print("\nPuxa, não foi dessa vez...") 
else:
    print("\nAeeeeeeeeeeee!!!!!!!!!!!!")