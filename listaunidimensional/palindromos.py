import os

os.system('cls')
pal = input('\nIngrese texto: \n')
pal = pal.replace(" ", "")
pal = pal.replace(",", "")
pal = pal.replace(".", "")
pal = pal.replace(":", "")
pal = pal.replace(";", "")
lista_pal = list(pal)

invlista_pal=lista_pal[::-1]
str_pal = ''.join(lista_pal)
str_invpal = ''.join(invlista_pal)
print()
if str_pal==str_invpal:
    print("es palindromo\n")
else:
    print("no es palindromo\n")
