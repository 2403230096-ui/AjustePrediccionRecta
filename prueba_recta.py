### Nombre:     Lopez Angulo Marco Adel
### Matricula:  2403230096
### Asignatura: Ciencia de Datos
### Fecha:      09/27/2026

import pandas as pd

datos = pd.read_csv("calculo_recta.csv")

x1 = datos["x"].iloc[0]
y1 = datos["y"].iloc[0]
x2 = datos["x"].iloc[1]
y2 = datos["y"].iloc[1]


def calculo_recta(x_1, y_1, x_2, y_2):
    """
    Calcula la pendiente (m) y la intersección con el eje y (b) de una recta.

    Lanza ValueError si las coordenadas x son iguales (linea vertical).

    Parámetros:
        x_1, y_1: Coordenadas del primer punto.
        x_2, y_2: Coordenadas del segundo punto.

    Retorna:
        tuple: (m, b) donde m es la pendiente y b el origen.
    """
    if x_1 == x_2:
        raise ValueError("No realizar el calculo (x1 y x2 no pueden ser iguales).")
    m = (y_2 - y_1) / (x_2 - x_1)
    b = y_1 - (m * x_1)
    return m, b

