from alumno import Alumno

class Opcion:
    @staticmethod
    def opcion1(alumnos):
        Alumno.cabecera()
        for alumno in alumnos:
            alumno.cuerpo()

    @staticmethod
    def opcion2(alumnos):
        idAlumno = input('INGRESE ID ALUMNO A BUSCAR? ')
        alumno = Opcion.buscar(idAlumno, alumnos)
        if not alumno:
            print("ERROR: NO EXISTE ALUMNO CON ESE ID")
        else:
            Alumno.cabecera()
            alumno.cuerpo()


    @staticmethod
    def opcion3(alumnos):
        idAlumno = input('INGRESE ID ALUMNO A ELIMINAR: ')
        val = False
        for i, alumno in enumerate(alumnos):
            if alumno.idAlumno == idAlumno:
                eli = alumnos.pop(i)
                print('Alumno', eli.nombre, 'eliminado')
                val = True
                break
        if not val:
            print('No se encontró el alumno')

    @staticmethod
    def opcion4(alumnos):
        idAlumno = input('INGRESE ID ALUMNO A MODIFICAR: ')
        val = False
        for i, alumno in enumerate(alumnos):
            if alumno.idAlumno == idAlumno:
                nombre = input('INGRESE NOMBRE NUEVO: ')
                ant=alumnos[i].nombre
                print(f'NOMBRE DE ALUMNO {i}, {alumno.nombre}, CAMBIADO A {nombre}')
                alumnos[i].nombre=nombre
                val = True
                break
        if not val:
            print('No se encontró el alumno')

    @staticmethod
    def opcion5(alumnos):
        pass
        

    @staticmethod
    def opcion6(alumnos):
        id=input('INGRESE ID: ')
        existe_id = False
        buc=False
        for alumno in alumnos:
            if alumno.idAlumno == id:
                existe_id = True
                break
        if existe_id == True:
            print('ID YA EN USO')
        else:
            nam=input('INGRESE NOMBRE: ')
            while buc==False:
                eda=input('INGRESE EDAD: ')
                if eda.isdigit():
                    while True:
                        cas=input('¿CASADO(Y/N)?: ')
                        if cas=='Y' or cas=='N':  
                            buc=True     
                            if cas=='Y':
                                cas=True
                                alumnos.append(Alumno(id, nam, int(eda), cas))
                                break
                            else:
                                cas=False
                                alumnos.append(Alumno(id, nam, int(eda), cas))
                                break
                        else:
                            print('DATO NO VALIDO')
                else:
                    print("DATO NO VALIDO")
        
            
            
    @staticmethod
    def buscar(idAlumno, alumnos):
        for alumno in alumnos:
            if alumno.idAlumno == idAlumno:
                return alumno
        return None
