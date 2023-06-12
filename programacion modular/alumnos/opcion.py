from util import cabecera,cuerpo,preguntarid,preguntarnombre,noencontrado
from crud import buscar
def opcion1(alumnos_1):
    cabecera()
    for i in alumnos_1:
        cuerpo(i)
        
def opcion2(id,alumnos_1):
    alumnobuscar = buscar(id, alumnos_1)
    if alumnobuscar:
        cabecera()
        cuerpo(alumnobuscar)
    else:
        noencontrado()

def opcion3(id,alumnos_1):
    id=preguntarid()
    val=False
    for i, alumno in enumerate(alumnos_1):
        if alumno['idAlumno'] == id:
            eli=alumnos_1.pop(i)
            print('alumno ',eli['nombre'],' eliminado')
            val=True
            break
    if val==False:
        print('no se encontro el alumno')

def opcion4(alumnos_1):
    val = False
    id = preguntarid()
    for alumno in alumnos_1:
        if alumno['idAlumno'] == id:
            alumno['nombre'] = preguntarnombre()
            print('nombre cambiado')
            val = True
            break
    if not val:
        print('alumno no encontrado')


def opcion5(alumnos_1):
    ini = input('ID inicial: ')
    fin = input('ID final: ')
    
    cabecera()

    for alumno in alumnos_1:
        if ini <= alumno['idAlumno'] <= fin:
            cuerpo(alumno)

def opcion6(alumnos_1):
    id_alumno = input('ID del alumno: ')
    nombre = input('Nombre del alumno: ')
    edad = input('Edad del alumno: ')
    casado = input('¿Está casado? (True/False): ')

    nuevo_alumno = {'idAlumno': id_alumno, 'nombre': nombre, 'edad': edad, 'casado': casado}
    alumnos_1.append(nuevo_alumno)

    print('Alumno añadido correctamente.')

