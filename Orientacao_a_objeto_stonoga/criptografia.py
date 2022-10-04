

palavra = input("Digite uma palavra: ").upper()

palavra_codificada = ""

letras_mapping = {
    "E": "3",
    "A": "4",
    "S": "5",
}
    

for letra in palavra:
    if letra == "A":
        palavra_codificada = palavra_codificada + "4"
    elif letra == "E":
        palavra_codificada = palavra_codificada + "3"
    elif letra == "S":
        palavra_codificada = palavra_codificada + "5"
    #if letra in letras_mapping:
        #letra_codificada = letras_mapping[letra]
        #palavra_codificada = palavra_codificada + letra_codificada
    else:
        palavra_codificada = palavra_codificada   + letra 
     

print(palavra_codificada)