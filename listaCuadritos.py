from mmap import ALLOCATIONGRANULARITY
from nodoCuadrito import nodoCuadrito

class listaCuadritos:
    def __init__(self, filas, columnas):
        self.cabeza = None
        self.filas = filas
        self.columnas = columnas
        self.contador = 0

    def insertarCuadrito(self, Cuadrito):
        if self.cabeza is None:
            self.cabeza = nodoCuadrito(Cuadrito=Cuadrito)
            self.contador +=1
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            if self.contador != self.columnas:
                self.contador +=1
                cuadUno = nodoCuadrito(Cuadrito=Cuadrito)
                actual.siguiente = cuadUno
                cuadUno.anterior = actual
            else:
                while actual.abajo:
                    actual = actual.abajo
                cuadUno = nodoCuadrito(Cuadrito=Cuadrito)
                actual.abajo = cuadUno
                cuadUno.arriba = actual
                if self.contador>1:
                    actual.siguiente = cuadUno
                    cuadUno.anterior = actual

    def mostrarMatriz(self):
        actual = self.cabeza
        img =""
        while (actual.abajo!=None) | (actual.siguiente!=None):
            img = img + " " +actual.Cuadrito.Tipo + str(actual.Cuadrito.x) + str(actual.Cuadrito.y) + "\n"
            if actual.siguiente !=None:
                actual = actual.siguiente
            else:
                img = img + "\n"
                if actual.abajo!=None:
                    actual = actual.abajo
                    while actual.anterior !=None:
                        actual = actual.anterior
        img = img+" "+actual.Cuadrito.Tipo+ str(actual.Cuadrito.x )+ str(actual.Cuadrito.y) + "\n"
        return img