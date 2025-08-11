import f_inventario
import f_siNo
import f_actualizar
import f_eliminar
import os
#!# -----------------------------------{ BUSCAR PRODUCTO (inicio) }-----------------------------------

def buscarProducto(archivo):
    seguir = True
    salir = False # acceso para volver al menu pricipal
    existe = False # me dice si se ingreso correctamente la busqueda
    
    while(seguir):
        os.system("cls")
        
        print("\n" + "-"*144)
        print("• 🔍 BUSCADOR/FILTRO 🔍  •".center(144))
        print("--------------------------".center(146))
        
        with open(archivo, "r") as txt:  
            txt.seek(0) 
            contenido = txt.read().strip()  # genero copia de archivo en memoria para poder buscar informacion.
            
        if len(contenido) > 1: 
            seguir = True
        else:
            print("-"*144)
            print("❗ INVENTARIO VACIO ❗".center(144))
            print("-"*144)
            seguir = False # salgo de buscar
            break
        
        contadorFichas = 0
        encontrado = False # indica si se encuentra
        while(True):
            buscarCategoria = input("▸ Categoria a buscar (no obligatorio): ")
            if buscarCategoria != "":
                if len(buscarCategoria) >= 3:
                    break 
                else:
                    print("-"*144)
                    print("❌ Ingresar mas de 3 caracteres ❌".center(144))
                    input("ENTER PARA REEINTENTAR".center(144))
                    print("-"*144)
            else:
                break
        
        while(True):
            buscarCaracteristica = input("▸ Caracteristica a buscar: ")
            if len(buscarCaracteristica) >= 3:
                break # porque cumple condicion
            else:
                print("-"*144)
                print("❌ Ingresar mas de 3 caracteres ❌".center(144))
                input("ENTER PARA REEINTENTAR".center(144))
                print("-"*144)
        
        categorias = contenido.split("---")
        for categoria in categorias:
            categoria = categoria.strip()
            lineas = categoria.split("\n")
            nombreCategoria = lineas[0].split(": ")[1].strip()
            if buscarCategoria.upper() in nombreCategoria and buscarCategoria != "": # busca coincidencias
                buscarCategoria = f"Categoria: {nombreCategoria}"
                existe = True
            elif buscarCategoria == "" and buscarCaracteristica != "":
                existe = True
            
            if existe:
                for producto in lineas[1:]: # tomo desde la primera linea donde se nombran los productos
                    partes = producto.split(" | ") # separo en partes la linea
                    for parte in partes:
                        campoDato = parte.split(": ") # separo entre campo: dato
                        if "ID" == campoDato[0].strip():
                            id = campoDato[1].strip()
                        if buscarCaracteristica.lower() in campoDato[1].strip().lower(): # busco coincidencia
                            encontrado = True
                    if encontrado:
                        f_inventario.ficha(id, archivo, contadorFichas) # busco los que poseen la caracteristica
                        contadorFichas += 1
                        encontrado = False # para que no se repita
                        existe = True
        if not encontrado and not existe:
            print("-"*144)
            print("❗ No se encontro la caracteristica deseada ❗\n")
            opcion = f_siNo.siNo(input("¿Reintentar? S/N: "))
            if not opcion:
                seguir = False # vuelve al menu principal
                salir = True
        else:
            print(f"╰{"─"*142}╯")
            print(f"Coincidencias: {contadorFichas}")
            print("-"*144)
            while(True):
                print("• OPCIONES •".center(144))
                print("1 - ACTUALIZAR PRODUCTO   2 - ELIMINAR PRODUCTO    0 - MENU PRINCIPAL".center(144))
                opcion = input("Opcion: ")
                match opcion:
                    case "1":
                        print("-"*144)
                        id = input("▸ Ingresar ID: ")
                        f_actualizar.actualizarProducto(archivo, id)
                        seguir = False
                        break
                    case "2":
                        print("-"*144)
                        id = input("▸ Ingresar ID: ")
                        f_eliminar.eliminarProducto(archivo, id)
                        seguir = False
                        break
                    case "0":
                        seguir = False
                        salir = True
                        break
                    case _:
                        print("-"*144)
                        print("❌ Opcion incorrecta ❌".center(144))
                        print("-"*144)
    txt.close()
    if salir: # aparece solo cuando quiero volver al menu desde la opcion
        print("\n" + "-"*144)
        input("ENTER menu principal".center(144))

#!# ------------------------------------{ BUSCAR PRODUCTO (fin) }------------------------------------

