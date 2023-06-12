import os
import re

def ejemplo1():#interseccion
    a={1,2,3,4}
    b={1,2,5,6}
    c=a&b
    print(a.intersection(b))
    print(c)

def ejemplo2():#union
    a={1,2,3,4}
    b={1,2,5,6}
    c=a|b
    print(a.union(b))
    print(c)

def ejemplo3():#diferencia
    a={1,2,3,4}
    b={1,2,5,6}
    c=a-b
    print(a.difference(b))
    print(c)

def ejemplo4():#inclusion
    a={1,2,}
    b={1,2,3,4}
    c=b>=a#c es cierto si dentro del conjunto "b" se encuentra el conjunto "a"
    print(c)

def ejemplo5():#exclusion
    a={1,2}
    b={3,4}
    c=a.isdisjoint(b) 
    print(c)


if __name__ == "__main__":
    os.system('cls')
    ejemplo5()
