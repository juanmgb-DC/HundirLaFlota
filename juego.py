from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()

    def lanzar_ataque(self, x, y):
        return self.tablero.disparar(x, y)

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")


if __name__ == "__main__":
    juego = Juego()
    resultado = juego.lanzar_ataque(5, 3)
    juego.mostrar_resultado(resultado)