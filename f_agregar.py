import os

#!# ----------------------------------{ AGREGAR CATEGORIA (inicio) }----------------------------------

def agregarCategoria(archivo):
    existe = False # maneja existencia de categorias
    seguir = False # maneja si se repite el bucle
    
    with open(archivo, "a+") as txt: # lectura y escritura "a: append(cursor al final)" 
        txt.seek(0) # pongo el cursos al inicio del archivo para poder leerlo, no afecta a append
        contenido = txt.read().strip()
        # trabajo dentro del bloque with porque voy a modificar el archivo.
        
        print("----------------------------------".center(144))
        print("\nCategorias existentes: \n|", end="")
        
        if len(contenido) > 1: # me da si existen categorias
            existe = True
            categorias = contenido.split("---")
            for categoria in categorias:
                categoria = categoria.strip()
                lineas = categoria.split("\n")
                nombreCategoria = lineas[0].split(": ")[1].strip()
                if nombreCategoria != "GENERAL": 
                    print(f" {nombreCategoria} ", end="|")
            print("")
        else:
            print(" No hay categorias creadas |")
        
        print("\n"+"-"*144)
        print("0: Crear categoria       1: Agregar producto a 'General'      2: Categoria existente".center(144))
        print("ENTER: Volver al menu".center(144))
        
        print("-"*144)
        opcion = input("Opcion: ")
        
        match opcion:
            case "0":
                print("-"*144)
                while(True):
                    categoria = input("▸ Nueva categoria (+3 caracteres): ")
                    if len(categoria) >= 3:
                        break
                    else:
                        print("-"*144)
                        print("❌ Ingresar mas de 3 caracteres ❌".center(144))
                        input("ENTER PARA REEINTENTAR".center(144))
                xCategoria = f"Categoria: {categoria.upper()}"
                txt.write("---\n") # genero la division de categorias al final de "inventario.txt"
                txt.write(f"{xCategoria}\n") # agrego la categoria 
                return xCategoria
            case "1":
                xCategoria = "Categoria: GENERAL"
                return xCategoria
            case "2":
                if not existe: # not false = true, maneja el conflicto por si no hay categorias existentes
                    print("-"*144)
                    print("❗ No hay categorias para elegir ❗".center(144))
                    input("ENTER PARA REEINTENTAR".center(144))
                    seguir = True
                    return seguir
                else:
                    while(True):
                        print("-"*144)
                        opcion = input("▸ Ingresar categoria (+3 caracteres): ")
                        if len(opcion) >= 3:
                            for categoria in categorias:
                                categoria = categoria.strip()
                                lineas = categoria.split("\n")
                                nombreCategoria = lineas[0].split(": ")[1].strip()
                                if opcion.upper() in nombreCategoria:
                                    print(f"❗ Categoria elegida: {nombreCategoria} ❗".center(144))
                                    print("-"*144)
                                    input("ENTER para continuar".center(144))
                                    elegidaCategoria = f"Categoria: {nombreCategoria}"
                                    return elegidaCategoria
                                elif opcion.upper() == "GENERAL":
                                    print("-"*144)
                                    print("❌ ERROR ❌".center(144))
                                    input("ENTER PARA REEINTENTAR".center(144))
                                    seguir = True
                                    return seguir
                            if existe: # existe = true porque hay categorias.
                                print("-"*144)
                                print("❌ No se encontraron coincidencias ❌".center(144))
                                input("ENTER PARA REEINTENTAR".center(144))
                        else:
                            print("-"*144)
                            print("❌ Ingresar mas de 3 caracteres ❌".center(144))
                            input("ENTER PARA REEINTENTAR".center(144))
            case "":
                return seguir
            case _:
                print("-"*144)
                print("❌ ERROR ❌".center(144))
                input("ENTER PARA REEINTENTAR".center(144))
                seguir = True
                return seguir
    # automaticamente se cierra el bloque with que trabaja con el archivo

#!# -----------------------------------{ AGREGAR CATEGORIA (fin) }-----------------------------------

#!# -----------------------------------{ AGREGAR PRODUCTO (inicio) }-----------------------------------

def agregarProducto(archivo):
    os.system("cls")
    
    seguir = True
    while(seguir):
        print("-"*144)
        print("• 🛒 AGREGANDO NUEVO PRODUCTO 🛒 •".center(144))
        
        eleccion = agregarCategoria(archivo)
        
        if not eleccion:
            seguir = False # vuelvo al menu principal
        if type(eleccion) == type("texto"):
            os.system("cls")
            break # continuo agregando producto
    
    archivoTemporal = "inventarioTemporal.txt" # archivo para modificar sin sobreescribir y despues reemplazar en el original
    with open(archivo, "r") as original, open(archivoTemporal, "w") as temporal:   
        contenido = original.read().strip()  # genero copia de archivo en memoria para poder buscar informacion.
        original.seek(0)
        
        if seguir:
            print("-"*144)
            print(f"• ❗❗ AGREGANDO A {eleccion.split(": ")[1].upper()} ❗❗ •".center(144))
            print("-"*144)

            # quiero contar cuantos ID tiene la categoria
            categorias = contenido.split("---")
            cantidadID = -1
            for categoria in categorias:
                categoria = categoria.strip()
                lineas = categoria.split("\n")
                if eleccion == lineas[0]:
                    if len(lineas) > 1:
                        for producto in lineas[1:]:
                            ultimoProducto = producto
                            cantidadID += 1
                    else:
                        cantidadID = 0
                        ultimoProducto = "" # la categoria esta vacia
            
            contador = cantidadID
            existe = False
            for linea in original: # recorro el archivo original
                if eleccion == linea.strip(): # encuentro coincidencia con la categoria
                    temporal.write(linea) # copia la linea al archivoTemporal
                    existe = True
                    nombreProducto = input("\n▸ Producto: ")
                    marca = input("\n▸ Marca: ")
                    while(True): # manejo error. precio y stock son solo numeros 
                        try:
                            precio = float(input("\n▸ Precio ($): "))
                            break
                        except:
                            print("-"*144)
                            print("❌ Ingresar solo numeros ❌")
                            print("-"*144)
                    while(True):
                        try:
                            stock = int(input("\n▸ Stock: "))
                            break
                        except:
                            print("-"*144)
                            print("❌ Ingresar solo numeros ❌")
                            print("-"*144)
                    extra = input("\n▸ Extra: ")
                    if ultimoProducto == "": # si no tiene productos
                        id = eleccion.split(": ")[1].strip() # Categoria: xxx
                        existe = False
                        # agrego linea del producto nuevo
                        ultimoID = (f"ID: {id[:3]+(str(cantidadID+1)).rjust(3, '0')} | " + 
                                    f"Producto: {nombreProducto} | " +
                                    f"Marca: {marca} | " +
                                    f"Precio: {str(precio)} | " +
                                    f"Stock: {str(stock)} | " +
                                    f"Extra: {extra}\n")
                        temporal.write(ultimoID)
                elif not existe:
                    temporal.write(linea)
                elif existe:
                    if contador >= 0: # copia lineas de la categoria deseada
                        temporal.write(linea)
                        contador -= 1
                        if contador == -1:
                            id = eleccion.split(": ")[1].strip() # Categoria: xxx
                            existe = False
                            
                            ultimoID = (f"ID: {id[:3]+(str(cantidadID+1)).rjust(3, '0')} | " + 
                                        f"Producto: {nombreProducto} | " +
                                        f"Marca: {marca} | " +
                                        f"Precio: {precio} | " +
                                        f"Stock: {stock} | " +
                                        f"Extra: {extra}\n")
                            temporal.write(ultimoID)
    
    if contador == -1 or ultimoProducto == "":
        os.replace(archivoTemporal, archivo)
        print("\n" + "-"*144)
        print("✅✅ Producto agregado exitosamente ✅✅".center(144))

    original.close()
    temporal.close()
    print("-"*144)
    input("ENTER menu principal".center(144))


#!# ------------------------------------{ AGREGAR PRODUCTO (fin) }------------------------------------