def buscar(id, alumnos_1):
    alumnobuscar = {}
    for alumno_d in alumnos_1:
        if alumno_d['idAlumno'] == id:
            alumnobuscar = alumno_d
            break
    return alumnobuscar