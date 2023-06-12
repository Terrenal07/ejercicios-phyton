import os

from opcion import opcion1, opcion2, opcion3, opcion4, opcion5, opcion6
from util import preguntarid;

alumnos_1 = [
    {'idAlumno': 'A1', 'nombre': 'luis', 'edad': '23', 'casado': True},
    {'idAlumno': 'A2', 'nombre': 'miguel', 'edad': '21', 'casado': True},
    {'idAlumno': 'A3', 'nombre': 'carlos', 'edad': '20', 'casado': False},
    {'idAlumno': 'A4', 'nombre': 'maria', 'edad': '18', 'casado': True},
    {'idAlumno': 'A5', 'nombre': 'arturo', 'edad': '24', 'casado': True},
    {'idAlumno': 'A6', 'nombre': 'gerson', 'edad': '25', 'casado': False},
    {'idAlumno': 'A7', 'nombre': 'silvia', 'edad': '26', 'casado': True},
]

def menu():
    while True:
        os.system('cls')
        print('1. Mostrar todos los alumnos')
        print('2. Buscar un alumno por ID')
        print('3. Eliminar alumno por ID')
        print('4. Actualizar nombre de alumno')
        print('5. Buscar un rango de ID de alumno')
        print('6. Añadir alumno')
        print('7. Salir')

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            os.system('cls')
            opcion1(alumnos_1)
            os.system('pause')
        elif opcion == '2':
            os.system('cls')
            id=preguntarid;
            opcion2(id,alumnos_1)
            os.system('pause')
        elif opcion == '3':
            os.system('cls')
            opcion3(id,alumnos_1)
            os.system('pause')
        elif opcion == '4':
            os.system('cls')
            opcion4(alumnos_1)
            os.system('pause')
        elif opcion == '5':
            os.system('cls')
            opcion5(alumnos_1)
            os.system('pause')
        elif opcion == '6':
            os.system('cls')
            opcion6(alumnos_1)
            os.system('pause')
        elif opcion == '7':
            os.system('cls')
            print('Bye')
            os.system('pause')
            break
        else:
            print('Opción inválida. Intente nuevamente.')

if __name__ == "__main__":
    os.system('cls')
    menu()
