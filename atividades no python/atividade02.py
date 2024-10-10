senha = int(input('Informe a senha: '))
saldo = 0
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
if senha == 123:
    print('1-Extrato')
    print('2-Deposito') 
    print('3-Saque') 
    print('4-adm')
    print('5-Sair') 
    resp = int(input('Digite o que deseja: '))
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

    if resp == 1:
        print('Seu extratro é de:',saldo)
    elif resp == 2:
        depo = float(input('Digite o quanto quer depositar: '))
        print('Seu deposito é de: +',depo)
        saldo = depo + saldo
        print('seu saldo é de: ',saldo)
    elif resp == 3:
        saque = float(input('Digite o quanto quer sacar: '))
        print('Seu deposito é de: -',saque)
        saldo = saque - saldo
        print('seu saldo é de: ',saldo)
    elif resp == 4:
        print('1-Cadastro')
        print('2-Editar cadastro')
        resp = int(input('Digite o que deseja: '))
        if resp == 1:
            nome = str(input('Nome: '))
            cpf = int(input('CPF: '))
            fone = int(input('Telefone: '))
            sexo = str(input('Sexo: '))
        elif resp == 2:
            nome = print()
            cpf = print()
            fone = print()
            sexo = print()
    elif resp == 5:
        print('Encerrado.')
        print('seu saldo é de: ',saldo)
    else:
        print('Opção Inválida')
else:
    print('Senha Inválida')