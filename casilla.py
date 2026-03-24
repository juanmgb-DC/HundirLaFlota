class Casilla:
    def __init__(self, nave=None):
        self.nave = nave
        self.visitada = False

    def disparar(self):
        if self.visitada:
            return None

        self.visitada = True

        if self.nave is None:
            return 0

        resultado = self.nave.recibir_disparo()
        return resultado