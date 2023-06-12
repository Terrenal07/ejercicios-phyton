import os
os.system('cls')
print()
print('---matriz tamaño fijo---')
print('-----------------------')

mat=[(1,2,3),
        (4,5,6),
        (7,8,9)]
print()
print('---recorre matriz por indice---')
print('-------------------------------')

for i in range(len(mat)):
    for j in range(len(mat[0])):
        val=mat[i][j]
        print("%5d"%(val),end="")
    print ()
print()
print('---recorre matriz por elemento---')
print('---------------------------------')

for fil in mat:
    for e in fil:
        print("%5d"%(e),end="")
    print()
print()
print('---recorre matriz por fila---')
print('-----------------------------')

for fila in mat:
    print(fila)
print()
print('---recorre matriz completa---')
print('-----------------------------')

print (mat)
print()
