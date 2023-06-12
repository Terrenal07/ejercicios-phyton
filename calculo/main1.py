import os
os.system('cls')

a,b,c=1,2,3
#es lo mismo que
a=1
b=2
c=3

print('invertir numero de dos digitos')

n=23
c=n//10#division entera
r=n%10#residuo
print('inicial: ',n)
print('cociente: ',c)
print('residuo: ',r)

print('invertido: ',r*10+c)

os.system('pause')