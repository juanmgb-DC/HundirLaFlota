class Nave:

    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.vida = tamano
        self.hundido = False


    def recibir_disparo(self):
        self.vida -= 1
        if self.vida <= 0:
            self.hundido = True
            print(f"¡El {self.nombre} ha sido hundido!")
        else:
            print(f"¡El {self.nombre} ha sido tocado! Vida restante: {self.vida}")