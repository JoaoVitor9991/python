total = 0
while True:
    print('--------------------------')
    produto = str(input("Nome do produto (ou 0 para encerrar): "))
    preco = float(input('Valor do produto(ou 0 para encerrar): '))
    total += preco
    if produto == "0" and preco == 0:
        print(f'Valor total da compra: R${total:.2f}')
        pago = float(input('Pago: R$'))
        if pago < total:
            print('valor insuficiente!')
        else:
            troco =  pago - total 
            print(f'troco: {troco:.2f}')