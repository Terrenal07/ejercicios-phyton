import os
os.system('cls')
print('---llenar matriz---')
print('-------------------')
nuf = int(input("numero de filas: "))
nuc = int(input("numero de columnas: "))
mat = []
os.system('cls')
for i in range(nuf):
    fil = []
    print(f"fila[{i}]:")
    for j in range(nuc):
        val = int(input(f"elemento [{i},{j}]="))
        fil.append(val)
    mat.append(fil)
os.system('cls')
print("matriz llena")

print('---leer matriz---')
print('-----------------')

for i in range(len(mat)):
    for j in range(len(mat[0])):
        val = mat[i][j]
        print("%5d" % (val), end="")
    print()

