import f_inventario
import f_agregar
import f_actualizar
import f_buscar
import f_eliminar
import f_siNo

import os

#!# ----------------------------------------{ MENU (inicio) }----------------------------------------

def menu(archivo,  acceso):
    while(acceso):
        os.system("cls")
        
        print("-"*144)
        print("💡 INICIO 💡 ".center(144))
        print("-"*144)
        
        print("_________________".center(145))
        print("•••••••••••| MENU  PRINCIPAL |••••••••••".center(144))
        print("|           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾          |".center(144))
        print("|       1 - VER INVENTARIO             |".center(144))
        print("|       2 - AGREGAR PRODUCTO           |".center(144))
        print("|       3 - ACTUALIZAR PRODUCTO        |".center(144))
        print("|       4 - BUSCAR PRODUCTO            |".center(144))
        print("|       5 - ELIMINAR                   |".center(144))
        print("|       0 - SALIR                      |".center(144))
        print("••••••••••••••••••••••••••••••••••••••••".center(144))
        
        print("Ingresar opcion:".center(144))
        opcion = input(" ".center(72))
        match opcion:
            case "1":
                f_inventario.verInventario(archivo)
            case "2":
                f_agregar.agregarProducto(archivo)
                
            case "3":
                f_actualizar.actualizarProducto(archivo, id = None)
            case "4":
                f_buscar.buscarProducto(archivo)
            case "5":
                f_eliminar.eliminarProducto(archivo, id = None)
            case "0":
                opcion = f_siNo.siNo(input("¿Salir? S/N: "))
                if opcion:
                    acceso = False # vuelve al inicio del proprama
                    return acceso
            case _:
                print("-"*144)
                print("❌ Opcion incorrecta ❌".center(144))
                print("-"*144)
                input("ENTER PARA REEINTENTAR".center(144))

#!# ----------------------------------------{ MENU (fin) }----------------------------------------