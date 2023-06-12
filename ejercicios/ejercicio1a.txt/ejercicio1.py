import os

def ejercicio1():
    divisa={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    div=input("ingrese divisa(nombre)")
    if div in divisa:
        sim = divisa[div]
        print("Divisa encontrada:", div, "-", sim)
    else:
        print("divisa no existente")

if __name__ == "__main__":
    os.system('cls')
    ejercicio1()