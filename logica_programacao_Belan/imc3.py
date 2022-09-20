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

idade = 0
jovens_total = 0
jovens_masculinos = 0
jovens_femininos = 0
jovens_pd = 0
adultos_masculinos = 0
adultos_femininos = 0
adultos_pd = 0
adultos_total = 0
experts_total = 0
experts_masculinos = 0
experts_femininos = 0
experts_pd = 0
Quantidade_entrevistados_masculinos = 0
Quantidade_entrevistados_femininos = 0
Quantidade_entrevistados_prefiro_nao_declarar = 0
Total_entrevistados = 0
media_idade = 0
media_peso = 0
media_altura = 0
Total_entrevistados
media_jovens= 0
media_adultos = 0
media_experts = 0
repete = 0
print("Olá. Tudo bem? Meu nome é Paloma Adria, e eu irei avaliar você.")
print("\nPara começar vou precisar que você me passe algumas informações:")

idade =int(input("Quantos anos você tem?")) 
while idade < 18 :
     print("Você ainda não atingiu a maior idade e não pode participar da entrevista.")
if idade >=18:
    print("Que bacana!\n")
    print("Vamos continuar.") 
    nome = input("Qual seu nome?")
    gênero = input("Qual seu gênero? Sendo que : masculino (m), feminino (f), prefiro não declarar (pd).\n ")
    print("Antes de continuar vamos a alguma dicas\n ")
    print("Para facilitar nossa comunicação para informações como peso/altura digite ponto para separar o kg das gramas. E ponto para separar metro dos centimetros. Obrigada!")
    peso = float(input("Qual seu peso?"))
    altura = float(input("Qual sua altura?"))
    imc = (peso / (altura*altura))*1000
    print("Seu IMC é: {:00.2f}".format(imc))
    if (imc < 18.5): 
        print("Seu IMC esta abaixo do indicado")
    elif (imc> 24.9):
        print("Seu IMC está acima do indicado")
    else:
        print("Seu IMC está no indicado")

if idade == 18 and  idade <= 32:
    jovens_total = jovens_total + 1
    media_jovens = jovens_total / jovens_total
    if gênero == "m" : 
        jovens_masculinos = jovens_masculinos + 1, Quantidade_entrevistados_masculinos + 1

    if gênero == "f" :
        jovens_femininos = jovens_femininos + 1, Quantidade_entrevistados_femininos + 1

    if gênero == "pd" :
        jovens_pd = jovens_pd + 1, Quantidade_entrevistados_prefiro_nao_declarar + 1

if idade == 33 and  idade <= 61:
    adultos_total = adultos_total + 1
    media_adultos = adultos_total / adultos_total
    if gênero == "m" : 
        adultos_masculinos = adultos_masculinos + 1, Quantidade_entrevistados_masculinos + 1

    if gênero == "f" :
        adultos_femininos = adultos_femininos + 1, Quantidade_entrevistados_femininos + 1

    if gênero == "pd" :
        adultos_pd = adultos_pd + 1, Quantidade_entrevistados_prefiro_nao_declarar + 1

else:
        experts_total = experts_total + 1
        media_experts = experts_total / experts_total 
        if gênero == "m" : 
            experts_masculinos = experts_masculinos + 1, Quantidade_entrevistados_masculinos + 1

        if gênero == "f" :
            experts_femininos = experts_femininos + 1, Quantidade_entrevistados_femininos + 1

        if gênero == "pd" :
            experts_pd = experts_pd + 1, Quantidade_entrevistados_prefiro_nao_declarar + 1
		 	
repete = input("Obrigada pelas informações para terminarmos digite 1")
#if repete == 1 :
print(media_experts)



