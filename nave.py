class Nave:
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = tamano
        self.hundido = False

    def recibir_disparo(self):
        if self.hundido:
            return 2
            # Si la nave está hundida devuelve 2

        self.vida -= 1
            # Resta una vida por el disparo recibido


        if self.vida <= 0:
            self.hundido = True
            return 2
            # Si no le quedan vidas , la nave está hundida y devuelve 2
        return 1
            # Si ha recibido el disparo pero todavia conserva vidas, está tocado