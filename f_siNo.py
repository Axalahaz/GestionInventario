import f_menu

#!# ---------------------------------------{ SI O NO (inicio) }---------------------------------------

def siNo(opcion):
    while(True):
        if opcion.lower() == "s":
            return True
        elif opcion.lower() == "n":
            return False
        else:
            opcion = input("Ingreso incorrecto. S/N: ")

#!# -----------------------------------------{ SI O NO (fin) }-----------------------------------------