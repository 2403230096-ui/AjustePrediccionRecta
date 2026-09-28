### Nombre:     Lopez Angulo Marco Adel
### Matricula:  2403230096
### Asignatura: Ciencia de Datos
### Fecha:      09/27/2026
"""
Módulo de prueba y consumo para la función calculo_recta.

Este script lee coordenadas desde un archivo CSV ('CalculoRecta.csv'),
extrae los primeros dos puntos y ejecuta pruebas de cálculo de pendiente (m)
e intersección en y (b) utilizando el módulo 'recta'.

Funcionalidades:
    - Lectura de datos desde archivo CSV con pandas.
    - Ejecución de pruebas con datos del CSV y datos hardcodeados.
    - Captura y manejo de excepciones (ValueError) para casos de líneas verticales.

Dependencias:
    - pandas
    - recta.calculo_recta

Archivos requeridos:
    - CalculoRecta.csv (debe contener al menos dos filas con columnas 'x' y 'y')
"""
from prueba_recta import calculo_recta
import pandas as pd

def probar_puntos(x_1, y_1, x_2, y_2):
    """
    Ejecuta el cálculo de la recta entre dos puntos.

    Parámetros:
        x_1 (float/int): Coordenada x del primer punto.
        y_1 (float/int): Coordenada y del primer punto.
        x_2 (float/int): Coordenada x del segundo punto.
        y_2 (float/int): Coordenada y del segundo punto.
    """
    try:
        m, b = calculo_recta(x_1, y_1, x_2, y_2)
        print(f"Puntos ({x_1}, {y_1}) y ({x_2}, {y_2}) -> m = {m}, b = {b}")
    except ValueError as e:
        print(f"Puntos ({x_1}, {y_1} y {x_2}, {y_2} -> Error: {e})")


if __name__ == "__main__":

    datos = pd.read_csv("calculo_recta.csv")

    x1 = datos["x"].iloc[0]
    y1 = datos["y"].iloc[0]
    x2 = datos["x"].iloc[1]
    y2 = datos["y"].iloc[1]

    probar_puntos(x1, y1, x2, y2)
    probar_puntos(1, 3, 8, 14)
    probar_puntos(2, 3, 2, 9)