class Retangulo:
    def __init__(self, l, a):
        self.largura = l
        self.altura = a
    
    def perimetro(self):
        return (self.altura+self.largura)*2
    def area(self):
        return (self.altura*self.largura)

#main
ret1 = Retangulo(4,3)
print(f'perimetro = {ret1.perimetro()} e area = {ret1.area()}')
