import sys
from os import startfile, system
from xml.dom import minidom









#estructura de mi menu principal
def menuPrincipal():
    print("                                                                ")
    print("|                                                              |")
    print("|*******************Misiones Chapín Warriors*******************|")
    print("|                                                              |")
    print("|  1. Cargar mapa de ciudad.                                   |")
    print("|  2. Ciudades Cargadas.                                       |")
    print("|  0. Salir.                                                   |")
    print("----------------------------------------------------------------")





#Este while me ayuda a mantener activo el menu siempre
while True:
    try:
        menuPrincipal()
        select = int(input("Selecciona alguna opción:"))
        print("\n")
        if select == 1:
            print("")
        elif select == 2:
            print("")
        elif select == 0:
            print("------          Gracias por usar mi programa :3           ------")
            print("----------------------------------------------------------------")
            break
        else:
            print("No existe esa opción")
    except:
        print("ocurrio un error, vuelve a intentarlo")
        print("El error fue:", sys.exc_info()[0])