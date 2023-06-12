from typing import Any
import math

class Circulo:

    def __init__(self,r):
        self.__radio=r

    def get_radio(self,):
        return self.__radio
    
    def set_radio(self,r):
        self.__radio=r

    def __str__(self):### phyton recurre a esto cunado se pide: print(objeto circulo)
        return self.__radio
    
    def perimetro(self):
        return round(2 * math.pi * self.__radio,2)

    def area(self):
        return round(math.pi * self.__radio**2,2)
    
    def cabecera():
        print('%5s %10s %10s %10s'%('id','radio','perimetro','area'))
        print('%5s %10s %10s %10s'%('--','-----','---------','----'))

    def cuerpo(self,i):
        print('%5d %10.2f %10.2f %10.2f'%(i,self.get_radio(),self.perimetro(),self.area()))