#manipulaçao de str
#empregada para obter o comprimento de uma sequência qualquer
#retorna o número de caracteres presentes na string.​
a = "Ederson"
print(len(a))
 
#transformar a primeira letra da primeira palavra em maiúscula
a = "ederson"
print(a.capitalize())

#transformar todo o texto em maiúsculo
a = "ederson"
print(a.upper())

#transformar todo o texto em minusculo
a = "EDERSON"
print(a.casefold())

#transformar todo o texto em minusculo
a = "EDERSON"
print(a.lower())

#Identificar se todo o texto está em minusculo
a ="EDERSON"
print(a.islower())
a ="ederson"
print(a.islower())

#Identificar se todo o texto está em maiúsculo
a = "EDERSON"
print(a.isupper())
a = "ederson"
print(a.isupper())

#Como verificar se uma string só possui números inteiros
a = "12345"
print(a.isdigit())
a = "12345abcd"
print(a.isdigit())

#trocar todas as ocorrências de uma substring por outra em uma string. ​
a = "Ederson Roberto"
print(a.replace("Roberto","Costa"))

#separa uma string usando sep como separador
a = "Ederson - Roberto - Costa"
print(a.split("-"))

#retorna onde a substring começa na string (“Primeira”)​

a = "A B C D E F G H"
print(a.find("F"))

#verifica se uma substring é parte de uma outra string
a = "Anne Primon Silva"
print("Primon" in a)

#retorna a frequência de ocorrência do parâmetro passado

a = "Anne Primon Silva"
print(a.count("n"))

#subtrings

s = "Anne Primon"
print(s[6])
s = "Anne Primon"
print(s[-6])

s = "Anne,Primon"
print(s[2:6])
#[ :5] [0: ]


