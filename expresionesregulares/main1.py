import os
import re
os.system('cls')

# Evaluar entrada de solo números enteros

patron = "[0-9]+"  # Patrón para buscar una o más ocurrencias de dígitos numéricos

while True:
    numero = input('Ingrese un número: ')
    correcto = re.fullmatch(patron, numero)  # Comprobar si el número coincide con el patrón

    if correcto:
        break  # Si el número es válido, salir del bucle

print('Número: ', numero)
