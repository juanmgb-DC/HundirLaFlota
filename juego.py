from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        # Crea un tablero nuevo al iniciar el juego

    def lanzar_ataque(self, x, y):
        return self.tablero.disparar(x, y)
        # Envia un disparo a la coordenada x, y y recibe un ataque

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")
        else:
            print("Resultado no válido")
        # Segun el resultado nos devuelve distintas opciones

if __name__ == "__main__":
    juego = Juego()
    #Crea una instancia del juego

    # Lista varios ataques para no tener que atacar de uno en uno
    ataques = [(1,1), (3,3), (1,1), (0,0), (9,9)]
    for x, y in ataques:
        print(f"\nDisparo en ({x},{y}):")
        resultado = juego.lanzar_ataque(x, y)
        # Recorre cada ataque y lo ejecuta
