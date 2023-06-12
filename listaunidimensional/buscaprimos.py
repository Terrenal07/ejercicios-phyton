import os
import re

os.system('cls')
primos = []
i = 2
patron = "[0-9]+"
while True:
    cnt = input('Ingrese cantidad de primos a buscar: ')
    os.system('cls')
    if re.fullmatch(patron, cnt):
        cnt = int(cnt)
        while len(primos) < cnt:
            no = False
            for e in range(i - 1, 1, -1):
                if e<i/2:
                    break
                if i % e == 0:
                    no = True
                    break
            if no==False:
                primos.append(i)
                print(primos[-1],end=(","))
            i += 1
        break
    else:
        print('Input no válido, introduzca solo un número entero')