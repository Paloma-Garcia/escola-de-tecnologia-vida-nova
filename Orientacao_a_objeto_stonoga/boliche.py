# Boliche no terminal
# Professor Rafael Stonoga/ Orientação a Objeto

# Considere os 10 pinos de boliche organizados assim: 
#cada pino é uma letra 'I' / Cada pino corresponde a um numero.

# Para desenhar a pista considere que cada linha possui um tamanho de 7 espaços.
# A primeira linha, por exemplo, é composta pelos 4 pinos e pelos 3 espaços entre eles.

# Faça uma função que recebe uma lista de numeros correspondente aos pinos.
# Cada pino cujo número aparece n lista deve ser "derrubado", sendo trocado por um "_"
# ou por um espaço vazio. 
# (Desafio 1) Generalize o código para que considere N pinos, 
# sendo N um número de pinos que permita a montagem de um triângulo. (Ex: 1, 3, 6, 10, 15, 21…)

# (Desafio 2) Faça um código que sorteia aleatoriamente um conjunto de pinos a ser derrubado (Dica: biblioteca random). 
# Veja quantas tentativas você leva para fazer um strike! E se você tentasse fazer um spare, como ficaria sua lógica? 


def minha_pista(pinos):
    for pinos_bol in pinos:
        print(pinos_bol, end= '')
    print()
        
pista = [
    'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', 
    ' ', 'I', ' ', 'I', ' ', 'I', ' ', '\n',
    ' ', ' ', 'I', ' ', 'I', ' ', ' ','\n',
    ' ', ' ', ' ', 'I', ' ', ' ', ' '
]

localizacao_dos_pinos = {
    "1": 27,
    "2": 20,
    "3": 18,
    "4": 13,
    "5": 11,
    "6": 9,
    "7": 6,
    "8": 4,
    "9": 2,
    "10": 0,
}
#tradução de quem é quem pro codigo

#for pinos in localizacao_dos_pinos:
    #localizacao = localizacao_dos_pinos[pinos]
    #pista[localizacao] = pinos


minha_pista(pista)

tentativas = []

while True:
    valor = input("Digite o pino que quer derrubar:\n")
    if not valor:
        break
    if valor in tentativas:
        print("Pino já derrubado.")
        continue
    else:
        tentativas.append(valor)

    indice = localizacao_dos_pinos [valor]

    pista[indice] = " "

    if "I" in pista:
        minha_pista(pista)
    else:
        print("Parabéns você conseguiu derrubar todos os pinos.")
        break