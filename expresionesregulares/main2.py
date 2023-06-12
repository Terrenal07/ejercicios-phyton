import os
import re
os.system('cls')
patron = "[0-9]+"
while True:
    numero1 = input('Ingrese un número 1: ')
    numero2 = input('Ingrese un número 2: ')
    if re.fullmatch(patron, numero1) and re.fullmatch(patron, numero2):
        break
    else:
        os.system('cls')
        print('input no valido')

print('suma: ',int(numero1)+int(numero2))