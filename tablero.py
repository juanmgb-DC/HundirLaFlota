from nave import Nave


class Tablero:

    def __init__(self, tamano=10):
        self.tamano = tamano

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        self.disparos_realizados = [[False] * self.tamano for _ in range(self.tamano)]

        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)



        self.casillero = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, por1, por1, por1, por1, por1, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, sub1, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra2, fra2, fra2, None, None, sub3, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra3, fra3, fra3, None, sub4, None, None, None, sub2]
        ]


    def disparar(self, x, y):
        if x < 0 or x >= self.tamano or y < 0 or y >= self.tamano:
            print("Coordenadas fuera de rango")
            return None

        if self.disparos_realizados[x][y]:
            print("Ya se disparó en esa posición")
            return None

        self.disparos_realizados[x][y] = True
        objetivo = self.casillero[x][y]

        if objetivo is None:
            return self.AGUA

        return objetivo.recibir_disparo()

