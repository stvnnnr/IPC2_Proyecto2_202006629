from nodoCiudad import nodoCiudad
class listaCiudades:
    def __init__(self):
        self.cabeza = None

    def insertarCiudad(self, Ciudad):
        if self.cabeza is None:
            self.cabeza = nodoCiudad(Ciudad=Ciudad)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoCiudad(Ciudad=Ciudad)

    def buscar(self, name):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Ciudad.nombre == name:
                print(actual.Ciudad.nombre)
                return actual.Ciudad.nombre
            actual = actual.siguiente

    def eliminar(self,carne):
        actual=self.cabeza
        anterior=None

        while actual and actual.Ciudad.nombre != carne:
            anterior=actual
            actual=actual.siguiente

        if anterior is None:
            self.cabeza = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None