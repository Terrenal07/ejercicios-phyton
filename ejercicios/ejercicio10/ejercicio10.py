import os

def ejercicio1():
    cli={}
    buc=False
    nif=''
    nom=''
    pre=''
    while not buc:
        buc2=False
        men = input('Seleccione una opción:\n(1) añadir cliente\n(2) eliminar cliente\n(3) consultar cliente\n(4) mostrar todos los clientes\n(5) mostrar clientes preferentes\n(6) salir\n')
        if men == '1':  # añadir cliente
            nif=input('Indique nif: ')
            if nif in cli:
                print('El cliente ya existe')
                rep=input('¿desea sustituirlo(Y)?')
                os.system('cls')
                if rep=='N':
                    pass
                else:
                    nom=input('Indique nombre: ')
                    os.system('cls')
                    while not buc2:
                        pre=input('¿preferente(Y/N)?: ')
                        os.system('cls')
                        if pre =='Y' or 'N':
                            buc2=True
                            if pre=='Y':
                                pre='Si' 
                            else:
                                pre='No'
                            break
                    else:
                        print('dato no valido')
                cli[nif] = nif,nom,pre
            else:
                nom=input('Indique nombre: ')
                os.system('cls')
                while not buc2:
                    pre=input('¿preferente(Y/N)?: ')
                    os.system('cls')
                    if pre =='Y' or 'N':
                        buc2=True
                        if pre=='Y':
                            pre='Si' 
                        else:
                            pre='No'
                            break
                    else:
                        print('dato no valido')
                        os.system('cls')
                cli[nif] = nif,nom,pre
            
        elif men == '2':  # eliminar cliente
            eli=input('nif cliente')
            if eli in cli:
                print(f'cliente {cli[eli]}con monmbre{cli[nom]}, eliminado')
                pic=cli.pop(eli)
                
        if men == '3':  # consultar cliente
            pass
        elif men == '4':  # mostrar todos los clientes
            print('nif      | nombre        | preferente?')
            print('---------+ --------------+ -----------')
            for i, j in cli.items():
                print('{:<9}|{:<14} |{:<9}'.format(i,j[0],j[1]))
        elif men == '5':  # mostrar clientes preferentes
            print('nif      | nombre        | preferente?')
            print('---------+ --------------+ -----------')
            for i, j in cli.items():
                if j[2] == 'Si':
                    print('{:<9}|{:<14} |{:<9}'.format(i, j[0], j[1]))
        elif men == '6':  # Cerrar programa
            buc = True
        print(cli)
if __name__ == "__main__":
    os.system('cls')
    ejercicio1()
