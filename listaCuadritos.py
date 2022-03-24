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
        actual.Cuadrito = cuadritoUniMilitar(fila,columna,poder)
    
    def recorrer(self):
        actual = self.cabeza
        while actual.abajo != None:
            while actual.siguiente != None:
                print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
                actual = actual.siguiente
            print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
            while actual.anterior != None:
                actual = actual.anterior
            actual = actual.abajo
        while actual.siguiente != None:
            print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
            actual = actual.siguiente
        print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")

    def menuRescates(self, filas, columnas):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU RESCATES                          |")
        n=1
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Civil":
                    print("  ",n,".","Unidad Civil","Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
                    n = n+1
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        print("   0 . Volver .")
        return n

    def menuRecursos(self, filas, columnas):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU RECURSOS                          |")
        n=1
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Recurso":
                    print("  ",n,".",actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"- Columna:",actual.Cuadrito.y,".                     ")
                    n = n+1
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        print("   0 . Volver .")

##################vas aqui hijo de puta, haciendo menu con contador para rescates
    def mantenerMenuRescate(self, filas, columnas):
        correcto = False
        if self.cabeza == None:
            print("No hay ciudades para mostrar")
        else:
            while (not correcto):
                n = self.menuRescates(filas, columnas)
                select = int(input("selecciona alguna opción:"))
                print("\n")
                for s in range(n):
                    if select == 0:
                        correcto = True
                        break
                    elif select == s:
                        x = self.devolverXRescate(s,filas, columnas)
                        y = self.devolverYRescate(s,filas, columnas)
                        ############### vas aqui qlo
                        break
                if select != s and select !=0:
                    print("esa opcion no existe")

    def devolverXRescate(self,n, filas, columnas):
        actual = self.cabeza
        cont = 0
        if n == 1:
            for i in range((int(filas))):
                for j in range(int(columnas)):
                    if actual.Cuadrito.Tipo == "Civil":
                        return actual.Cuadrito.x
                    if actual.siguiente !=None:
                        actual = actual.siguiente
                while actual.anterior:
                    actual = actual.anterior
                actual = actual.abajo

        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Civil":
                    cont +=1
                    if cont == n:
                        return actual.Cuadrito.x
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo

    def devolverYRescate(self,n, filas, columnas):
        actual = self.cabeza
        cont = 0
        if n == 1:
            for i in range((int(filas))):
                for j in range(int(columnas)):
                    if actual.Cuadrito.Tipo == "Civil":
                        return actual.Cuadrito.y
                    if actual.siguiente !=None:
                        actual = actual.siguiente
                while actual.anterior:
                    actual = actual.anterior
                actual = actual.abajo

        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Civil":
                    cont +=1
                    if cont == n:
                        return actual.Cuadrito.y
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo

