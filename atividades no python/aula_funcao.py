##a funcao so ira executar ao chamar ela
# def hello ():
#     print('Ola!')
# hello()

##parametro(variavel)
# def hello(nome):
#     print('Ola',nome)
# hello ('Ederson')


# def hello(nome):
#     print('Seja bem-vindo,',nome)
# n = input('Digite seu nome: ')
# hello(n)


# def hello(nome,idade):
#     print('Ola!',nome,'\nSua idade é',idade)
# a = input('Digite seu nome:')
# b = input('Digite sua idade:')
# hello(a,b)

##funcao saida
# def calcular_pag(qnd_horas,valor_hora):
#     horas = float(qnd_horas)
#     taxa = float(valor_hora)
#     if horas <=40:
#         salario = horas*taxa
#     else:
#         h_excd = horas-40        
#         salario= 40*taxa+(h_excd *(1.5*taxa))
#     print(salario)
# qnd_horas = float(input('Digite as horas:'))
# valor_hora = float(input('Digite a taxa:'))
# calcular_pag(qnd_horas,valor_hora)

##return(devolver o resultado)
# def soma(x,y):
#     result = x+y
#     return result
# a = int(input('Primeiro numero: '))
# b = int(input('Segundo numero: '))
# res = soma(a,b)
# print('resultado:',res)

##return com str
# def inverte(nome,sobrenome):
#     nomeinverso = sobrenome+","+nome
#     return nomeinverso
# nome = input('Nome:')
# sobrenome = input('Sobrenome:')
# invertido = inverte(nome,sobrenome)
# print('Ola', invertido)

##return com booleano
# def par(x):
#     if (x%2)==0:
#         return True
#     else:
#         return False
# while True:
#     num = int(input('Insira um numero: '))
#     if par(num):
#         print("é par")
#     else:
#         print('é impar')

##return varios valores
# def cadastro():
#     name = input('Qual o seu nome:')
#     age = input('Qual sua idade:')
#     return name,age
# print('iniciando cadastro...')
# nome,idade = cadastro()
# print('cadastro realizado com sucesso')
# print('Seu nome é',nome,'e sua idade é',idade)