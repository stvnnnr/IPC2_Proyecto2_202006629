class robot(object):
    def __init__(self, nombre):
        self.nombre =  nombre

class robotRescate(robot):
    def __init__(self, nombre):
        robot.__init__(self, nombre)

class robotPelea(robot):
    def __init__(self, nombre, capaCombate):
        robot.__init__(self, nombre)
        self.capaCombate = capaCombate