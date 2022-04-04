import sys
from os import startfile, system
from nodoCiudad import nodoCiudad
class listaCiudades:
    def __init__(self):
        self.cabeza = None

    def insertarCiudad(self, Ciudad):
        if self.cabeza is None:
            self.cabeza = nodoCiudad(Ciudad=Ciudad)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoCiudad(Ciudad=Ciudad)

    def buscar(self, name):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Ciudad.nombre == name:
                print(actual.Ciudad.nombre)
                return actual.Ciudad.nombre
            actual = actual.siguiente

    def eliminar(self,carne):
        actual=self.cabeza
        anterior=None

        while actual and actual.Ciudad.nombre != carne:
            anterior=actual
            actual=actual.siguiente

        if anterior is None:
            self.cabeza = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def menuCiudades(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU CIUDADES                          |")
        #acá iran todos las ciudades que cargue
        n=1
        while actual != None:
            print("  ",n,".",actual.Ciudad.nombre,".                     ")
            n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")

    def mantenerMenuCiudad(self):
        correcto = False
        if self.cabeza == None:
            print("No hay ciudades para mostrar")
        else:
            while (not correcto):
                self.menuCiudades()
                actual = self.cabeza
                select = int(input("selecciona alguna opción:"))
                print("\n")
                n = 1
                while actual != None:
                    if select == 0:
                        correcto = True
                        break
                    elif select == n:
                        self.mantenerCiudadElegida(actual.Ciudad.nombre)
                        break
                    n = n+1
                    actual=actual.siguiente
                if select != n and select !=0:
                    print("esa opcion no existe")

    def menuCiudadElegida(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Ciudad.nombre == nombre:
                print("")
                print("_______________________ MENU:",actual.Ciudad.nombre,"_______________________")
                print("  1. Misiones de Rescate.")
                print("  2. Misiones de Extracción.")
                print("  0. volver.")
            actual = actual.siguiente

    def mantenerCiudadElegida(self, nombre):
        while (True):
            # try:
                self.menuCiudadElegida(nombre)
                select = int(input("Selecciona alguna opción:"))
                print("\n")
                if select == 1:
                    self.buscarRescates(nombre)
                    
                elif select == 2:
                    self.buscarRecurso(nombre)
                elif select == 0:
                    print("volviendo...")
                    break
                else:
                    print("No existe esa opción")
            # except:
            #     print("ocurrio un error, vuelve a intentarlo")
            #     print("El error fue:", sys.exc_info()[0])

    def buscarRescates(self, nombre):
        actual =  self.cabeza
        while actual != None:
            if actual and actual.Ciudad.nombre == nombre:
                filas=actual.Ciudad.filas
                columnas=actual.Ciudad.columnas
                listaP = actual.Ciudad.getListaCua()
                #self.graficar(nombre,filas, columnas)
                datos=listaP.mantenerMenuRescate(filas, columnas)
                x = str(datos[0])
                y = str(datos[1])
                z= str(datos[2])
                self.graficarRescate(nombre,filas,columnas,x,y,z)
            actual = actual.siguiente


    def buscarRecurso(self, nombre):
        actual =  self.cabeza
        while actual != None:
            if actual and actual.Ciudad.nombre == nombre:
                filas=actual.Ciudad.filas
                columnas=actual.Ciudad.columnas
                listaP = actual.Ciudad.getListaCua()
                datos=listaP.mantenerMenuRecursos(filas, columnas)
                x = str(datos[0])
                y = str(datos[1])
                z= str(datos[2])
                self.graficarRecurso(nombre,filas,columnas,x,y,z)
            actual = actual.siguiente


    def graficarRescate(self, nombre, filas, columnas,x,y,nombreBot):
        actual = self.cabeza
        while actual != None:
            try:
                if actual and actual.Ciudad.nombre == nombre:
                    listaConPatron = actual.Ciudad.getListaCua()
                    textoConComas = listaConPatron.pintar(filas, columnas)
                    textoSinComas = textoConComas.split(",")
                    z=0#auxiliar
                    Archivo = open('rescate.dot', 'w')
                    cabeza = '''digraph structs {
                                node [shape=box]
                                struct3 [label=<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="1" CELLPADDING="20">
                                    '''
                    Archivo.write(cabeza)
                    for fila in range(int(filas)):
                        inicioFila = "<TR>"
                        Archivo.write(inicioFila)
                        for columna in range(int(columnas)):
                            Archivo.write(textoSinComas[z])
                            z=z+1
                        finFila = "</TR>"
                        Archivo.write(finFila)
                    finDot = '''</TABLE>>];'''
                    Archivo.write(finDot)
                    cabezaDos = '''struct4 [label=<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="15" CELLPADDING="10">
                                    <TR>
                                    <TD BGCOLOR="#6B238E" COLSPAN="20">'''
                    Archivo.write(cabezaDos)
                    nombre = (str(nombre)+"\n </TD></TR>")
                    Archivo.write(nombre)
                    misio = ("<TR> <TD BGCOLOR=\"#9932CD\" COLSPAN=\"20\"> Tipo de mision: Rescate"+"\n </TD> </TR>")
                    Archivo.write(misio)
                    ubicacion = ("<TR> <TD BGCOLOR=\"#9F5F9F\" COLSPAN=\"20\"> Unidad Civil en:"+x+","+y+"\n </TD> </TR>")
                    Archivo.write(ubicacion)
                    bot = ("<TR> <TD BGCOLOR=\"#FF00FF\" COLSPAN=\"20\"> Salvada por el dron:"+nombreBot+" </TD> </TR>")
                    Archivo.write(bot)
                    ############aca irian los otros datos
                    finDotDos = '''</TABLE>>];}'''
                    Archivo.write(finDotDos)
                    Archivo.close()
                    system('dot -Tpng rescate.dot -o rescate.png')
                    startfile('rescate.png')
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])
            actual = actual.siguiente


    def graficarRecurso(self, nombre, filas, columnas,x,y,nombreBot):
        actual = self.cabeza
        while actual != None:
            try:
                if actual and actual.Ciudad.nombre == nombre:
                    listaConPatron = actual.Ciudad.getListaCua()
                    textoConComas = listaConPatron.pintar(filas, columnas)
                    textoSinComas = textoConComas.split(",")
                    z=0#auxiliar
                    Archivo = open('recurso.dot', 'w')
                    cabeza = '''digraph structs {
                                node [shape=box]
                                struct3 [label=<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="1" CELLPADDING="20">
                                    '''
                    Archivo.write(cabeza)
                    for fila in range(int(filas)):
                        inicioFila = "<TR>"
                        Archivo.write(inicioFila)
                        for columna in range(int(columnas)):
                            Archivo.write(textoSinComas[z])
                            z=z+1
                        finFila = "</TR>"
                        Archivo.write(finFila)
                    finDot = '''</TABLE>>];'''
                    Archivo.write(finDot)
                    cabezaDos = '''struct4 [label=<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="15" CELLPADDING="10">
                                    <TR>
                                    <TD BGCOLOR="#6B238E" COLSPAN="20">'''
                    Archivo.write(cabezaDos)
                    nombre = (str(nombre)+"\n </TD></TR>")
                    Archivo.write(nombre)
                    misio = ("<TR> <TD BGCOLOR=\"#9932CD\" COLSPAN=\"20\"> Tipo de mision: Extraccion Recurso"+"\n </TD> </TR>")
                    Archivo.write(misio)
                    ubicacion = ("<TR> <TD BGCOLOR=\"#9F5F9F\" COLSPAN=\"20\"> Unidad de Recurso en:"+x+","+y+"\n </TD> </TR>")
                    Archivo.write(ubicacion)
                    bot = ("<TR> <TD BGCOLOR=\"#FF00FF\" COLSPAN=\"20\"> Salvada por el dron:"+nombreBot+" </TD> </TR>")
                    Archivo.write(bot)
                    ############aca irian los otros datos
                    finDotDos = '''</TABLE>>];}'''
                    Archivo.write(finDotDos)
                    Archivo.close()
                    system('dot -Tpng recurso.dot -o recurso.png')
                    startfile('recurso.png')
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])
            actual = actual.siguiente