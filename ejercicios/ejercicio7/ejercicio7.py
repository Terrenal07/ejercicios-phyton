import os

def ejercicio1():
    per = {}
    out = False
    pre = False
    sum=0
    while out == False:
        pre = False
        cla = input("Introduce artículo: ")
        while pre == False:
            val = input("Introduce precio: ")
            per[cla] = val
            try:
                int(val)
                pre = True
            except ValueError:
                print('Entrada no válida')
                pre = False
        sal = input("¿Finalizar compra? (S/N): ")
        if sal.upper() == 'S':
            out = True
        else:
            out = False
    print('Lista de la compra')
    for i, e in per.items():
        print('%-10s %10s' % (i, e))
        sum+=int(e)
    print('TOTAL: %15s'%(sum))



    
if __name__ == "__main__":
    os.system('cls')
    ejercicio1()