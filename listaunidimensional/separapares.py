import os

os.system('cls')
n = int(input('Ingrese longitud de la lista: '))
vector = [1,2,3,4,5,6,7,8,9]
vpar=[]
vimpar=[]
for e in vector:
    if e%2==0:
        vpar.append(e)
    else:
        vimpar.append(e)
print('lista inicial',vector,'\n\n')
print('lista par',vpar,'\n\n')
print('lista impar',vimpar,'\n\n')