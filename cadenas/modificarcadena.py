import os
import re
#sustituir volcales por 'x'
er='[aeiouAEIOUáéíóúÁÉÍÓÚ]'
#rebanado
def ejemplo1():
    s=''
    cadena='ola k ase?'
    for e in cadena:
        if re.match(er,e):
            s+='x'
        else:
            s+=e
    print(s)

def ejemplo2():
    cadena='ola k ase?'
    cadena=re.sub(er,'x',cadena)
    print(cadena)

#eliminar numeros d euna cadena
def ejemplo3():
    er='[0-9]'
    s=''
    cadena='16ola 4165k a5614s156e?'
    for e in cadena:
        if re.match(er,e):
            s=s
        else:
            s+=e
    print(s)

def ejemplo4():
    er='[0-9]'
    cadena='ola k ase?'
    cadena=re.sub(er,'',cadena)
    print(cadena)

#principal
if __name__ == "__main__":
    os.system('cls')
    ejemplo4()

