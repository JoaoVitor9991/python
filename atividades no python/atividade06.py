n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

media = (n1 + n2 + n3 + n4 )/4

if media <= 4:
    print("Conceito:E")
    print('Status:Reprovado')
    print('Média:',media)
elif media <= 5.9:
    print('Conceito:D')
    print('Status:Reprovado')
    print('Média:',media)
elif media <= 7.5:
    print('Conceito:C')
    print('Status:Aprovado')
    print('Média:',media)
elif media <= 9:
    print('Conceito:B')
    print('Status:Aprovado')
    print('Média:',media)
elif media <= 10.0:
    print('Conceito:A')
    print('Status:Aprovado')
    print('Média:',media)