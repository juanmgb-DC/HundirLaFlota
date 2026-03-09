from nave import Nave
from tablero import Tablero


class Juego:

    def __init__(self):
        # Creamos un tablero de 5x5 compuesto por objetos Casilla
        self.tablero = [[Tablero() for _ in range(5)] for _ in range(5)]
        self.inicializar_naves()  # Colocamos las naves en el tablero
        resultado = self.lanzar_ataque(3,2)
        self.mostar_resultado(resultado)



    def inicializar_naves(self):
        # Ejemplo: Colocar un Submarino (de tamaño 1) en la posición (3,1)
        submarino = Nave("Submarino", 1)
        self.tablero[3][1].ocupante = submarino
        # Aquí se podrían colocar más naves de diferentes tamaños y posiciones

    def lanzar_ataque(self, x, y):
        casilla = self.tablero[x][y]  # Obtenemos la casilla objetivo
        if casilla.revelada:
            # Si ya se disparó aquí, avisamos al usuario
            print(f"Ya has disparado en ({x}, {y})")
            return

        se_hundio = casilla.disparar()  # Disparamos a la casilla y comprobamos si se hundió una nave

        if casilla.ocupante:
            # Si había una nave, informamos del impacto
            print(f"¡Impacto en un {casilla.ocupante.nombre}!")
            if se_hundio:
                # Si la nave se ha hundido, lo notificamos
                print(f"¡Hundido! Has destruido el {casilla.ocupante.nombre}")
        else:
            # Si no había nave, es agua
            print("Agua.")

    def mostar_resultado(self,resultado):...

if __name__ == "__main__":
    Juego()