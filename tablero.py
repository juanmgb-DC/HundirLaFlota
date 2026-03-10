from nave import Nave

class Tablero:
    def __init__(self):
        self.ocupante = None
        self.revelada = False

    def disparar(self):
        self.revelada = True
        if self.ocupante:
            return self.ocupante.recibir_disparo()
        return False