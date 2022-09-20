# Logica de programação/ professor Thiago Belan
# Exercício final (IMC)
# Vamos criar um sistema para categorizar as pessoas entrevistadas.Só armazenaremos pessoas com idade maior que 18 anos
# Só armazenaremos pessoas com idade maior que 18 anos
# Teremos 3 grupos:
# Jovens – pessoas de 18 a 32 anos, Adultos – pessoas de 33 a 61, Experts – pessoas de 61 acima 
# Considerando altura e peso do entrevistado você deve devolver se o entrevistado está com
# peso ok ou sobrepeso. Para isso você deve usar cálculo do IMC (divide-se o peso do paciente
# pela sua altura elevada ao quadrado). Caso o resultado esteja entre 18,5 e 24,9 você avisa o
# entrevistado que o peso dele está ok. Resultado acima = sobrepeso, resultado abaixo = abaixo do peso.

# Fase 2 - Ao final do registro de todos entrevistados, o programa deve apresentar: 
# Quantidade de entrevistados, Média de idade, Média de peso, Média de altura
# Essas médias por grupo criados e sexo.
# Você deve criar um controle para finalização de digitação.


print("Olá. Tudo bem? Meu nome é Paloma Adria e eu vou te entrevistar hoje.")
print("\nVamos começar?:")

entrevistados= []



while True:
    
    nome = str(input("Qual seu nome?"))
    idade = int(input("Qual a sua idade?"))
    gênero = str(input("Qual seu gênero? Sendo que : masculino (m), feminino (f), prefiro não declarar (pd).\n "))
    altura = float(input("Qual a sua altura ?"))
    peso = int(input("Qual seu peso?"))

    entrevistados.append ({
        "nome": nome,
        "idade" : idade,
        "gênero" : gênero,
        "altura" : altura,
        "peso" : peso

    })

    imc = peso / (altura*altura)

    print (imc)

    continuar = ""
    while "s" != continuar.upper() != "n":
        continuar = str(input("Deseja continuar as entrevistas? Digite s para sim e n para não. "))

    if continuar.upper() == "n" :
        break

print("Quantidade de entrevistados : {}".format(len(entrevistados)))


entrevistados_homens = []

if 

    jovens = idade > 18 and idade < 32 
    adultos = idade >= 33 and idade < 61
    experts = idade >= 62


    entrevistados_homens. append ({
        "jovens" : jovens,
        "adultos" : adultos,
        "experts" : experts,
})