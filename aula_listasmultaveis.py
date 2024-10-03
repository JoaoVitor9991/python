#
frutas = ["banan", "Maça", "cereja"]
frutas[0] = "pera"
frutas[-1]= "laranja"
print(frutas)

#
uma_lista = ['a', 'b','c', 'd', 'e', 'f']
uma_lista[1:3] = ['x','y']
print(uma_lista)

#
uma_lista = ['a', 'b','c', 'd', 'e', 'f']
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3] = []
print(uma_lista)
print(len(uma_lista))

#
uma_lista = ['a', 'b','f']
uma_lista[1:1] = ['c','f']
print(uma_lista)
uma_lista[4:4] = ['e']
print(uma_lista)

#
a = ["uma","dois","tres"]
del a[1]
print(a)

lista = ['a', 'b','c', 'd', 'e', 'f']
del lista[1:5]
print(lista)

#operador . 
a = [81, 82,83]
a.append(5)
print(a)

#
a = [88, 81, 82, 83]
a.sort()
print(a)

#
a = [1,2,3,4,5,6,7,8,9]
print(a.index(4))

#
a = [88,81,82,83]
a.insert(1,100) #posicao,insira 100
print(a)

#
a = [88,81,82,83,88,85,88,86]
print(a)
print(a.count(88))

#
a = [88,81,82,83,88,85,88,86]
a.pop()
print(a)

a.pop(0)
print(a)

#
lista = [1,2]
lista.extend([3,4])
print(lista)