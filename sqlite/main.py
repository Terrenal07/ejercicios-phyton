import os
import sqlite3
from os import path
from sqlite3 import Error

conexion = None

def get_conexion():
    nra = 'SQLITE\\instituto.sqlite'
    try:
        if path.exists(nra):
            conexion = sqlite3.connect(nra)
        else:
            conexion = None
        return conexion
    except Error:
        return None

def borrartabla():
    conexion = get_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        sql = "DROP TABLE IF EXISTS alumno"
        cursor.execute(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Tabla borrada")
    else:
        print('No se ha podido conectar a la base de datos')

def creartabla():
    conexion = get_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS alumno (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre varchar(20),
            estatura double,
            edad integer,
            casado boolean
        );
        """
        cursor.execute(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Tabla creada")
    else:
        print('No se ha podido conectar a la base de datos')

def insertar():
    conexion = get_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        insert_l = [
            "INSERT INTO alumno (nombre, estatura, edad, casado) VALUES ('Juan', 1.75, 25, 0);",
            "INSERT INTO alumno (nombre, estatura, edad, casado) VALUES ('María', 1.65, 23, 0);",
            "INSERT INTO alumno (nombre, estatura, edad, casado)VALUES ('Pedro', 1.80, 27, 1);"
        ]
        for i in insert_l:
            cursor.execute(i)
        conexion.commit()
        cursor.close()
        conexion.close()
        print('Datos ingresados')
    else:
        print('No se ha podido conectar a la base de datos')

def separador():
    print                           ('     +------+-----------+----------+------+--------+')
def cabecera():
    separador()
    print('     |%6s|%11s|%9s|%5s|%7s|' % ('id ',' nombre ', ' estatura ', ' edad ', ' casado '))
    separador()

def cuerpo(alumno_t):
    print('     |%5d | %-10s| %8.2f |%5d |%7s |' % (alumno_t[0], alumno_t[1], alumno_t[2], alumno_t[3], alumno_t[4]))

def select():
    i = 0
    count = 0
    conexion = get_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        query = "SELECT * FROM alumno"
        cursor.execute(query)
        registros_l = cursor.fetchall()
        total_registros = len(registros_l)
        cabecera()
        for alumno_t in registros_l:
            cuerpo(alumno_t)
            i += 1
            count += 1
            if i % 4 == 0:
                separador()
                i = 0
            elif count == total_registros:
                separador()
        cursor.close()
        conexion.close()
    else:
        print('No se ha podido conectar a la base de datos')

def eliminaalumno():
    conexion = get_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        id = input("\nIngrese el ID del Alumno a Eliminar:")
        sql = f"DELETE from alumno WHERE id={int(id)}"
        try:
            cursor.execute(sql)
            conexion.commit()
            print('\nAlumno eliminado exitosamente\n')
        except Exception as e:
            print(e)
        cursor.close()
        conexion.close()
    else:
        print('No se ha podido conectar a la base de datos')

def atualizar():
    conexion = get_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        id = int(input('Ingrese el ID del alumno a actualizar: '))
        nombre = str(input("Ingrese el nuevo nombre: "))
        query = f"UPDATE alumno SET nombre = '{nombre}' WHERE id = {id}"
        cursor.execute(query)
        conexion.commit()
        cursor.close()
        conexion.close()
    else:
        print('No se ha podido conectar a la base de datos')

if __name__ == "__main__":
    os.system('cls')
    borrartabla()
    creartabla()
    insertar()
    insertar()
    insertar()
    insertar()
    insertar()
    insertar()
    insertar()
    select()
    eliminaalumno()
    select()
    atualizar()
    select()
