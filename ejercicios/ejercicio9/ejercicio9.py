import os

def ejercicio1():
    fac = {}
    buc = False
    buc2 = False
    pag = 0
    pen = 0
    val = ''
    while not buc:
        eli = False
        buc2 = False
        men = input('Seleccione una opción:\n(1) Añadir factura\n(2) Pagar factura\n(3) Cerrar programa\n')
        if men == '1':  # Añadir factura
            num = input("Introduce el número de factura: ")
            if num in fac:
                print("Esta factura ya existe")
                val = input('¿modificar factura (Y)?')
                if val == 'Y':
                    eli = True
                else:
                    buc2 = True
            while not buc2:
                try:
                    pre = float(input('Indica el valor de la factura: '))
                    buc2 = True
                    if eli:
                        valor = fac[num]
                        pen -= valor
                    pen += pre
                    fac[num] = pre
                    print(f'Factura con id {num}, con valor {pre}, guardada')
                except ValueError:
                    print('Entrada no válida')
        elif men == '2':  # Pagar factura
            while not buc2:
                num = input('Introduce el número de factura: ')
                if num in fac:
                    print(f"Factura {num}, con valor {fac[num]}, pagada")
                    pic = float(fac.pop(num))
                    pag += pic
                    pen -= pic
                    buc2 = True
                else:
                    print('Número de factura incorrecto')
                    val = input('¿Volver al menú (Y)?')
                    if val != 'Y':
                        buc2 = True
        elif men == '3':  # Cerrar programa
            buc = True
        print(' - Pagado:    ', round(pag, 2))
        print(' - Pendiente: ', round(pen, 2))
if __name__ == "__main__":
    os.system('cls')
    ejercicio1()
