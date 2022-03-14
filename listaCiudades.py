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