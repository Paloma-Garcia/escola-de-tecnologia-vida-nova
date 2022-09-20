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

print("Olá. Tudo bem? Meu nome é Paloma Adria, e eu irei avaliar você.")
print("\nPara começar vou precisar que você me passe algumas informações:")

idade =int(input("Quantos anos você tem?")) 

class IMC():
        def imc():

            while True: 
                peso = float(input("Qual seu peso (kg)?:"))
                altura = float(input("Qual sua altura (m)?:"))
                imc = peso / (altura*altura)


                if imc < 18.5:
                    print("Seu imc esta abaixo do indicado")


                elif imc >= 18.5 and imc <= 24.9:
                    print("Seu imc esta no indicado")  


                elif imc >= 25.0 and imc <= 29.9:
                    print("Seu imc esta acima do indicado") 

                elif imc >= 30.0 and imc <= 39.9:
                    print("Seu imc esta muito acima do indicado")  
