#manipulaçao de str, funçao len

a = "Ederson"
print(len(a))
 
#funçao capitalize

a = "ederson"
print(a.capitalize())

#funçao upper

a = "ederson"
print(a.upper())

#funçao casefold

a = "EDERSON"
print(a.casefold())

#fuçao lower

a = "EDERSON"
print(a.lower())

#funçao islower

a ="EDERSON"
print(a.islower())
a ="ederson"
print(a.islower())

#funçao isupper

a = "EDERSON"
print(a.isupper())
a = "ederson"
print(a.isupper())

#funçao isdigit

a = "12345"
print(a.isdigit())
a = "12345abcd"
print(a.isdigit())

#funçao replace

a = "Ederson Roberto"
print(a.replace("Roberto","Costa"))

#funçao split

a = "Ederson - Roberto - Costa"
print(a.split("-"))

#funçao fing

a = "A B C D E F G H"
print(a.find("F"))

#funçao in
a = "Anne Primon Silva"
print("Primon" in a)

#funçao count

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


