import numpy as np #importar libreria

#Se define una cuadrícula de Sudoku en forma de lista bidimensional.
grid = [[8,0,0,0,0,7,0,9,0],
        [0,2,9,0,0,4,0,0,6],
        [3,0,0,2,0,0,0,0,0],
        [0,0,0,0,0,6,5,0,0],
        [0,1,7,4,0,0,0,3,0],
        [2,0,0,0,0,0,0,0,0],
        [0,9,4,1,0,0,0,7,0],
        [0,0,8,0,0,0,0,0,0],
        [0,0,0,0,7,0,0,0,3]]

#Esta función comprueba si es posible colocar un número en una posición específica del tablero de Sudoku. Verifica si el número ya está presente en la fila, columna o cuadrado 3x3 correspondiente.
def possible(row, column, number):
    global grid
    # ¿Aparece el número en la fila dada?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    # ¿Aparece el número en la columna dada?
    for i in range(0,9):
        if grid[i][column] == number:
            return False

    # ¿Aparece el número en el cuadrado dado?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

#Esta función imprime el tablero de Sudoku en formato de texto.
def print_sudoku():
   for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if row[j] == 0:
                print(". ", end="")
            else:
                print(f"{row[j]} ", end="")
        print()

#Esta función resuelve el Sudoku utilizando el algoritmo de backtracking.
"""
Comienza recorriendo cada celda del tablero de izquierda a derecha, de arriba a abajo.
Si encuentra una celda vacía, prueba todos los números del 1 al 9 en esa celda utilizando la función possible().
Si encuentra un número válido, lo coloca en la celda y llama recursivamente a solve() para continuar probando el siguiente número.
Si solve() encuentra una solución, imprime el tablero resultante.
"""
def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number

                        solve()
                        grid[row][column] = 0

                return
    print_sudoku()

    #print(np.matrix(grid))
    #input('Generar otra posible solución (presione Enter para salir)')



#se imprime el tablero original
print_sudoku()
print("="*30)

#se manda a llamar a la función solve
solve()