
import math
from geometrica import Geometrica

class Cuadrado(Geometrica):

    def __init__(self,lado=None):
        self.lado=lado

    def set_base(self,base):
        self.base=base

    def get_base(self,base):
        return base

    def perimetro (self):
        return 4*self.lado
    
    def area(self):
        return math.pow(self.lado,2)
    
    def soy(self):
        return 'cuadrado'