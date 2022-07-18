#Você deve criar um programa que:
# Conte quantas palavras há no arquivo
# Conte quantas vezes cada letra do alfabeto aparece no arquivo
# Conte quantas palavras começam com cada letra do alfabeto
# Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
# Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
# Identifique todas as palavras que são palíndromos e salve-as num arquivo separado
# Professor Rafael Stonoga/ Orientação a Objeto.


numero_de_palavras = 0
with open(r'palavras.txt', 'r') as arquivo_palavras:
    # Esta linha faz você ler o arquivo todo de uma vez, o que não é muito bom
    # O ideal é você ler linha a linha, para não precisar carregar tudo na memória de uma vez só
    palavras = arquivo_palavras.read()    
    letras_maiusculas = palavras.upper()  # Note que essa variável não é utilizada
    numero_de_palavras += len(palavras) # Aqui você está somando a quantidade de letras, e não a quantidade de palavras

# Uma alternativa seria isso:
numero_de_palavras = 0
with open('palavras.txt', 'r') as arquivo_palavras:
    for palavra in arquivo_palavras:
        numero_de_palavras += 1  # Para cada linha somamos 1 na variável de contagem. Ao final teremos o total de palavras

print("este é o numero de palavras q existe em nosso arquivo de palavras",numero_de_palavras)

# Isso funciona para a contagem de letras, mas de novo... não é muito eficiente.
# Percebe como o processo é igual para todas as letras? 
# Quando isso acontece normalmente podemos adaptar o código pra deixá-lo mais genérico
# Tente pensar em uma solução mais enxuta. É aqui que mora a grande sacada do exercício ;)
print("Este é o numero de letras usados no arquivo de palavras")
a = list(letras_maiusculas).count("a")
b = list(palavras).count("b")
c = list(palavras).count("c")
d = list(palavras).count("d")
e = list(palavras).count("e")
f = list(palavras).count("f")
g = list(palavras).count("g")
h = list(palavras).count("h")
i = list(palavras).count("i")
j = list(palavras).count("j")
k = list(palavras).count("k")
l = list(palavras).count("l")
m = list(palavras).count("m")
n = list(palavras).count("n")
o = list(palavras).count("o")
p = list(palavras).count("p")
q = list(palavras).count("q")
r = list(palavras).count("r")
s = list(palavras).count("s")
t = list(palavras).count("t")
u = list(palavras).count("u")
v = list(palavras).count("v")
w = list(palavras).count("w")
x = list(palavras).count("x")
y = list(palavras).count("y")
z = list(palavras).count("z")
print("a", a)
print("b", b)
print("c", c)
print("d", d)
print("e", e)
print("f", f)
print("g", g)
print("h", h)
print("i", i)
print("j", j)
print("k", k)
print("l", l)
print("m", m)
print("n", n)
print("o", o)
print("p", p)
print("q", q)
print("r", r)
print("s", s)
print("t", t)
print("u", u)
print("v", v)
print("w", w)
print("x", x)
print("y", y)
print("z", z)


lista_alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



