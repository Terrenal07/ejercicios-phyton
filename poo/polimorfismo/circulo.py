import math
from geometrica import Geometrica

class Circulo(Geometrica):
    def __init__(self, radio=None):
        self.radio = radio

    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * pow(self.radio, 2)

    def soy(self):
        return 'circulo'