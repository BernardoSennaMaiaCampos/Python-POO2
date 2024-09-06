class Retangulo:
    def __init__(self, l, a):
        self.largura = l
        self.altura = a
        
    def perimetro(self):
        return (self.altura+self.largura)*2
    def area(self):
        return (self.altura*self.largura)
    def __str__(self):
        return 'perimetro = ' + str(self.perimetro()) + ' e area = ' + str(self.area())
# main
ret1 = Retangulo(4,3)
print(ret1)