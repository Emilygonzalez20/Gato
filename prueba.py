import random

def mostrar_menu():
    print("¡Bienvenido al juego del Gato!")
    print("Menú:")
    print("a. Nueva partida (Player 1 VS COM)")
    print("b. Versus (P1 VS P2)")
    print("c. Salir")

def imprimir_tablero(tablero):
    for fila in tablero:
        print(''.join(fila))

def jugar_contra_computadora():
    jugador_1 = input("Ingrese el nombre del jugador 1 (x): ")
    jugador_2 = "Computadora"
    turno_1 = True
    turno = 0

    tablero = [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
    ]

    while turno < 9:
        imprimir_tablero(tablero)
        if turno_1:
            print(f"{jugador_1}, elige una posición por favor:")
            jugada = int(input())
        else:
            jugada = random.randint(1, 9)

        valor = cambiar_tablero(tablero, jugada, turno_1)
        if valor == 0:
            turno_1 = not turno_1
            turno += 1
            ganador_resultado = ganador(tablero)
            if ganador_resultado == 1:
                imprimir_tablero(tablero)
                print(f"{jugador_1} ha ganado, ¡felicitaciones!")
                print("La computadora ha perdido, será la próxima.")
                break
            elif ganador_resultado == 2:
                imprimir_tablero(tablero)
                print("La computadora ha ganado, ¡inténtalo de nuevo!")
                print(f"{jugador_1} ha perdido.")
                break
        else:
            print(valor)
        if turno == 9:
            imprimir_tablero(tablero)
            print("Empate...")

def jugar_versus():
    turno_1 = True
    jugador_1 = input("Ingrese el nombre del jugador 1 (x): ")
    jugador_2 = input("Ingrese el nombre del jugador 2 (o): ")
    turno = 0

    tablero = [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
    ]

    while turno < 9:
        imprimir_tablero(tablero)
        if turno_1:
            print(f"{jugador_1}, elige una posición por favor:")
        else:
            print(f"{jugador_2}, elige una posición por favor:")

        jugada = int(input())
        valor = cambiar_tablero(tablero, jugada, turno_1)
        if valor == 0:
            turno_1 = not turno_1
            turno += 1
            ganador_resultado = ganador(tablero)
            if ganador_resultado == 1:
                imprimir_tablero(tablero)
                print(f"{jugador_1} ha ganado, ¡felicitaciones!")
                print(f"{jugador_2} ha perdido, será la próxima.")
                break
            elif ganador_resultado == 2:
                imprimir_tablero(tablero)
                print(f"{jugador_2} ha ganado, ¡felicitaciones!")
                print(f"{jugador_1} ha perdido, sigue intentando.")
                break
        else:
            print(valor)
        if turno == 9:
            imprimir_tablero(tablero)
            print("Empate...")

def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo = 'x'
    else:
        simbolo = 'o'

    posiciones = {
        1: (0, 0), 2: (0, 2), 3: (0, 4),
        4: (2, 0), 5: (2, 2), 6: (2, 4),
        7: (4, 0), 8: (4, 2), 9: (4, 4)
    }

    if posicion in posiciones:
        fila, columna = posiciones[posicion]
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada.'
    else:
        return 'Esa posición no existe.'

def ganador(tablero):
    for simbolo in ['x', 'o']:
        fila_0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo
        fila_2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
        fila_4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
        columna_0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero[4][0] == simbolo
        columna_2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero[4][2] == simbolo
        columna_4 = tablero[0][4] == simbolo and tablero[2][4] == simbolo and tablero[4][4] == simbolo
        diagonal_abajo = tablero[0][0] == simbolo and tablero[2][2] == simbolo and tablero[4][4] == simbolo
        diagonal_arriba = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo

        if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_abajo or diagonal_arriba:
            return 1 if simbolo == 'x' else 2

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "a":
            jugar_contra_computadora()
        elif opcion == "b":
            jugar_versus()
        elif opcion == "c":
            print("Salir del menú")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
