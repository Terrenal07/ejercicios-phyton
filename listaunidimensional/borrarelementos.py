import os

os.system('cls')
n = int(input('Ingrese longitud de la lista: '))
vector = []

# Llenar la lista
for i in range(n):
    x = int(input('Ingrese un elemento: '))
    vector.append(x)
os.system('cls')
# Recorrer la lista por índice
for i in range(n):
    print(vector[i], end=' ')
    print('\n\n')
    os.system('cls')
    # Recorrer la lista por elemento
for e in vector:
    print(e, end=' ')
    
    # Eliminar por índice
def ejemplo1():
    x = int(input('Elemento a borrar por posición: '))
    vector.append(x)
    del vector[x]
    print(vector)
    
    # Eliminar por posición con pop()
def ejemplo2():
    x = int(input('Elemento a borrar por posición: '))
    vector.append(x)
    elemento = vector.pop(4)
    print(vector, 'Contenido eliminado:', elemento)
    
    # Eliminar por elemento
def ejemplo3():
    x = int(input('Elemento a borrar por elemento: '))
    vector.remove(x)
    print(vector)
