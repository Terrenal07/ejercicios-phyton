import os

def ejercicio1():
    sum=0
    print("Ejercicio 1")
    curso={'Matemáticas': 6, 'Física': 4, 'Química': 5}
    for i,e in curso.items():
        print(f'{i} tiene {e} créditos')
        sum+=float(e)
    print(f'el total de creditos es de {sum}')
    
if __name__ == "__main__":
    os.system('cls')
    ejercicio1()