
class robot(object):
    def __init__(self, nombre, Tipo):
        self.nombre =  nombre
        self.Tipo = Tipo

class robotRescate(robot):
    def __init__(self, nombre):
        robot.__init__(self, nombre, "Rescate")

class robotPelea(robot):
    def __init__(self, nombre, capaCombate):
        robot.__init__(self, nombre,"Pelea")
        self.capaCombate = capaCombate