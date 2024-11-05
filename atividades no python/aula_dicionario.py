# #
# tradutor = {}
# tradutor['pineapple'] = 'Abacaxi'
# tradutor['apple'] ='Maça'
# tradutor['orange'] = 'Laranja'
# print(type(tradutor))
# print(tradutor)

# #
# tradutor1 = {}
# tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
# print(type(tradutor1))
# print(tradutor1)

# #
# tradutor1 = {}
# tradutor1 = {'pineapple': 'abacaxi','apple' : 'maça', 'orange' : 'laranja'}
# print(tradutor1['apple'])

# #
# tradutor1 = {}
# tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
# print(tradutor1)
# del (tradutor1 ['apple'])
# print(tradutor1)

# #
# tradutor1 = {}
# tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
# print(tradutor1)
# del (tradutor1 ['apple'])
# print(tradutor1)
# print(tradutor1.pop('banana', 'Fruta nao encontrada'))

# #
# tradutor1 = {}
# tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
# print(tradutor1)
# del (tradutor1 ['apple'])
# print(tradutor1)
# print(tradutor1.clear())

#pesquisa por chaves (antes dos ":")
# tradutor1 = {}
# tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
# print('pineapple' in tradutor1)

#pesquisar o conteudo (apos os ":")
# tradutor1 = {}
# tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
# print('laranja' in tradutor1.values())

#
tradutor1 = {}
tradutor1 = {'pineapple' : 'abacaxi', 'apple' : 'maça', 'orange' : 'laranja'}
print(tradutor1)
tradutor1 ['apple'] = 'goiaba'
print(tradutor1)

#
dados = {'crossfox': {'km': 3500, 'ano':2005},'DSS':{'km': 1700,'ano':2015},'Fusca':{'km': 130000, 'ano': 1979}}
print(dados)

#
dados = {'crossfox': {'km': 3500, 'ano':2005},'DSS':{'km': 1700,'ano':2015},'Fusca':{'km': 130000, 'ano': 1979}}
print(dados.get('Gol', 'veiculo nao encontrado'))