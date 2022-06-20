# Preencher o envelope para o envio de sua correspondencia pode ser complicado hoje em dia.
# Nossa geração domina as máquinas mas não preenche um envelope corretamente
# Se você é daqueles que também tem dificuldade nessa hora esse codigo te ajuda!

# primeiro passo

# Informações:


nome = input("Digite seu nome completo por favor: ").capitalize()
logradouro = input("\nDigite seu logradoro: ").capitalize()
numero = int(input("Digite o número da sua residência: "))
complemento = input("Digite seu complemento se houver: ").capitalize()
cep = input("Digite seu cep 'apenas numeros': ")
bairro = input("Digite seu bairro: ").capitalize()
cidade = input("Digite sua cidade: ").capitalize()
estado = input("Digite seu estado: ")

if len(cep) < 8:
    cep = cep.zfill
cep = "{}-{}".format(cep[:5], cep[5:8])
# Segundo passo

# Imprimir: 
print(nome)
print("{}, N°{}, {}".format(logradouro, numero, complemento))

print(bairro)
print("{}, {} - {}".format(cep, cidade, estado))