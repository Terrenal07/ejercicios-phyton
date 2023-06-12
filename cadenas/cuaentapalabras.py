import os
import re

def ejemplo1():
    simbolos = r"[^\w\s]"
    cadena = input('Ingrese cadena: ')
    cadena = re.sub(simbolos, '', cadena.lower())
    os.system('cls')
    cads = cadena.split()
    acu = []
    acun = []
    for e in cads:
        if e not in acu:
            acu.append(e)
            acun.append(1)
        else:
            index = acu.index(e)
            acun[index] += 1
    acu=sorted(acu)
    for i in range(len(acu)):
        if acun[i] == 1:
            print('Palabra: %d vez - %s' % (acun[i],acu[i] ))
        else:
            print('Palabra: %d veces - %s' % (acun[i],acu[i]))

    print()
    print('Cantidad de palabras unicas:', len(acu))
    print()
if __name__ == "__main__":
    os.system('cls')
    ejemplo1()
