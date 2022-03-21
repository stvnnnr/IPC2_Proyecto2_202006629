from listaCuadritos import listaCuadritos
from listaRobots import listaRobots
class Ciudad:
    def __init__(self, nombre,filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.listaCuadritos = listaCuadritos
        self.listaRobots = listaRobots
    
    def setListaCua(self, lista):
        self.listaCuadritos = lista

    def getListaCua(self):
        return self.listaCuadritos

    def setListaRo(self, lista):
        self.listaRobots = lista

    def getListaRo(self):
        return self.listaRobots