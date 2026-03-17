class Nave:

    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = tamano
        self.hundido = False

    def recibir_disparo(self):
        self.vida -= 1

        if self.vida <= 0:
            self.hundido = True
            print(f"El {self.nombre} ha sido hundido")
            return 2
        else:
            print(f"El {self.nombre} ha sido tocado. Vida restante: {self.vida}")
            return 1