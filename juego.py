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
        else:
            print("Resultado no válido")

if __name__ == "__main__":
    juego = Juego()


    ataques = [(1,1), (3,3), (1,1), (0,0), (9,9)]
    for x, y in ataques:
        print(f"\nDisparo en ({x},{y}):")
        resultado = juego.lanzar_ataque(x, y)
