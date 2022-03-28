from tkinter.messagebox import NO
from nodoCuadrito import nodoCuadrito
from Cuadrito import Cuadrito, cuadritoUniMilitar
from listaRobots import listaRobots

class listaCuadritos:
    def __init__(self, filas, columnas):
        self.cabeza = None
        self.filas = filas
        self.columnas = columnas
        self.contadorC = 0
        self.contadorF = 0
        self.listaRobs = listaRobots

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
    
    def setListaRob(self, listarob):
        self.listaRobs = listarob

    def buscarPCo(self, fila, columna, poder):
        actual = self.cabeza
        for i in range(1, int(columna)):
            actual = actual.siguiente
        for j in range(1, int(fila)):
            actual = actual.abajo
        actual.Cuadrito = cuadritoUniMilitar(fila,columna,poder)
    
    def recorrer(self):
        actual = self.cabeza
        # while actual.abajo != None:
        #     while actual.siguiente != None:
        #         print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
        #         actual = actual.siguiente
        #     print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
        #     while actual.anterior != None:
        #         actual = actual.anterior
        #     actual = actual.abajo
        # while actual.siguiente != None:
        #     print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
        #     actual = actual.siguiente
        # print(actual.Cuadrito.Tipo,"Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")


        while actual.abajo != None:
            while actual.siguiente != None:
                print(actual.Cuadrito.indicador)
                actual = actual.siguiente
            print(actual.Cuadrito.indicador)
            while actual.anterior != None:
                actual = actual.anterior
            actual = actual.abajo
        while actual.siguiente != None:
            print(actual.Cuadrito.indicador)
            actual = actual.siguiente
        print(actual.Cuadrito.indicador)
        
    def pintar(self, filas, columnas):
        lista = "."
        actual = self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Intransitable":
                    linea = "<TD BGCOLOR=\"black\"></TD>"
                if actual.Cuadrito.Tipo == "Entrada":
                    linea = "<TD BGCOLOR=\"green\"></TD>"
                if actual.Cuadrito.Tipo == "Camino":
                    linea = "<TD></TD>"
                if actual.Cuadrito.Tipo == "Militar":
                    linea = "<TD BGCOLOR=\"red\"></TD>"
                if actual.Cuadrito.Tipo == "Civil":
                    linea = "<TD BGCOLOR=\"blue\"></TD>"
                if actual.Cuadrito.Tipo == "Recurso":
                    linea = "<TD BGCOLOR=\"gray\"></TD>"
                if actual.Cuadrito.indicador == -1:
                    linea = "<TD BGCOLOR=\"yellow\"></TD>"
                if actual.siguiente !=None:
                    actual = actual.siguiente
                lista = lista +","+ linea
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        lista = lista.split(".,")[1]
        return lista
######################################################################

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
                        x = str(self.devolverXRescate(s,filas, columnas))
                        y = str(self.devolverYRescate(s,filas, columnas))
                        w = str(self.listaRobs.mantenerRobotoElegidoRescate())
                        #self.caminoRecurso(filas, columnas, int(x),int(y))
                        lol = False
                        while (not lol):
                            print("¿Ha elegido salvar la Unidad Civil localizada en: Fila:"+x+" - columna:"+y+" con el dron de rescate:"+w+"?")
                            print("Si = 1")
                            print("No = 2")
                            select = int(input("selecciona alguna opción:"))
                            if select == 1:
                                self.caminoRescate(filas, columnas,x,y)
                                print("Vamo a darle")
                                lol = True
                                return True
                            elif select == 2:
                                lol = True
                                print("No")
                                print("Volviendo....")
                                return False
                            elif select != 1 and select !=2:
                                print("esa opcion no existe")
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

    def caminoRescate(self,filas, columnas, x ,y):
        self.cambiarIndicadores(x,y,filas, columnas)
        xEntrada = self.buscarEntradaX(filas, columnas)
        yEntrada = self.buscarEntradaY(filas, columnas)
        actual = self.cabeza
        for i in range(1, int(yEntrada)):
            actual = actual.siguiente
        for j in range(1, int(xEntrada)):
            actual = actual.abajo
        actual.Cuadrito.setIndicador(1)
        ####################################
        actual.Cuadrito.x = int(actual.Cuadrito.x)
        actual.Cuadrito.y = int(actual.Cuadrito.y)
        x = int(x)
        y = int(y)
        
        if actual.Cuadrito.x < x:
            if actual.Cuadrito.y < y:
                a = self.recorridoCuatro(xEntrada,yEntrada, filas, columnas)
                print(a)
            elif actual.Cuadrito.y > y:
                a = self.recorridoTres(xEntrada,yEntrada, filas, columnas)
                print(a)
            elif actual.Cuadrito.y == y:
                identificador = "-y"
        elif actual.Cuadrito.x >x:
            if actual.Cuadrito.y < y:
                a = self.recorridoDos(xEntrada,yEntrada, filas, columnas)
                print(a)
            elif actual.Cuadrito.y > y:
                a = self.recorridoUno(xEntrada,yEntrada, filas, columnas)
                print(a)
            elif actual.Cuadrito.y == y:
                a = self.recorridoUno(xEntrada,yEntrada, filas, columnas)
                print(a)
        elif actual.Cuadrito.x == x:
            if actual.Cuadrito.y < y:
                a = self.recorridoUno(xEntrada,yEntrada, filas, columnas)
                print(a)
            elif actual.Cuadrito.y > y:
                a = self.recorridoDos(xEntrada,yEntrada, filas, columnas)
                print(a)



        actual= self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if int(actual.Cuadrito.x) == int(x) and int(actual.Cuadrito.y) == int(y):
                    actual.Cuadrito.setIndicador(0)
                if int(actual.Cuadrito.x) == int(xEntrada) and int(actual.Cuadrito.y) == int(yEntrada):
                    actual.Cuadrito.setIndicador(0)
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo

    def cambiarIndicadores(self, x,y, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Camino":
                    actual.Cuadrito.setIndicador(1)
                if int(actual.Cuadrito.x) == int(x) and int(actual.Cuadrito.y) == int(y):
                    actual.Cuadrito.setIndicador(3)
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo

    def recorridoUno(self, x,y, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if int(actual.Cuadrito.x) == int(x) and int(actual.Cuadrito.y) == int(y):
                    if actual.Cuadrito.indicador == 3:
                        return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y))
                    actual.Cuadrito.setIndicador(-1)
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        
        actual = self.cabeza
        for i in range(1, int(x)):
            actual = actual.abajo
        for j in range(1, int(y)):
            actual = actual.siguiente
        print(actual.Cuadrito.x, actual.Cuadrito.y)
        camino = ""
                #######################################
        if int(x) > int(0) and (int(actual.arriba.Cuadrito.indicador))in [1,3]:
            # print(actual.arriba.Cuadrito.x, actual.arriba.Cuadrito.y)
            camino = self.recorridoUno(actual.arriba.Cuadrito.x,actual.arriba.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) < (int(columnas)) and (int(actual.siguiente.Cuadrito.indicador)) in [1,3]:
            # print(actual.siguiente.Cuadrito.x, actual.siguiente.Cuadrito.y)
            camino = self.recorridoUno(actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(x) < (int(filas)) and (int(actual.abajo.Cuadrito.indicador)) in [1,3]:
            # print(actual.abajo.Cuadrito.x, actual.abajo.Cuadrito.y)
            camino = self.recorridoUno(actual.abajo.Cuadrito.x,actual.abajo.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) > (int(0)) and (int(actual.anterior.Cuadrito.indicador)) in [1,3]:
            # print(actual.anterior.Cuadrito.x, actual.anterior.Cuadrito.y)
            camino = self.recorridoUno(actual.anterior.Cuadrito.x,actual.anterior.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        return ("No se puede recorrer")
    
    def recorridoCuatro(self, x,y, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if int(actual.Cuadrito.x) == int(x) and int(actual.Cuadrito.y) == int(y):
                    if actual.Cuadrito.indicador == 3:
                        return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y))
                    actual.Cuadrito.setIndicador(-1)
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        
        actual = self.cabeza
        for i in range(1, int(x)):
            actual = actual.abajo
        for j in range(1, int(y)):
            actual = actual.siguiente
        print(actual.Cuadrito.x, actual.Cuadrito.y)
        camino = ""
                #######################################
        
        if int(x) < (int(filas)) and (int(actual.abajo.Cuadrito.indicador)) in [1,3]:
            # print(actual.abajo.Cuadrito.x, actual.abajo.Cuadrito.y)
            camino = self.recorridoCuatro(actual.abajo.Cuadrito.x,actual.abajo.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) < (int(columnas)) and (int(actual.siguiente.Cuadrito.indicador)) in [1,3]:
            # print(actual.siguiente.Cuadrito.x, actual.siguiente.Cuadrito.y)
            camino = self.recorridoCuatro(actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(x) > int(0) and (int(actual.arriba.Cuadrito.indicador))in [1,3]:
            # print(actual.arriba.Cuadrito.x, actual.arriba.Cuadrito.y)
            camino = self.recorridoCuatro(actual.arriba.Cuadrito.x,actual.arriba.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) > (int(0)) and (int(actual.anterior.Cuadrito.indicador)) in [1,3]:
            # print(actual.anterior.Cuadrito.x, actual.anterior.Cuadrito.y)
            camino = self.recorridoCuatro(actual.anterior.Cuadrito.x,actual.anterior.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        return ("No se puede recorrer")
    
    def recorridoDos(self, x,y, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if int(actual.Cuadrito.x) == int(x) and int(actual.Cuadrito.y) == int(y):
                    if actual.Cuadrito.indicador == 3:
                        return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y))
                    actual.Cuadrito.setIndicador(-1)
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        
        actual = self.cabeza
        for i in range(1, int(x)):
            actual = actual.abajo
        for j in range(1, int(y)):
            actual = actual.siguiente
        print(actual.Cuadrito.x, actual.Cuadrito.y)
        camino = ""
                #######################################
        
        if int(x) > int(0) and (int(actual.arriba.Cuadrito.indicador))in [1,3]:
            # print(actual.arriba.Cuadrito.x, actual.arriba.Cuadrito.y)
            camino = self.recorridoDos(actual.arriba.Cuadrito.x,actual.arriba.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) > (int(0)) and (int(actual.anterior.Cuadrito.indicador)) in [1,3]:
            # print(actual.anterior.Cuadrito.x, actual.anterior.Cuadrito.y)
            camino = self.recorridoDos(actual.anterior.Cuadrito.x,actual.anterior.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(x) < (int(filas)) and (int(actual.abajo.Cuadrito.indicador)) in [1,3]:
            # print(actual.abajo.Cuadrito.x, actual.abajo.Cuadrito.y)
            camino = self.recorridoDos(actual.abajo.Cuadrito.x,actual.abajo.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) < (int(columnas)) and (int(actual.siguiente.Cuadrito.indicador)) in [1,3]:
            # print(actual.siguiente.Cuadrito.x, actual.siguiente.Cuadrito.y)
            camino = self.recorridoDos(actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        return ("No se puede recorrer")
    
    def recorridoTres(self, x,y, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
            for j in range(int(columnas)):
                if int(actual.Cuadrito.x) == int(x) and int(actual.Cuadrito.y) == int(y):
                    if actual.Cuadrito.indicador == 3:
                        return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y))
                    actual.Cuadrito.setIndicador(-1)
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        
        actual = self.cabeza
        for i in range(1, int(x)):
            actual = actual.abajo
        for j in range(1, int(y)):
            actual = actual.siguiente
        print(actual.Cuadrito.x, actual.Cuadrito.y)
        camino = ""
                #######################################
            
        if int(x) < (int(filas)) and (int(actual.abajo.Cuadrito.indicador)) in [1,3]:
            # print(actual.abajo.Cuadrito.x, actual.abajo.Cuadrito.y)
            camino = self.recorridoTres(actual.abajo.Cuadrito.x,actual.abajo.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) > (int(0)) and (int(actual.anterior.Cuadrito.indicador)) in [1,3]:
            # print(actual.anterior.Cuadrito.x, actual.anterior.Cuadrito.y)
            camino = self.recorridoTres(actual.anterior.Cuadrito.x,actual.anterior.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino

        if int(x) > int(0) and (int(actual.arriba.Cuadrito.indicador))in [1,3]:
            # print(actual.arriba.Cuadrito.x, actual.arriba.Cuadrito.y)
            camino = self.recorridoTres(actual.arriba.Cuadrito.x,actual.arriba.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        
        if int(y) < (int(columnas)) and (int(actual.siguiente.Cuadrito.indicador)) in [1,3]:
            # print(actual.siguiente.Cuadrito.x, actual.siguiente.Cuadrito.y)
            camino = self.recorridoTres(actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y, filas, columnas)
            if camino:
                return (str(actual.Cuadrito.x) +","+ str(actual.Cuadrito.y)) + "-" + camino
        return ("No se puede recorrer")
######################################################################

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
                    print("  ",n,".","Unidad de Recursos","Fila:",actual.Cuadrito.x,"Columna:",actual.Cuadrito.y,".                     ")
                    n = n+1
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo
        print("   0 . Volver .")
        return n

    def mantenerMenuRecurso(self, filas, columnas):
        correcto = False
        if self.cabeza == None:
            print("No hay ciudades para mostrar")
        else:
            while (not correcto):
                n = self.menuRecursos(filas, columnas)
                select = int(input("selecciona alguna opción:"))
                print("\n")
                for s in range(n):
                    if select == 0:
                        correcto = True
                        break
                    elif select == s:
                        x = str(self.devolverXRecurso(s,filas, columnas))
                        y = str(self.devolverYRecurso(s,filas, columnas))
                        w = str(self.listaRobs.mantenerRobotoElegidoPelea())
                        lol = False
                        while (not lol):
                            print("¿Ha elegido salvar el Recurso localizado en: Fila:"+x+" - columna:"+y+" con el dron de Pelea:"+w+"?")
                            print("Si = 1")
                            print("No = 2")
                            select = int(input("selecciona alguna opción:"))
                            if select == 1:
                                print("Vamo a darle")
                                lol = True
                            elif select == 2:
                                lol = True
                                print("No")
                                print("Volviendo....")
                                break
                            elif select != 1 and select !=2:
                                print("esa opcion no existe")
                        break
                if select != s and select !=0:
                    print("esa opcion no existe")

    def devolverXRecurso(self,n, filas, columnas):
        actual = self.cabeza
        cont = 0
        if n == 1:
            for i in range((int(filas))):
                for j in range(int(columnas)):
                    if actual.Cuadrito.Tipo == "Recurso":
                        return actual.Cuadrito.x
                    if actual.siguiente !=None:
                        actual = actual.siguiente
                while actual.anterior:
                    actual = actual.anterior
                actual = actual.abajo

        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Recurso":
                    cont +=1
                    if cont == n:
                        return actual.Cuadrito.x
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo

    def devolverYRecurso(self,n, filas, columnas):
        actual = self.cabeza
        cont = 0
        if n == 1:
            for i in range((int(filas))):
                for j in range(int(columnas)):
                    if actual.Cuadrito.Tipo == "Recurso":
                        return actual.Cuadrito.y
                    if actual.siguiente !=None:
                        actual = actual.siguiente
                while actual.anterior:
                    actual = actual.anterior
                actual = actual.abajo

        for i in range((int(filas))):
            for j in range(int(columnas)):
                if actual.Cuadrito.Tipo == "Recurso":
                    cont +=1
                    if cont == n:
                        return actual.Cuadrito.y
                if actual.siguiente !=None:
                    actual = actual.siguiente
            while actual.anterior:
                actual = actual.anterior
            actual = actual.abajo

    def buscarEntradaX(self, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
                for j in range(int(columnas)):
                    if actual.Cuadrito.Tipo == "Entrada":
                        return actual.Cuadrito.x
                    if actual.siguiente !=None:
                        actual = actual.siguiente
                while actual.anterior:
                    actual = actual.anterior
                actual = actual.abajo

    def buscarEntradaY(self, filas, columnas):
        actual = self.cabeza
        for i in range((int(filas))):
                for j in range(int(columnas)):
                    if actual.Cuadrito.Tipo == "Entrada":
                        return actual.Cuadrito.y
                    if actual.siguiente !=None:
                        actual = actual.siguiente
                while actual.anterior:
                    actual = actual.anterior
                actual = actual.abajo
