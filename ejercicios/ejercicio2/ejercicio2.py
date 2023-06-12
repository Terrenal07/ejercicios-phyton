import os

def ejercicio1():
    nom=input('introduzca nombre: ')
    eda=input('introduzca edad: ')
    tfn=input('introduzca numero de telefono: ')
    dir=input('introduzca direccion: ')
    usu= {'tfn': {'nombre': nom,'direccion': dir,'edad':eda,}}
    print(f"{usu['tfn']['nombre']} vive en {usu['tfn']['direccion']} y su número de teléfono es {tfn}.")

if __name__ == "__main__":
    os.system('cls')
    ejercicio1()