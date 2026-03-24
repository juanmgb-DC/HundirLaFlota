class Casilla:
    def __init__(self, nave=None):
        self.nave = nave
        # Guarda la nave que hay en la casilla, si no hay nave, se guarda como None
        self.visitada = False
        # Indica si la casilla ya fue atacada


    def disparar(self):
        if self.visitada:
            return None
        # Si la casilla ya se visitó antes,
        # no dispara otra vez

        self.visitada = True
        # Marcamos la casilla como visitada

        if self.nave is None:
            return 0
        # Si no hay nave en la casilla el disparo se queda en None

        resultado = self.nave.recibir_disparo()
        return resultado
        # Si hay una nave, recibe el disparo