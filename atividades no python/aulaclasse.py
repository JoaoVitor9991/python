class  Vendedor():
    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas

#self -  variavel global,se chamar fora da funcao ela ira funcionar
vendedor1 =  Vendedor('Ederson', 1000)
print(vendedor1.nome)