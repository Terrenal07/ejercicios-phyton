import os
import random
os.system('cls')

mat = []
nuf = 5
nuc = 5

for i in range(nuf):
    fil = []
    for j in range(nuc):
        fil.append(random.randint(0, 100))
    mat.append(fil)

print('---matriz inicial---')
print('-------------------')

for i in range(len(mat)):
    for j in range(len(mat[0])):
        val = mat[i][j]
        print("%5d" % (val), end="")
    print()

print()

print('---comprobar pares---')
print('---------------------')

matp = []

for i in range(nuf):
    fil = []
    for j in range(nuc):
        if mat[i][j] % 2 == 0:
            fil.append(1)
        else:
            fil.append(0)
    matp.append(fil)

print('---mostrar matriz con pares---')
print('-----------------------------')

for i in range(len(matp)):
    for j in range(len(matp[0])):
        val = matp[i][j]
        print("%5d" % (val), end="")
    print()

print()
mats = []

for i in range(len(mat)):
    fil = []
    min_v = min(mat[i])
    fil.append(min_v)
    max_v = max(mat[i])
    fil.append(max_v)
    pro = sum(mat[i]) / len(mat[i])
    fil.append(pro)
    mats.append(fil)

print()
print('---mostrar valores estadísticos---')
print('---------------------------------')

for i in range(len(mats)):
    for j in range(len(mats[0])):
        val = mats[i][j]
        print("%5d" % (val), end="")
    print()

print()
print('---estadisticas diagonal---')
print('---------------------------')

vecs = []

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == j:
            vecs.append(mat[i][j])

min_v = min(vecs)
max_v = max(vecs)
pro = sum(vecs) / len(vecs)
vecsr = [min_v, max_v, pro]

print("[max,min,prom]")
print(vecsr)