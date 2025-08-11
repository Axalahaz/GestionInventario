import f_siNo
import os

#!# ---------------------------------{ ACTUALIZAR PRODUCTO (inicio) }---------------------------------

def actualizarProducto(archivo, id): # id puede venir de f_buscar    
    os.system("cls")
    
    existe = False
    actualizar = False
    
    print("-"*144)
    print("• 🔄 ACTUALIZANDO PRODUCTO 🔄 •".center(144))
    print("-------------------------------".center(146))
    
    archivoTemporal = "inventarioTemporal.txt" # archivo para modificar sin sobreescribir y despues reemplazar en el original
    with open(archivo, "r") as original, open(archivoTemporal, "w") as temporal:   
        original.seek(0)
        if len(archivo) == 1: # creo restriccion por si no hay productos en el inventario
                print("❗ No hay productos para actualizar ❗")
                print("INVENTARIO VACIO")
        else:
            if id == None:
                while(True):
                    idProducto = input("Ingresar ID: ")
                    if len(idProducto) < 6:
                        print("-"*144)
                        print("❌ Ingresar ID COMPLETO ❌".center(144))
                        input("ENTER PARA REEINTENTAR".center(144))
                        print("-"*144)
                    else:
                        break
            else:
                idProducto = id
            
        for linea in original:
            if idProducto.upper() in linea:
                existe = True # prueba que existe
                print("-"*144)
                print(linea.strip()) # visualizo linea
                print("-"*144 + "\n")
                
                while(True):
                    print("____________".center(144))
                    print("•••••••••••| ACTUALIZAR |•••••••••••••".center(144))
                    print("|           ‾‾‾‾‾‾‾‾‾‾‾‾             |".center(144))
                    print("|      A - PRODUCTO  B - MARCA       |".center(144))
                    print("|      C - PRECIO    D - STOCK       |".center(144))
                    print("|      E - EXTRA     0 - actualizar  |".center(144))
                    print("••••••••••••••••••••••••••••••••••••••".center(144))
                    print("Ingresar opcion:".center(144))
                    opcion = input(" ".center(72))
                    print("-"*144)
                    
                    id, producto, marca, precio, stock, extra = linea.split(" | ")
                    match opcion.upper():
                        case "A":
                            nombreProducto = input("▸ Nuevo Nombre: ")
                            nuevoProducto = producto.split(": ") # separo entre campo: dato
                            nuevoProducto[1] = nombreProducto # sobreescribo dato
                            producto = ": ".join(nuevoProducto) # uno campo: dato de producto
                            informacionProducto = " | ".join([id, producto, marca, precio, stock, extra]) # vuelvo a unir los campos y datos de la linea
                            temporal.write(informacionProducto)
                            existe = False # para que siga escribiendo el resto de las lineas
                            actualizar = True
                            break
                        case "B":
                            nombreMarca = input("▸ Nueva Marca: ")
                            nuevaMarca = marca.split(": ") 
                            nuevaMarca[1] = nombreMarca 
                            marca = ": ".join(nuevaMarca)
                            informacionProducto = " | ".join([id, producto, marca, precio, stock, extra])
                            temporal.write(informacionProducto)
                            existe = False
                            actualizar = True
                            break
                        case "C":
                            while(True): # manejo error. precio y stock son solo numeros 
                                try:
                                    montoPrecio = float(input("▸ Nuevo Precio ($): "))
                                    break
                                except:
                                    print("-"*144)
                                print("❌ Ingresar solo numeros ❌")
                                print("-"*144)
                            nuevoPrecio = precio.split(": ") 
                            nuevoPrecio[1] = str(montoPrecio) # lo guardo como str para el .txt 
                            precio = ": ".join(nuevoPrecio)
                            informacionProducto = " | ".join([id, producto, marca, precio, stock, extra])
                            temporal.write(informacionProducto)
                            existe = False
                            actualizar = True
                            break
                        case "D":
                            while(True):
                                try:
                                    cantidadStock = int(input("▸ Nuevo Stock: "))
                                    break
                                except:
                                    print("-"*144)
                                    print("❌ Ingresar solo numeros ❌")
                                    print("-"*144)
                            nuevoStock = stock.split(": ") 
                            nuevoStock[1] = str(cantidadStock) 
                            stock = ": ".join(nuevoStock)
                            informacionProducto = " | ".join([id, producto, marca, precio, stock, extra])
                            temporal.write(informacionProducto)
                            existe = False
                            actualizar = True
                            break
                        case "E":
                            contenidoExtra = input("▸ Nuevo Extra: ")
                            nuevoExtra = extra.split(": ") 
                            nuevoExtra[1] = contenidoExtra 
                            extra = ": ".join(nuevoExtra)
                            informacionProducto = " | ".join([id, producto, marca, precio, stock, extra])
                            temporal.write(informacionProducto)
                            existe = False
                            actualizar = True
                            break
                        case "0":
                            opcion = f_siNo.siNo(input("¿Volver al menu principal? S/N: "))
                            if opcion:
                                actualizar = "actualizar"
                                break
                        case _:
                            print("\n" + "-"*144)
                            print("Incorrecto. Reintentar".center(144))
                if actualizar != "actualizar": # porque esta fuera del bucle y no quiero que se escriba a noser que se actualize
                    print("-"*144 )
                    print("Actualizacion:")
                    print(informacionProducto)
            elif not existe:
                temporal.write(linea)
            
    if actualizar == "actualizar": # confirmo actualizar sin actualizar nada
        print("❗ CONFIRMADO ❗".center(144))
    elif not existe and not actualizar:
        print("\n" + "-"*144)
        print("❌ ID ingresado no existe ❌".center(144))
    elif not existe and actualizar:
        os.replace(archivoTemporal, archivo)
        print("-"*144)
        print("✅✅ Producto actualizado exitosamente ✅✅".center(144))
    
    original.close()
    temporal.close()
    print("-"*144)
    input("ENTER menu principal".center(144))

#!# ----------------------------------{ ACTUALIZAR PRODUCTO (fin) }----------------------------------
