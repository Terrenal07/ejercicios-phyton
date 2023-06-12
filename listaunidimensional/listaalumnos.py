import os

os.system('cls')
codigo=[1,2,3,4,5]
nombre=['luis','miguel','carlos','arturo','carmen']
edad=[21,24,25,23,20]
estatura=[1.70,1.80,1.14,1.68,1.85]
casado=[True,False,True,True,False]

print ('%6s  %-8s  %-4s  %-10s %-8s'%('codigo','nombre','edad','estatura','casado'))
print ('%6s  %-8s  %-4s  %-10s %-8s'%('______','______','____','________','______'))
for i in range(len(codigo)):
    print ('%6d  %-8s  %-4d  %-10.2f %-8s'%(codigo[i],nombre[i],edad[i],estatura[i],casado[i]))
