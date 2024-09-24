nome = str(input('Produto= '))
quant = int(input('Quantidade= '))
valor = float(input('Valor= '))
porc = int(input('Percentrual de desconto= '))

desc = porc/100

total1 = (valor * quant) 
total2 = total1 * desc
total3 = total1 - total2

print(f'O total a pagar do produto {nome} é de R${total3}')