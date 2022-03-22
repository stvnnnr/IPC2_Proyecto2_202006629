from nodoCuadrito import nodoCuadrito
from Cuadrito import Cuadrito, cuadritoUniMilitar

class listaCuadritos:
    def __init__(self, filas, columnas):
        self.cabeza = None
        self.filas = filas
        self.columnas = columnas
        self.contadorC = 0
        self.contadorF = 0

    def insertarCuadrito(self, Cuadrito):
        actual = self.cabeza
        if self.cabeza is None:
            self.cabeza = nodoCuadrito(Cuadrito=Cuadrito)
            self.contadorC +=1
            self.contadorF +=1
            # print("metemos cabeza")
            # print(self.cabeza.Cuadrito.x,self.cabeza.Cuadrito.y)
        else:
            # print("pasamos de cabeza")
            actual = self.cabeza
            if self.contadorF == 1:
                # print("estamos en la primera fila")
                while actual.siguiente:
                    actual = actual.siguiente
                if self.contadorC != self.columnas:
                    # print("estamos en la columna"+str(self.contadorC))
                    self.contadorC +=1
                    cuadUno = nodoCuadrito(Cuadrito=Cuadrito)
                    actual.siguiente = cuadUno
                    cuadUno.anterior = actual
                    
                else:
                    # print("estamos en la columna "+str(self.contadorC)+" ultimo de la fila")
                    # print(actual.Cuadrito.x, actual.Cuadrito.y)

                    while actual.anterior:
                        actual = actual.anterior

                    # print("regresamos a")
                    # print(actual.Cuadrito.x, actual.Cuadrito.y)

                    cuadUno = nodoCuadrito(Cuadrito=Cuadrito)
                    actual.abajo = cuadUno
                    cuadUno.arriba = actual
                    # print("lolito")
                    # print(actual.Cuadrito.x, actual.Cuadrito.y)
                    # print(cuadUno.Cuadrito.x, cuadUno.Cuadrito.y)
                    self.contadorC = 1
                    self.contadorF +=1
                    # print("volvemos a la primera columna")
                    # print("enlazamos el de la primera columna con en nuevo que seria abajo")
            else:
                # print("estamos en la fila"+str(self.contadorF))
                while actual.abajo:
                    actual = actual.abajo#bajamos hasta encontrar el ultimo
                while actual.siguiente:
                    actual = actual.siguiente#derecha hasta encontrar el ultimo
                if self.contadorC != self.columnas:
                    self.contadorC +=1
                    cuadUno = nodoCuadrito(Cuadrito=Cuadrito)
                    actual.siguiente = cuadUno
                    cuadUno.anterior = actual
                    arib = actual.arriba.siguiente
                    cuadUno.arriba = arib
                    arib.abajo = cuadUno
                else:
                    # print("estamos en la columna "+str(self.contadorC)+" ultimo de la fila")
                    # print(actual.Cuadrito.x, actual.Cuadrito.y)
                    while actual.anterior:
                        actual = actual.anterior
                    cuadUno = nodoCuadrito(Cuadrito=Cuadrito)
                    actual.abajo = cuadUno
                    cuadUno.arriba = actual
                    # print("lolito")
                    # print(actual.Cuadrito.x, actual.Cuadrito.y)
                    # print(cuadUno.Cuadrito.x, cuadUno.Cuadrito.y)
                    self.contadorC = 1
                    self.contadorF +=1
            # print(actual.Cuadrito.x, actual.Cuadrito.y)


    def buscarPCo(self, fila, columna, poder):
        actual = self.cabeza
        for i in range(1, int(columna)):
            actual = actual.siguiente
        for j in range(1, int(fila)):
            actual = actual.abajo
        actual.Cuadrito = cuadritoUniMilitar(i,j,poder)