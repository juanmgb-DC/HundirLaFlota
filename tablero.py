from nave import Nave
from casilla import Casilla

class Tablero:
    def __init__(self, tamano=10):
        self.tamano = tamano
        # Tamaño del tablero
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        # Constantes para el resultado

        self.casillero = [[Casilla() for _ in range(tamano)] for _ in range(tamano)]
        # Crea un tablero de casillas vacias


        # Crea naves
        self.por1 = Nave("Enterprise", "portaaviones", 5)
        self.fra1 = Nave("Bismarck", "fragata", 3)
        self.fra2 = Nave("Prince of Wales", "fragata", 3)
        self.fra3 = Nave("Graf Spee", "fragata", 3)
        self.sub1 = Nave("U-47", "submarino", 1)
        self.sub2 = Nave("U-96", "submarino", 1)
        self.sub3 = Nave("U-505", "submarino", 1)
        self.sub4 = Nave("U-534", "submarino", 1)

        # Coloca las naves
        self.colocar_nave(self.por1, 1, 1, "H")
        self.colocar_nave(self.fra1, 3, 3, "V")
        self.colocar_nave(self.fra2, 7, 1, "H")
        self.colocar_nave(self.fra3, 9, 1, "H")
        self.colocar_nave(self.sub1, 4, 6, "H")
        self.colocar_nave(self.sub2, 9, 9, "H")
        self.colocar_nave(self.sub3, 7, 6, "H")
        self.colocar_nave(self.sub4, 9, 5, "H")


    # Funcion para colocar las naves en la que ponemos su fila , columna y orientacion.
    def colocar_nave(self, nave, fila, col, orientacion="H"):
        if orientacion == "H":
            if col + nave.vida > self.tamano:
                raise ValueError(f"La nave {nave.nombre} no cabe horizontalmente")
            for i in range(nave.vida):
                self.casillero[fila][col + i].nave = nave
                # Esta condicion sirve para asegurar que si quieres añadir una nave de manera horizontal
                # quepa y no sobrepase los limites del tablero
        elif orientacion == "V":
            if fila + nave.vida > self.tamano:
                raise ValueError(f"La nave {nave.nombre} no cabe verticalmente")
            for i in range(nave.vida):
                self.casillero[fila + i][col].nave = nave
                # Esta condicion sirve para asegurar que si quieres añadir una nave de manera vertical
                # quepa y no sobrepase los limites del tablero


    # Dispara a las cordenadas que indiquemos si estas estan dentro del rango posible y devuelve un resultado (None, 0, 1 ,2)
    def disparar(self, x, y):
        if x < 0 or x >= self.tamano or y < 0 or y >= self.tamano:
            print("Coordenadas fuera de rango")
            return None

        resultado = self.casillero[x][y].disparar()

        if resultado is None:
            print("Ya se disparó a esta casilla")
            return None
        elif resultado == 0:
            print("Agua")
            return self.AGUA
        elif resultado == 1:
            print("Tocado")
            return self.TOCADO
        elif resultado == 2:
            print("Hundido")
            return self.HUNDIDO