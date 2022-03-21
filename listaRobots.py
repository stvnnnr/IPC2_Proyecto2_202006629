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
            