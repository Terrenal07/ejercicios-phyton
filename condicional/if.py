import os
os.system('cls')

#if -then - else
#evaluar nota con aprobado o suspenso

nota=6
evalua='suspenso'
if nota >= 5:
    evalua='-aprobado-'

print(evalua)

#evaluar nota con aprobado o suspenso con else

if nota >= 5:
    evalua='-aprobado-'
else:
    evalua='-suspenso-'

print(evalua)
evalua='-suspenso-'
if nota < 0:
    evalua='-no valido-'
if nota >= 5:
    evalua='-aprobado-'
    if nota >= 7:
        evalua='-notable-'
        if nota > 10:
            evalua='-no valido-'
print(evalua)