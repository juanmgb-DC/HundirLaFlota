class Nave:
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = tamano
        self.hundido = False

    def recibir_disparo(self):
        if self.hundido:
            return 2

        self.vida -= 1

        if self.vida <= 0:
            self.hundido = True
            return 2
        return 1