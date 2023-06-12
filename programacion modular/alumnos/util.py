def cabecera():
    print('%8s %10s %4s %6s' % ('idAlumno', 'nombre', 'edad', 'casado'))
    print('%8s %10s %4s %6s' % (guiones('idAlumno'), guiones('nombre'), guiones('edad'), guiones('casado')))

def guiones(cadena):
    s = ''
    for i in range(len(cadena)):
        s += '-'
    return s

def cuerpo(alumno_1):
    print('%8s %10s %4s %6s' % (alumno_1['idAlumno'], alumno_1['nombre'], alumno_1['edad'], alumno_1['casado']))

def preguntarid():
    return input('ID del alumno: ')

def preguntarnombre():
    return input('nombre nuevo del alumno: ')

def noencontrado():
    print('no se encontro el alumno')