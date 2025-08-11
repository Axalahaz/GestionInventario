import f_siNo
import os

#!# ------------------------------------{ ELIMINAR PRODUCTO (inicio) }------------------------------------

def eliminarProducto(archivo, id):    
    os.system("cls")
    
    existe = False
    seguir = True
    borrar = False
        
    while(seguir):
        
        print("\n" + "-"*144)
        print("• 💣 ELIMINAR PRODUCTO 💣  •".center(144))
        print("----------------------------".center(146))
        
        archivoTemporal = "inventarioTemporal.txt" # archivo para modificar sin sobreescribir y despues reemplazar en el original
        with open(archivo, "r") as original, open(archivoTemporal, "w") as temporal:
            original.seek(0)
            # genero archivoTemporal para copiar y reescribir archivo.
            if id == None:
                while(True):
                    eleccion = input("▸ Ingresar ID del producto a borrar: ")
                    if len(eleccion) < 6:
                        print("-"*144)
                        print("❌ Ingresar ID COMPLETO ❌".center(144))
                        input("ENTER PARA REEINTENTAR".center(144))
                        print("-"*144)
                    else:
                        break
            else:
                eleccion = id
            
            for linea in original:
                if eleccion.upper() in linea:
                    existe = True
                    
                    print("-"*144)
                    print("Eliminando:")
                    print(linea.strip())
                    print("-"*144)
                    
                    opcion = f_siNo.siNo(input("❗ Confirmar Eliminacion ❗ S/N:  "))
                    if not opcion:
                        # no realizo reemplazo de archivos.
                        seguir = False
                        break # salgo del for
                    else:
                        existe = False # no copio la linea. por lo que se borra
                        borrar = True
                    
                elif not existe:
                    temporal.write(linea)
            
            if not existe and borrar: # al confirmar eliminacion 
                print("-"*144)
                print("✅✅ Producto borrado exitosamente ✅✅".center(144))
                seguir = False
            elif not existe and seguir: # id no existe y sigue el bucle
                print("-"*144)
                print("❌ NO EXISTE ID ❌".center(144))
                print("-"*144)
                opcion = f_siNo.siNo(input("¿Reintentar? S/N: "))
                if not opcion:
                    seguir = False # vuelve al menu principal
                    borrar = False
                else:
                    os.system("cls")
    
    if not existe and borrar: # confirmo eliminacion
        os.replace(archivoTemporal, archivo)
    original.close() # cierro el archivo por si no se cerro automaticamente
    temporal.close()
    print("-"*144)
    input("ENTER menu principal".center(144))

#!# --------------------------------------{ ELIMINAR PRODUCTO (fin) }-------------------------------------