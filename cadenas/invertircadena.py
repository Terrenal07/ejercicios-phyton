import os

#rebanado
def ejemplo1():
    cadena='ola k ase?'
    for i in range(len(cadena) - 1, -1, -1):#en el comando for se especifica (objeto,inicio,fin,paso)
        print(cadena[i])#en este caso el primer -1, indica que empieze por el final de la cadena
        print(cadena)   #el segundo -1, que acabe en 0 incluido 8si solo s epoen un 0 el indice 0 no se llega a imprimir
                        #el tercer -1, indica que el paso sea -1, es decir retorcedo una posicion por ciclo

def ejemplo2():
    cadena='ola k ase?'
    s=''
    for e in cadena:
        s=e+s
    print(s)#se escribe cada nuevo caracter antes en lugar despues de la cadena, por lo que que invertido



#principal
if __name__ == "__main__":
    os.system('cls')
    ejemplo2()
