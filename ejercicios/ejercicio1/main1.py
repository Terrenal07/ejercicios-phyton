import os

def ejercicio1():
    input_str="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    inp = input_str.split("\n")
    for i in range(len(inp)):
        inp[i]=inp[i].split(";")
    print("%-11s %-22s %-26s %-12s %-9s"%(inp[0][0],inp[0][1],inp[0][2],inp[0][3],inp[0][4]))
    print("---         ------                 -----                      --------     ---------")
    for i in range(len(inp)-1):
        print("%-11s %-22s %-26s %-12s %-9s"%(inp[i+1][0],inp[i+1][1],inp[i+1][2],inp[i+1][3],inp[i+1][4]))

def ejercicio2():
    input_str = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    inpd={}
    inp = input_str.split("\n")
    for i in range(len(inp)):
        inp[i]=inp[i].split(";")
    for i in range(1,len(inp)):
        inpd[inp[i][0]]={'nif':inp[i][0],
                     'nombre':inp[i][1],
                     'email':inp[i][2],
                     'telefono':inp[i][3],
                     'descuento':inp[i][4]}
    print(inpd)

if __name__ == "__main__":
    os.system('cls')
    ejercicio1()
    print()
    ejercicio2()
