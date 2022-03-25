from selectors import SelectorKey
import sys
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
                    print("extraccion")
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
                listaP.mantenerMenuRescate(filas, columnas)
            actual = actual.siguiente

    def buscarRecurso(self, nombre):
        actual =  self.cabeza
        while actual != None:
            if actual and actual.Ciudad.nombre == nombre:
                filas=actual.Ciudad.filas
                columnas=actual.Ciudad.columnas
                listaP = actual.Ciudad.getListaCua()
                listaP.mantenerMenuRecurso(filas, columnas)
            actual = actual.siguiente