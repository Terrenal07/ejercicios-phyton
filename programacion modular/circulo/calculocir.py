import os
import util

if __name__ == "__main__":
    os.system('cls')
    rad = float(input('Ingrese el radio: '))
    perimetro = util.getPerimetro(rad)
    area = util.getArea(rad)
    print("Perímetro:", util.redondear2(perimetro))
    print("Área:", util.redondear2(area))
