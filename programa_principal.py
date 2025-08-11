import f_menu
import os

#Todo# -----------------------------------
# { PROGRAMA PRINCIPAL (inicio) }----------------------------------

#** Creo si no existe el archivo .txt para almacenar la base de datos para el inventario

archivo = "inventario.txt"
if not os.path.exists(archivo):
    with open(archivo, "w") as txt:
        pass # creo el archivo si no existe
else:
    pass # trabajo con el archivo existente

""" visualizacion del .txt donde 'x' es el dato generado.

Categoria: GENERAL
ID: xx | Producto: x | Marca: x | Precio: x | Stock: x | Extra: xxxx
---
Categoria: XXXXXX
ID: xx | Producto: x | Marca: x | Precio: x | Stock: x | Extra: xxxx

"""

print("\n" + "-"*144)
print("👋 ¡¡BIENVENIDO AL SISTEMA!! 👋".center(144))
print("-"*144)
input("Enter para entrar".center(144))

acceso = True
while (acceso):
    acceso = f_menu.menu(archivo, acceso) # al salir del menu se termina el programa

os.system("cls")
print("-"*144)
print("👋 ¡¡NOS VEMOS!! 👋".center(144) + "\n" + "-"*144 + "\n")

#Todo# ------------------------------------{ PROGRAMA PRINCIPAL (fin) }------------------------------------