
class clase1:

    def __init__(self,atributo=None):
        self.atributo = atributo

    def metodo1_1(self):
        print('metodo1_1',self.atributo)

class clase2:

    def metodo2_1(self):
        print('metodo2_1')


class clasehijo(clase1,clase2):

    def __init__(self,atributo=None):
        self.atributo=atributo