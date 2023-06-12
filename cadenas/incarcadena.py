import os
#se indica cadena 1 y cadena 2, si la cadena 2 empieza con cadena 1, indicar si, en caso 
def ejemplo1():
    cadena1 = 'hola'
    cadena2 = input('ingrese cadena: ')
    os.system('cls')
    ver = 'si'
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            ver = 'no'
            break
    print(ver)

#simplifcado
def ejemplo2():
    cadena1 = 'hola'
    cadena2 = input('Ingrese cadena: ')
    aux = cadena2[0:len(cadena1)]
    os.system('cls')
    if cadena1 == aux:
        print('si')
    else:
        print('no')

#se indica cadena 1 y cadena 2, si la cadena 2 empieza con cadena 1, indicar si, en caso (se ignoran minusculas y mayusculas)
def ejemplo3():
    cadena1 = 'hola'
    cadena2 = input('ingrese cadena: ')
    os.system('cls')
    cadena1=cadena1.lower()
    cadena2=cadena2.lower()
    ver = 'si'
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            ver = 'no'
            break
    print(ver)

#simplifcado
import os

def ejemplo4():
    cadena1 = 'hola'
    cadena2 = input('Ingrese cadena: ')
    aux = cadena2[0:len(cadena1)]
    os.system('cls')
    if cadena1.lower() == aux.lower():
        print('si')
    else:
        print('no')

if __name__ == "__main__":
    ejemplo4()


#principal
if __name__ == "__main__":
    os.system('cls')
    ejemplo4()
