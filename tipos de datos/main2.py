import os
os.system('cls')

a=5
b='6'

print ('tipo a: ',type (a))
print ('tipo b: ',type (b))

if isinstance(a,int)and isinstance(b,int):
    r=a+b
    print('suma a+b: '.a+b)
else:
    print('no se puede sumar')

os.system('pause')