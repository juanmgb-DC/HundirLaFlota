
### Codigo de clase Juego que inicia el programa :
#### if __name__ == "__main__": ####
    juego = Juego()

    ataques = [(1,1), (3,3), (1,1), (0,0), (9,9)]
    for x, y in ataques:
        print(f"Disparo en ({x},{y}):")
        resultado = juego.lanzar_ataque(x, y)


### Resultado:
Disparo en (1,1):
Tocado

Disparo en (3,3):
Tocado

Disparo en (1,1):
Ya se disparó a esta casilla

Disparo en (0,0):
Agua

Disparo en (9,9):
Hundido

Process finished with exit code 0

### Fin