import os

def ejemplo1(): #clave cadena
    alumno=[{'idAlumno':'A1','nombre':'Luis','edad':23,'estatura':1.72,'casado':False},
           {'idAlumno':'A2','nombre':'Luis','edad':23,'estatura':1.72,'casado':False}]
    for clave in alumno:
        print (clave)
    print()
    for clave in alumno:
        valor=alumno[clave]
        print('%10s -- %-10s'%(clave,valor))

def ejemplo1_1():
    idalumno = input('Ingrese id del alumno: ')
    nombre = input('Ingrese nombre del alumno: ')
    edad = input('Ingrese edad del alumno: ')
    alumno={'idalumno':idalumno,'nombre':nombre,'edad':edad}
    for clave in alumno:
        print(clave,"\t",alumno[clave])

def ejemplo2(): #clave numero
    fruta={1:'manzana',2:'naranja',3:'uva',1:'fresa'}
    for clave in fruta:
        print('%10s -- %-10s'%(clave,fruta[clave]))


def ejemplo3(): #clave tupla
    fruta={('manzana','roja'):5,('manzana','amarilla'):7}
    
#se pueden mezclar tipos de valor de todos los casos


if __name__ == "__main__":
    os.system('cls')
    ejemplo3()
