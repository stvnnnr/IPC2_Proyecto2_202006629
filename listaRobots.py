from nodoRobot import nodoRobot

class listaRobots:
    def __init__(self):
        self.cabeza = None

    def insertarRobot(self, Robot):
        if self.cabeza is None:
            self.cabeza = nodoRobot(robot=Robot)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoRobot(robot=Robot)

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print("name="+actual.robot.nombre,"tipo="+actual.robot.Tipo,"->")
            actual=actual.siguiente
    
    def buscar(self, name):
        actual = self.cabeza
        while actual != None:
            if actual and actual.robot.nombre == name:
                print(actual.robot.nombre)
                return actual.robot.nombre
            actual = actual.siguiente

    def eliminar(self,carne):
        actual=self.cabeza
        anterior=None

        while actual and actual.robot.nombre != carne:
            anterior=actual
            actual=actual.siguiente

        if anterior is None:
            self.cabeza = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
    
    def menuRobRescate(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU DRONES                          |")
        n=1
        while actual != None:
            if actual.robot.Tipo == "Rescate":
                print("  ",n,".",actual.robot.nombre,".                     ")
                n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")

    def mantenerRobotoElegidoRescate(self):
        correcto = False
        if self.cabeza == None:
            print("No hay drones de rescate para mostrar")
        else:
            while (not correcto):
                self.menuRobRescate()
                actual = self.cabeza
                select = int(input("Que dron quiere para su misión:"))
                print("\n")
                n = 1
                while actual != None:
                    if actual.robot.Tipo == "Rescate":
                        if select == 0:
                            correcto = True
                            break
                        elif select == n:
                            return(actual.robot.nombre)
                        n = n+1
                    actual=actual.siguiente
                if select != n and select !=0:
                    print("esa opcion no existe")

    def menuRobPelea(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU DRONES                          |")
        n=1
        while actual != None:
            if actual.robot.Tipo == "Pelea":
                print("  ",n,".",actual.robot.nombre,".                     ")
                n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")

    def mantenerRobotoElegidoPelea(self):
        correcto = False
        if self.cabeza == None:
            print("No hay drones de rescate para mostrar")
        else:
            while (not correcto):
                self.menuRobPelea()
                actual = self.cabeza
                select = int(input("Que dron quiere para su misión:"))
                print("\n")
                n = 1
                while actual != None:
                    if actual.robot.Tipo == "Pelea":
                        if select == 0:
                            correcto = True
                            break
                        elif select == n:
                            return(actual.robot.nombre)
                        n = n+1
                    actual=actual.siguiente
                if select != n and select !=0:
                    print("esa opcion no existe")