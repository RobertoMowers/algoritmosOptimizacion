import random
import tkinter as tk

class JuegoDeLaVida:
    def __init__(self, t_size, canvas):
        self.t_size = t_size
        self.celdas = []
        self.canvas = canvas
        self.celdas_canvas = []  # Almacena los identificadores de las celdas en el lienzo

        self.generarEcosistema()
        self.updateEcosistema()

    def nuevaGeneracion(self):
        new_celdas = []

        for i, fila in enumerate(self.celdas):
            new_filas = []
            for j, celda in enumerate(fila):
                vecinos = self.contadorVecinas(i, j)
                new_state = self.reglasJuegoVida(celda, vecinos)
                new_filas.append(new_state)
            new_celdas.append(new_filas)

        self.celdas = new_celdas
        self.updateView()

    def contadorVecinas(self, i, j):
        vecinas = {'arriba': (1, 0), 'abajo': (-1, 0), 'izq': (0, -1), 'der': (0, 1)}
        no_vecinas = 0

        for key, value in vecinas.items():
            new_i, new_j = i + value[0], j + value[1]
            if (0 <= new_i < len(self.celdas)) and (0 <= new_j < len(self.celdas[0])):
                if self.celdas[new_i][new_j] == 1:
                    no_vecinas += 1

        return no_vecinas

    def generarEcosistema(self):
        for i in range(self.t_size):
            fila = []
            fila_canvas = []  # Almacena los identificadores de las celdas en el lienzo
            for j in range(self.t_size):
                estado = random.choice([0, 1])  # 0 para muerto, 1 para vivo
                color = "green" if estado else "white"
                celda = self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color,
                                                     outline="black")
                fila.append(estado)
                fila_canvas.append(celda)
            self.celdas.append(fila)
            self.celdas_canvas.append(fila_canvas)

    def updateEcosistema(self):
        self.nuevaGeneracion()
        self.canvas.after(1000, self.updateEcosistema)

    def reglasJuegoVida(self, state, vecinos):
        if state == 0 and vecinos == 3:
            return 1
        elif state == 1 and 4 > vecinos > 1:
            return 1
        elif state == 1 and (2 > vecinos or vecinos > 3):
            return 0
        else:
            return state

    def updateView(self):
        for i in range(self.t_size):
            for j in range(self.t_size):
                color = "green" if self.celdas[i][j] else "white"
                self.canvas.itemconfig(self.celdas_canvas[i][j], fill=color)

t_size = 9
ventana = tk.Tk()
ventana.title("Juego de la Vida")
canvas = tk.Canvas(ventana, width=t_size * 30, height=t_size * 30)
canvas.pack()

juego = JuegoDeLaVida(t_size, canvas)
ventana.mainloop()
