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