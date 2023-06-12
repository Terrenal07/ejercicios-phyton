import os


#recorrer cadena por elementos
def ejemplo1():
    cadena='hola mundo'
    for e in cadena: #funciona como un for each
        print(e,end=',')
    print('\n\n')

#recorrer cadena por indice
def ejemplo2():
    cadena='hola mundo'
    for i in range(len(cadena)): #se indica la logitud de la cadena en este caso, se indica las condicones finales
        print (cadena[i],end=',')
    print('\n')

#recorre cadena por indice y elemento
def ejemplo3():
    cadena = 'hola mundo'
    for i, e in enumerate(cadena):
        print('%5d %5s' % (i, e))
    print('\n')

#recorrer como lista de caracteres
def ejemplo4():
    cadena='hola mundo'
    lista=list(cadena)
    print(lista)
    for e in lista:
        print(e,end='')
    print('\n')


#principal
if __name__ == "__main__":
    os.system('cls')
    ejemplo1()