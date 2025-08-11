import os

#!# ------------------------------------{ VER INVENTARIO (inicio) }------------------------------------

def verInventario(archivo):
    os.system("cls")
    
    print("-"*144)
    print("• 📁 Inventario 📁  •".center(144))
    print("---------------------".center(146))

    print("\n" + f"╭{"─"*142}╮")
    print("|" + " CATEGORIA ".center(21) + "+" + " ID ".center(10) + "+" + " PRODUCTO ".center(20) + "+" +
        " MARCA ".center(19) + "+" + " PRECIO ".center(18) + "+" + " STOCK ".center(11) + "+" + 
        " EXTRA ".center(37) + "|")
    
    with open(archivo, "r") as txt: # leo el archivo
        contenido = txt.read().strip() # le saco los espacios, quiero solo las cadenas
        txt.seek(0)
        # se cierra el archivo / trabajo con la copia "contenido" almacenada en memoria
    
    if len(contenido) == 0:
        print("|" + "—"*21 + "|" + "—"*10 + "|" + "—"*20 + "|" + "—"*19 + "|" + "—"*18 + "|" + "—"*11 + "|" + "—"*37 + "|") # linea divisoria
        print("|" + " ".center(142) + "|")
        print("|" + " ~ VACIO ~ ".center(142) + "|")
        print("|" + " ".center(142) + "|")
        print(f"╰{"─"*142}╯")
    else:
        categorias = contenido.split("---") # separo los bloques de categorias en .txt
        for categoria in categorias:
            print("|" + "—"*21 + "|" + "—"*10 + "|" + "—"*20 + "|" + "—"*19 + "|" + "—"*18 + "|" + "—"*11 + "|" + "—"*37 + "|") # linea divisoria
            categoria = categoria.strip() # elimino los saltos de linea que se crearon al dividir los bloques
            lineas = categoria.split("\n") # en el bloque el contenido se divide por saltos de lineas 
            nombreCategoria = lineas[0].split(": ")[1] # primera linea del bloque y la separo en dos "[0]: [1]"
            print("|" + f" {nombreCategoria} ".center(21).upper() + "|" + " ".center(10) + "|" + " ".rjust(20) + "|" + 
                " ".rjust(19) + "|" + " ".rjust(18) + "|" + " ".rjust(11) + "|" + " ".rjust(37) + "|")
            
            for productos in lineas[1:]: # tomo desde la primera linea donde se nombran los productos
                listaProductos = [] # para leer mejor el inventario guardo los datos en una lista
                informacionProductos = productos.strip().split(" | ") # separo la informacion contenida del producto
                for producto in informacionProductos:
                    datosProducto =  {producto.split(": ")[0]: producto.split(": ")[1]} # genero diccionario de producto
                    listaProductos.append(datosProducto)
                print(  "|" + "+".center(21) + "|" +
                    f" {listaProductos[0]["ID"]} ".center(10) + "|" +      # ID
                    f" {listaProductos[1]["Producto"]:>18} " + "|" +             # Producto
                    f" {listaProductos[2]["Marca"]:>17} " + "|" +             # Marca
                    f" $ {listaProductos[3]["Precio"]} ".rjust(18) + "|" +     # Precio
                    f" {listaProductos[4]["Stock"]:>9} " + "|" +              # Stock
                    f" {listaProductos[5]["Extra"]:>35} " + "|")              # Extra
        
        print(f"╰{"─"*142}╯") 
    txt.close() # cierro el archivo por si no se cerro automaticamente
    print("\n" + "-"*144)
    input("ENTER menu principal".center(144))

#!# --------------------------------------{ VER INVENTARIO (fin) }--------------------------------------

#!# -----------------------------------------{ FICHA (inicio) }-----------------------------------------

def ficha(id, archivo, contadorFichas):
    with open(archivo, "r") as txt:
        txt.seek(0)
        contenido = txt.read().strip()
    
    categorias = contenido.split("---") 
    
    for categoria in categorias:
        categoria = categoria.strip() # elimino los saltos de linea que se crearon al dividir los bloques
        lineas = categoria.split("\n") # en el bloque el contenido se divide por saltos de lineas 
        nombreCategoria = lineas[0].split(": ")[1] # primera linea del bloque y la separo en dos "[0]: [1]"
        
        
        for productos in lineas[1:]: # tomo desde la primera linea donde se nombran los productos
            listaProductos = [] # para leer mejor el inventario guardo los datos en una lista
            informacionProductos = productos.strip().split(" | ") # separo la informacion contenida del producto
            for producto in informacionProductos:
                datosProducto =  {producto.split(": ")[0]: producto.split(": ")[1]} # genero diccionario de producto
                listaProductos.append(datosProducto)
            if id == listaProductos[0]["ID"]:
                if contadorFichas == 0:
                    print("\n" + f"╭{"─"*142}╮")
                    print("|" + " CATEGORIA ".center(21) + "+" + " ID ".center(10) + "+" + " PRODUCTO ".center(20) + "+" +
                        " MARCA ".center(19) + "+" + " PRECIO ".center(18) + "+" + " STOCK ".center(11) + "+" + 
                        " EXTRA ".center(37) + "|")
                    print("|" + "—"*21 + "|" + "—"*10 + "|" + "—"*20 + "|" + "—"*19 + "|" + "—"*18 + "|" + "—"*11 + "|" + "—"*37 + "|") # linea divisoria
                    
                print("|" + f" {nombreCategoria} ".center(21).upper() + "|" + " ".center(10) + "|" + " ".rjust(20) + "|" + 
                    " ".rjust(19) + "|" + " ".rjust(18) + "|" + " ".rjust(11) + "|" + " ".rjust(37) + "|")
                
                print(  "|" + "+".center(21) + "|" +
                    f" {listaProductos[0]["ID"]} ".center(10) + "|" +      # ID
                    f" {listaProductos[1]["Producto"]:>18} " + "|" +             # Producto
                    f" {listaProductos[2]["Marca"]:>17} " + "|" +             # Marca
                    f" $ {listaProductos[3]["Precio"]} ".rjust(18) + "|" +     # Precio
                    f" {listaProductos[4]["Stock"]:>9} " + "|" +              # Stock
                    f" {listaProductos[5]["Extra"]:>35} " + "|")              # Extra
        
        
        
        """ for producto in lineas[1:]: # tomo desde la primera linea donde se nombran los productos
            informacionProducto = producto.split(" | ") # separo la informacion contenida del producto
            if id == informacionProducto[0].split(": ")[1]:
                if contadorFichas == 0:
                    print("\n" + f"╭{"─"*142}╮")
                    print("|" + " CATEGORIA ".center(21) + "+" + " ID ".center(10) + "+" + " PRODUCTO ".center(20) + "+" +
                        " MARCA ".center(19) + "+" + " PRECIO ".center(18) + "+" + " STOCK ".center(11) + "+" + 
                        " EXTRA ".center(37) + "|")
                    print("|" + "—"*21 + "|" + "—"*10 + "|" + "—"*20 + "|" + "—"*19 + "|" + "—"*18 + "|" + "—"*11 + "|" + "—"*37 + "|") # linea divisoria
                    
                print("|" + f" {nombreCategoria} ".center(21).upper() + "|" + " ".center(10) + "|" + " ".rjust(20) + "|" + 
                    " ".rjust(19) + "|" + " ".rjust(18) + "|" + " ".rjust(11) + "|" + " ".rjust(37) + "|")
                
                print(  "|" + "+".center(21) + "|" +
                        f" {informacionProducto[0].split(": ")[1]} ".center(10) + "|" +      # ID
                        f" {informacionProducto[1].split(": ")[1]:>18} " + "|" +             # Producto
                        f" {informacionProducto[2].split(": ")[1]:>17} " + "|" +             # Marca
                        f" $ {informacionProducto[3].split(": ")[1]} ".rjust(18) + "|" +     # Precio
                        f" {informacionProducto[4].split(": ")[1]:>9} " + "|" +              # Stock
                        f" {informacionProducto[5].split(": ")[1]:>35} " + "|")              # Extra     """           
    txt.close() # cierro el archivo por si no se cerro automaticamente
    
#!# ------------------------------------------{ FICHA (fin) }------------------------------------------