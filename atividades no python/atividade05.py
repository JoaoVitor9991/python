salario = float(input('Digite o salario: '))

if salario <= 280:
    perc = 20
    reaj = salario + (salario * 0.20)
    dif = reaj - salario

elif salario <= 700:
    perc = 15
    reaj = salario + (salario * 0.15)
    dif = reaj - salario

elif salario <= 1500:
    perc = 10
    reaj =salario + (salario * 0.10)
    dif = reaj - salario

elif salario > 1500:
    perc = 5
    reaj = salario + (salario * 0.05)
    dif = reaj - salario

print('O salario antes dos reajustes é:',salario)
print('O percentual de aumento aplicado é:',perc)
print('O aumento foi de:',dif)
print('O salario atual é:',reaj)