class Triangulo:
    def __init__(self, a, b, c):
        self.lado1 = a
        self.lado2 = b
        self.lado3 = c
        self.lados = [a,b,c]

    def FormaTriangulo(self):
        self.lados.sort()
        return self.lados[2]<=self.lados[0]+self.lados[1]

    def listaLados(self):
        return self.lados 