import os
from circulo import Circulo

if __name__ =="__main__":

    radio=float(input('ingrese radio'))
    print("perimetro: ", Circulo.perimetro(radio))
    print("Area: ", Circulo.area(radio))