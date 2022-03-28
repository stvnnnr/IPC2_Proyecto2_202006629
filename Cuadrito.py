class Cuadrito(object):
    def __init__(self, Tipo, x, y):
        self.Tipo = Tipo
        self.x = x
        self.y = y
        self.indicador = 0
    
    def setIndicador(self,x):
        self.indicador = x

class cuadritoEntrada(Cuadrito):
    def __init__(self, x, y):
        Cuadrito.__init__(self, "Entrada", x, y)

class cuadritoTransitable(Cuadrito):
    def __init__(self, x, y):
        Cuadrito.__init__(self, "Camino", x, y)

class cuadritoIntransitable(Cuadrito):
    def __init__(self, x, y):
        Cuadrito.__init__(self, "Intransitable", x, y)

class cuadritoUniMilitar(Cuadrito):
    def __init__(self, x, y, capaCombate):
        Cuadrito.__init__(self, "Militar", x, y)
        self.capaCombate = capaCombate

    def setCapacidad(self, capacidad):
        self.capaCombate = capacidad

class cuadritoUniCivil(Cuadrito):
    def __init__(self, x, y):
        Cuadrito.__init__(self, "Civil", x, y)

class cuadritoRecurso(Cuadrito):
    def __init__(self, x, y):
        Cuadrito.__init__(self, "Recurso", x, y)