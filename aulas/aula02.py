#String - Conjunto de caracteres

texto = "Essa string é apenas um texto"

#1 Método de acesso -> . (Ponto)

#a Format
nome = input ("Qual é o seu nome?")
texto = "Olá {}, seja bem vinda".format(nome)
print (texto)

#b Split
dividindotexto = texto.split ('a')
print (dividindotexto)

#c Maiuscula e Minuscula
caixaBaixa = texto.lower()
print (caixaBaixa)

caixaAlta = texto.upper ()
print (caixaAlta)



#2 Indexacao de String

print (texto [4])