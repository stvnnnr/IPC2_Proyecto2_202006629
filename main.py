import sys
from os import startfile, system
from xml.dom import minidom
from listaCuadritos import listaCuadritos
from listaCiudades import listaCiudades
from listaRobots import listaRobots
from robot import robotPelea, robotRescate
from Ciudad import Ciudad
from Cuadrito import cuadritoEntrada, cuadritoIntransitable, cuadritoRecurso, cuadritoTransitable, cuadritoUniCivil
global listaCiudad
listaCiudad = listaCiudades()
global listaRob 
listaRob = listaRobots()

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

def cargaarchivo():
    # try:
        global listaCiudad
        global listaRob
        documentt = minidom.parse(str(input("Ingrese la ruta de su archivo: --> ")))
        print("")
        raicita= documentt.documentElement
        nombreFabrica = raicita.nodeName
        #creo lista de pisos
        ciudades = raicita.getElementsByTagName("ciudad")
        robotos = raicita.getElementsByTagName("robot")
        for ciudad in ciudades:
            nombreSucio = ciudad.getElementsByTagName("nombre")[0]
            nameCiudad = str(nombreSucio.childNodes[0].data)

            comprobar=listaCiudad.buscar(nameCiudad)
            if comprobar == nameCiudad:
                listaCiudad.eliminar(nameCiudad)

            nam = ciudad.getElementsByTagName("nombre")
            for x in nam:
                filas = int(x.getAttribute("filas"))
                columnas = int(x.getAttribute("columnas"))
            ciuUno = Ciudad(nameCiudad, filas, columnas)

            contenidoFila = ""
            fils = ciudad.getElementsByTagName("fila")
            for p in fils:
                textoCrudo = p.childNodes[0].nodeValue
                texto = textoCrudo.split("\"")[1]
                contenidoFila = contenidoFila + str(texto)
            z=0
            listaa = listaCuadritos(filas, columnas)
            for i in range(1,(int(filas)+1)):
                for j in range(1,(int(columnas)+1)):
                    if contenidoFila[z] == " ":
                        a = cuadritoTransitable(i,j)
                        listaa.insertarCuadrito(a)
                        z = z+1
                    elif contenidoFila[z] == "*":
                        a = cuadritoIntransitable(i,j)
                        listaa.insertarCuadrito(a)
                        z = z+1
                    elif contenidoFila[z] == "E":
                        a = cuadritoEntrada(i,j)
                        listaa.insertarCuadrito(a)
                        z = z+1
                    elif contenidoFila[z] == "C":
                        a = cuadritoUniCivil(i,j)
                        listaa.insertarCuadrito(a)
                        z = z+1
                    elif contenidoFila[z] == "R":
                        a = cuadritoRecurso(i,j)
                        listaa.insertarCuadrito(a)
                        z = z+1
            unis = ciudad.getElementsByTagName("unidadMilitar")
            for s in unis:
                fila = int(s.getAttribute("fila"))
                columna = int(s.getAttribute("columna"))
                poder = int(s.childNodes[0].nodeValue)
                #print(str(fila), str(columna), str(poder))
                listaa.buscarPCo(fila, columna, poder)
            #listaa.recorrer()
            ciuUno.setListaCua(listaa)
            listaCiudad.insertarCiudad(ciuUno)
        for robo in robotos:
            
            nombreSuciox = robo.getElementsByTagName("nombre")[0]
            nameRoboto = nombreSuciox.childNodes[0].data
            compo=listaRob.buscar(nameRoboto)
            if compo == nameRoboto:
                listaRob.eliminar(nameRoboto)
            
            nama = robo.getElementsByTagName("nombre")
            for d in nama:
                tipo = (d.getAttribute("tipo"))
                if d.getAttribute("capacidad"):
                    capa = int(d.getAttribute("capacidad"))
            if tipo == "ChapinFighter":
                ro = robotPelea(nameRoboto, capa)
            elif tipo == "ChapinRescue":
                ro = robotRescate(nameRoboto)
            listaRob.insertarRobot(ro)
        print("El archivo de: "+nombreFabrica+ " se cargo con exito ✓")
    # except:
    #     print("ocurrio un error, vuelve a intentarlo")
    #     print("El error fue:", sys.exc_info()[0])


# Este while me ayuda a mantener activo el menu siempre
while True:
    # try:
        menuPrincipal()
        select = int(input("Selecciona alguna opción:"))
        print("\n")
        if select == 1:
            cargaarchivo()
            print("")
        elif select == 2:
            listaCiudad.mantenerMenuCiudad()
            print("")
        elif select == 0:
            print("------          Gracias por usar mi programa :3           ------")
            print("----------------------------------------------------------------")
            break
        else:
            print("No existe esa opción")
    # except:
    #     print("ocurrio un error, vuelve a intentarlo")
    #     print("El error fue:", sys.exc_info()[0])



# ja = "123456789"
# fila = 3
# Columna = 3
# listaa = listaCuadritos(fila, Columna)
# z=0
# for i in range(1,(int(fila)+1)):
#     for j in range(1,(int(Columna)+1)):
#         a = cuadritoEntrada(i,j)
#         listaa.insertarCuadrito(a)
        # print(z)
        # z+=1

# li = listaa.mostrarMatriz()
# print(li)