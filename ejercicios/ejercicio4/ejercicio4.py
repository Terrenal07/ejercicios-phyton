import os

def ejercicio1():
    fecha = input('Ingrese fecha en formato (dd/mm/aaaa): ')
    dia, mes_num, anio = fecha.split('/')

    def mes_a_texto(mes_num):
        if mes_num == '01':
            return 'enero'
        elif mes_num == '02':
            return 'febrero'
        elif mes_num == '03':
            return 'marzo'
        elif mes_num == '04':
            return 'abril'
        elif mes_num == '05':
            return 'mayo'
        elif mes_num == '06':
            return 'junio'
        if mes_num == '07':
            return 'julio'
        elif mes_num == '08':
            return 'agosto'
        elif mes_num == '09':
            return 'septiembre'
        elif mes_num == '10':
            return 'octubre'
        elif mes_num == '11':
            return 'noviembre'
        elif mes_num == '12':
            return 'diciembre'    
        else:
            return 'mes desconocido'

    mes_texto = mes_a_texto(mes_num)
    print(f"{dia} de {mes_texto} de {anio}")
if __name__ == "__main__":
    os.system('cls')
    ejercicio1()