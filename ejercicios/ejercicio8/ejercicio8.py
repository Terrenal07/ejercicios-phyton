import os

def ejercicio1():
    dic={'hi':'holi','how':'como','are':'estas','you':'tu','my':'mi','name':'nombre','is':'es','the':'el'}
    fra=input('introduce la frase en "ingles: ')
    fra=fra.lower()
    pal=fra.split()
    for i in range(len(pal)):
        if pal[i]in dic:
            pal[i]=dic[pal[i]]
    tra = ' '.join(pal)
    print("Frase traducida:", tra)
    print()

if __name__ == "__main__":
    os.system('cls')
    ejercicio1()