import os
os.system('cls')
import re

n=int(input('ingrese n'))#se considerara cadena

i=1
for i in range(n):
    print(i, end=" ")

print()  #inicio,final e incremento
for i in range(n, 0, -1):
    print(i, end=" ")