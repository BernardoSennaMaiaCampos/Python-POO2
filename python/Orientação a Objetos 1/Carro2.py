class Carros():
    def __init__(self, modelo, preco, cor, ano):
        self.modelo=modelo
        self.preco=preco
        self.cor=cor
        self.ano=ano
meucarro= Carros('Honda','100k', 'Prata', 2015)
print(meucarro.modelo)
print(meucarro.preco)
print(meucarro.cor)
print(meucarro.ano)