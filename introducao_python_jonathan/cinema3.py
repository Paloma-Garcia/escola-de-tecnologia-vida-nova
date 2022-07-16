# Exercício cinema 
# professor Jonathan André/Introdução a Python
# O objetivo dessa atividade é desenvolver um algoritmo (código) que receba (input) o número de assentos que a sala possui,
# Ápós isso, exiba na tela todos os lugares da sala, e para cada reserva realizada, 
# exibe novamente os lugares marcando aqueles que estão ocupados (já foram reservados). 
# O código deve permitir que seja digitado o lugar ao qual se deseja reservar...
# É obrigatório o uso de vetores para o desenvolvimento do exercício...

import os

quantidade_lugares  =  int(input( "Escolha a quantidade de lugares: "))
lugares  = [ '-' ] * quantidade_lugares

coluna_dict  = {
    'a' : 1 ,
    'b' : 2 ,
    'c' : 3 ,
    'd' : 4 ,
    'e' : 5 ,
    'f' : 6 ,
    'g' : 7 ,
    'h' : 8 ,
    'i' : 9 ,
    'j' : 10 ,
}

y  =  0
while (y < len (lugares)):

    letras_coluna  = print ("\n A,B,C,D,E,F,G,H,I,J")
    numero_da_fileira  = 1
    
    for x in range(1, quantidade_lugares + 1 ): 
        print(lugares[x - 1], end  = " " )
        if ( x % 10  ==  0 ) or ( x  ==  quantidade_lugares):
            print(numero_da_fileira ,"\n")
            numero_da_fileira += 1

    fileira =  int(input("\n Digite a fileira desejada:"))
    coluna  =  input( "Digite a coluna desejada: ")
        
    os.system("cls")
    lugar_No_Cinema  = ( fileira - 1 ) * 10 + ( coluna_dict [ coluna ])

    if (lugares [lugar_No_Cinema - 1 ] == 'x' ): 
        y -= 1
        os.system("cls")
        print ( 'A CADEIRA ESTÁ OCUPADA! ESCOLHA OUTRO LUGAR: ' )
    y += 1

    lugares [lugar_No_Cinema - 1 ] =  "x"
print("\t -- NÃO EXISTEM MAIS LUGARES DISPONIVEIS -- \n PREPARE-SE O FILME JA VAI COMEÇAR! \n")
    