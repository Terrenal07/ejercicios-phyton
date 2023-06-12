from geometrica import Geometrica

class Triangulo(Geometrica):
    def __init__(self, base=None, altura=None):
        self.base = base
        self.altura = altura

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def perimetro(self):
        return self.base * 3

    def area(self):
        return (self.base * self.altura) / 2

    def soy(self):
        return 'triangulo'
