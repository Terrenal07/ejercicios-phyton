import os

def ejercicio1():
    per = {}
    out = False
    while out == False:
        cla = input("Introduce una nueva clave: ")
        val = input("Introduce el valor correspondiente: ")
        per[cla] = val
        for i,e in per.items():
            print(i,":  ",e)
        print(per)
        sal = input("¿Deseas cerrar el programa? (S/N): ")
        if sal.upper() == 'S':
            out = True
        else:
            out = False



    
if __name__ == "__main__":
    os.system('cls')
    ejercicio1()