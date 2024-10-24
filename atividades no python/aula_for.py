#ira pegar cada nome por vez
nome = ['PEdro' 'Joao' 'Leticia']
for n in nome:
    print(n)

#ira pegar cada letra por vez
nome ="Ederson"
for n in  nome:
    print(n)

#parar o loop antes de percorrer todos os itens(print Joao)
nome = ['Pedro' 'Joao' 'Leticia']
for n in nome:
    print(n)
    if n == 'Joao':
        break

#parar o loop antes de percorrer todos os itens(nao print Joao)
nome = ['Pedro' 'Joao' 'Leticia']
for n in nome:
    if n == 'Joao':
        break
    print(n)

#pode parar a iteraçao atual do loop e contiuara com a proxima
nome = ['Pedro' 'Joao' 'Leticia']
for n in nome:
    if n == 'Joao':
        continue
    print(n)

#quantidade de vezes
for x in range(6):
    print(x)

#entre o valor de 2 e 6(sem contar o 6)
for x in range(2,6):
    print(x)

#incrementa o valor escrito(inicio/fim/incremento)
for x in range(2,10,2):
    print(x)

#loop aninhado é um loop dentro de um loop(o segundo loop ira se executado ate o fim,dps voltara ao inicio e zera novamente)
for i in range(5):
    for j in range(6):
        print(i,j)

nome = ['Pedro' 'Joao' 'Leticia']
for n in nomes:
    print(n)