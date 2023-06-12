
class Alumno:
    def __init__(self,idAlumno,nombre,edad,casado):
        self.idAlumno=idAlumno
        self.nombre=nombre
        self.edad=edad
        self.casado=casado

    @staticmethod
    def cabecera():
        print('%-8s%-10s%6s%8s'%('idAlumno','nombre','edad','casado'))
        print('%-8s%-10s%6s%8s'%('--------','------','----','------'))
        

    def cuerpo(self):
        print('%-8s%-10s%6d%8s' % (self.idAlumno, self.nombre, self.edad, self.casado))

    def __str__(self):
        return 'El alumno con id = {0} tiene nombre={1}, edad={2}, casado{3}'
        
    
