from geometrica import Geometrica

class Rectangulo(Geometrica):
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
        return 2 * self.base + 2 * self.altura

    def area(self):
        return self.base * self.altura

    def soy(self):
        return 'rectangulo'
