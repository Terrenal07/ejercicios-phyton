import os

def ejercicio1():
    fruta = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}
    fru = input('¿Fruta deseada?: ')
    cnt = float(input('Cantidad en kilogramos: '))  # Convertir a número decimal
    
    if fru in fruta:
        print(f"Su pedido con {cnt} kilogramos de {fru} cuesta {fruta[fru] * cnt}€")
    else:
        print("La fruta ingresada no está disponible en la lista.")


if __name__ == "__main__":
    os.system('cls')
    ejercicio1()