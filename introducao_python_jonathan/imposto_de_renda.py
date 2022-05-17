#calculo da porcentagem do imposto de renda (IR)

# Tabela de dados para base 

# Até 1.903,98 / ------
# De 1.903,99  até 2.826,65 / 7,5% 
# De 2.826,66 até 3.371,05 / 15%
# De 3.751,06 até 4.664,68 /22,5%
# Acima de 4.664,69 / 27,5%


nome = str(input("Digite seu nome completo : "))

cpf = int(input("Digite seu cpf apenas numeros : "))

valorrendabruta = float(input("Digite valor da renda bruta : "))


if valorrendabruta <= 1903.98:
    imposto = 0
    print('=' * 50)
    print("Você não precisa declarar imposto de renda pois não atingiu valor minimo para essa ação.")

elif valorrendabruta > 1903.99 and valorrendabruta < 2826.65:
    imposto = 7.5

elif valorrendabruta > 2826.66 and valorrendabruta < 3371.05:
    imposto = 15.0

elif valorrendabruta > 3371.06 and valorrendabruta < 4664.68:
    imposto = 22.5

elif valorrendabruta > 4664.69:
    imposto = 27.5 

valorrendaliquida = valorrendabruta - (valorrendabruta * (imposto / 100))

print('=' * 50)
print("sr'a' {} \nCPF: {} \nRenda bruta de: {} \nValor liquido {:.2f}".format(nome, cpf, valorrendabruta, valorrendaliquida))
print('=' * 50)