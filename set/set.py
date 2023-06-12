import os

def ejemplo1():
    c={4,2,1,0,0,0}
    print(c)#"ordena" de mayor a menor
    c={'Amor','Felicidad','Esperanza',
    'Libertad','Aventura','Éxito','Serenidad',
    'Pasión','Generosidad','Gratitud'} #no las "ordena" alfabeticamente
    print(c)

def ejemplo2():
    lista=[1,1,1,1,2,1,3,4,2]
    lista=list(set(lista))
    print(lista)

def ejemplo3():
    lista={4,5,1,3,3}
    conjunto={*lista}
    print(conjunto)

def ejemplo4():
    lista={4,5,1,3,3}
    conjunto=set()
    for e in lista:
        conjunto.add(e)
    print(conjunto)

def ejemplo5():#no funciona por que los conjuntos no tienen indice
    conjunto={2,3,4,3}
    for i in range(len(conjunto)):
        print(conjunto[i])
        
        print(conjunto)

def ejemplo6():
    conjunto={4,5,1,3,3}
    conjunto.remove(5)
    print(conjunto)

def ejemplo7():
    conjunto={4,5,1,3,3}
    conjunto.clear()
    print(conjunto)

def ejemplo8():
    conjunto={4,5,1,3,3}
    for i in range(len(conjunto)):
        x=conjunto.pop()
        print(x)
    print(conjunto)

def ejemplo9():
    conjunto={4,5,1,3,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    x=conjunto.pop()
    print(x)
    print(conjunto)



if __name__ == "__main__":
    os.system('cls')
    ejemplo9()
