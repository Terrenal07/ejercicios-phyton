import os
import random

from circulo import Circulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from triangulo import Triangulo
def ejemplo1():
    cir = Circulo(5.1)
    cua = Cuadrado(3.1)
    rec = Rectangulo(2.2, 5.1)
    tri = Triangulo(3.1, 4.2)

    dg = [cir, cua, rec, tri]

    for i in dg:
        if isinstance(i, Circulo):
            print(f'figura: {i.soy()}\n       radio: {round(i.radio,2)}\n       area: {round(i.area(),2)}\n        perimetro: {round(i.perimetro(),2)},')
        if isinstance(i, Cuadrado):
            print(f'figura:{i.soy()}\n        lado: {round(i.lado,2)}\n        area: {round(i.area(),2)}\n        perimetro:{round(i.perimetro(),2)},')
        if isinstance(i, Rectangulo):
            print(f'figura:{i.soy()}\n        base: {round(i.base,2)}\n        altura: {round(i.altura),2}\n        area: {round(i.area(),2)}\n        perimetro:{round(i.perimetro(),2)},')
        if isinstance(i, Triangulo):
            print(f'figura:{i.soy()}\n        base: {round(i.base,2)}\n        altura: {round(i.altura,2)}\n        area: {round(i.area(),2)}\n        perimetro:{round(i.perimetro(),2)},')

def ejemplo2():
    fg = []
    rndfig = [Circulo, Cuadrado, Rectangulo, Triangulo]
    ffg = [0,0,0,0,0]
    
    for i in range(100):
        e = random.randint(0, 3)
        
        if e == 0:
            fg.append(Circulo(round(random.uniform(0, 100), 2)))
        elif e == 1:
            fg.append(Cuadrado(round(random.uniform(0, 100), 2)))
        elif e == 2:
            fg.append(Rectangulo(round(random.uniform(0, 100), 2), round(random.uniform(0, 100), 2)))
        elif e == 3:
            fg.append(Triangulo(round(random.uniform(0, 100), 2), round(random.uniform(0, 100), 2)))
    
    for i in fg:
        if i.soy() == 'circulo':
            ffg[0] += 1
        if i.soy() == 'cuadrado':
            ffg[1] += 1
        if i.soy() == 'rectangulo':
            ffg[2] += 1
        if i.soy() == 'triangulo':
            ffg[3] += 1
        ffg[4]+=1
            
    print(f'total figuras:          -{ffg[4]}\nNúmero de círculos:     -{ffg[0]}\nNúmero de cuadrados:    -{ffg[1]}\nNúmero de rectángulos:  -{ffg[2]}\nNúmero de triángulos:   -{ffg[3]}')
 
if __name__ == "__main__":
    os.system('cls')
    ejemplo2()
