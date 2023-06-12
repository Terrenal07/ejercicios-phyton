import os


def ejemplo1():
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    mes = {}
    for i in range(len(meses)):
        mes[i] = meses[i]
    for clave in mes:
        print('%10s -- %-10s' % (clave, mes[clave]))

def ejemplo2():
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    mesesd={}
    for k,v in zip(meses,range(len(meses))):
        mesesd[v]=k
    print(mesesd)

def ejemplo3(): 
    alumno={'idAlumno':'A1','nombre':'Luis','edad':23,'estatura':1.72,'casado':False}
    clave=input('ingrese clave: ')
    valor=alumno.get(clave)
    print(clave,' : ', valor)

def ejemplo4():
    alumno = {
        'idAlumno': 'A1',
        'nombre': 'Luis',
        'edad': 23,
        'estatura': 1.72,
        'casado': False,
        'asignaturas': ['fisica', 'quimica', 'matematicas']
    }
    asignatura = input('Ingrese el nombre de la asignatura: ')
    if asignatura in alumno['asignaturas']:
        print('inscrito en', asignatura)
    else:
        print('no inscrito en', asignatura)

if __name__ == "__main__":
    os.system('cls')
    ejemplo4()
