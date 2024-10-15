r1 = str(input('Telefonou para a vitima?')).capitalize()
r2 = str(input('Esteve no local do crime?')).capitalize()
r3 = str(input('Mora perto da vitima?')).capitalize()
r4 = str(input('Devia para a vitima?')).capitalize()
r5 = str(input('Já trabalhou com a vitima?')).capitalize()

cont = 0

if r1 == "Sim":
    cont = cont + 1
if r2 == "Sim":
    cont = cont + 1
if r3 == "Sim":
    cont = cont + 1
if r4 == "Sim":
    cont = cont + 1
if r5 == "Sim":
    cont = cont + 1

if cont == 2:
    print('Suspeita')
elif cont ==4 or cont == 3:
    print('Cumplise')
elif cont == 5:
    print('Assassino')
else:
    print('Inocente')