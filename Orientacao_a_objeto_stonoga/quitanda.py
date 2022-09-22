# Orientação a objeto 
# Professor Rafael Stonoga
# Exercicio : Quitanda

# Enunciado do exercício:
# Joaquim tem duas paixões: vender frutas na feira e dar o troco certo para os seus clientes. Vamos ajudá-lo a automatizar o trabalho? 
# Suponha que Joaquim vende 3 tipos de fruta: laranja, melancia e morango. Suponha também que cada um possui um preço por unidade.

# Etapa 1:
# - Pergunte ao cliente que fruta ele gostaria 

# - Pergunte quantas unidades ele quer
# - Escreva na tela o preço total da compra
# (Desafio)
# - Repita o processo anterior quantas vezes o cliente quiser (Podes usar uma opção S/N para perguntar se ele quer comprar mais frutas)
# - Ao invés de mostrar apenas o preço total, mostre também quantas frutas de cada tipo o cliente pediu

# Etapa 2:
# - Pergunte ao cliente quanto dinheiro ele vai dar ao Joaquim (use números inteiros nesse momento) - Calcule o troco
# - Determine quantas notas de cada tipo Joaquim deve devolver de troco (considere nesse momento apenas notas de 1, 5 e 20 reais)

# (Desafio)
# - E se o cliente inserir um valor menor que o preço da compra?
#  - Troque o preço por unidade por um preço por kilo e permita o uso de valores com vírgula na pergunta do cliente
# - Permita o uso de moedas de 1, 5, 10 e 25 centavos no troco

# Se não for possível entregar o troco exato, imprima também uma mensagem informando quanto faltou.

# Fase 1

frutas_menu_dict = {
    "amora" : 25,
    "banana" : 14,
    "cereja" : 10,
    "goiaba" : 13,
    "laranja" : 7,
    "maça" : 15,
    "melancia" : 10,
    "morango" : 8,
    "pera" : 20,
    "limão" : 10
}

print("_Olá seja bem vindo a quitanda 'Vida Nova'\n\n_Meu nome é Paloma e hoje eu vou te atender.")
print("\n Já vou te encaminhar nosso menu de frutas.")
print("\nSegue abaixo nosso menu com as frutas que temos disponiveis hoje e os valores:")

fruta_menu = """

Frutas........................Valor

Amora........................... 25
Banana.......................... 14
Cereja.......................... 10
Goiaba.......................... 13
Laranja.......................... 7
Maça............................ 15
Melancia........................ 10
Morango.......................... 8
Pera............................ 20
limão............................10

Qual fruta você gostaria de comprar hoje?\n  Pra não confundirmos seu pedido escreve apenas uma fruta de cada vez. Obrigada \n: """
fruta = input(fruta_menu).lower()
preco = frutas_menu_dict[fruta]
print("O preço por kg esta no menu  {}" .format(preco))

quantidade = float(input("Quantas kg você gostaria? " ))

total = quantidade * preco
print("O total de sua compra é  R${}" .format(total))

dinheiro = int(input("Qual valor da nota utilizada para o  pagamento?\n Lembrete Falicite o troco : "))

def calcula_troco(total , dinheiro):
    troco = dinheiro - total
    print( "total: " , total)
    print("dinheiro: ", dinheiro)
    print( "Troco: " , troco)
    
calcula_troco(total, dinheiro)




