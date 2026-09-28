
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def validar_filas_csv(datos):
    """
    Valida que el DataFrame contenga exactamente dos filas para el cálculo.

    Lanza ValueError si la cantidad de filas es distinta de dos.

    Parámetros:
        datos (pandas.DataFrame): Datos cargados desde el archivo CSV.

    Retorna:
        None
    """
    if len(datos) != 2:
        raise ValueError(
            f"El archivo debe tener 2 filas (se encontraron {len(datos)})."
        )


def validar_columnas_csv(datos):
    """
    Valida que el DataFrame contenga las columnas requeridas 'x' y 'y'.

    Lanza ValueError si falta alguna de las dos columnas necesarias.

    Parámetros:
        datos (pandas.DataFrame): Datos cargados desde el archivo CSV.

    Retorna:
        None
    """
    columnas_requeridas = {"x", "y"}

    if not columnas_requeridas.issubset(datos.columns):
        raise ValueError(
            "El archivo debe contener las columnas 'x' y 'y'. "
            f"Columnas encontradas: {list(datos.columns)}"
        )


def validar_numericos_csv(datos):
    """
    Valida que las columnas 'x' y 'y' contengan solo números no nulos.

    Lanza ValueError si existen celdas vacías o valores no numéricos.

    Parámetros:
        datos (pandas.DataFrame): Datos cargados desde el archivo CSV.

    Retorna:
        None
    """
    if datos[["x", "y"]].isna().any().any():
        raise ValueError(
            "El archivo contiene celdas vacías en las columnas 'x' o 'y'."
        )

    for columna in ["x", "y"]:
        if not pd.api.types.is_numeric_dtype(datos[columna]):
            raise ValueError(
                f"La columna '{columna}' contiene valores no numéricos "
                "(texto o caracteres inválidos)."
            )


def cargar_csv(origen_csv):
    """
    Carga y valida un archivo CSV con coordenadas para el cálculo de recta.

    Lee el archivo CSV y aplica las validaciones de filas, columnas y tipo
    de datos. Convierte errores técnicos de lectura en ValueError descriptivos.

    Parámetros:
        origen_csv (str o File-like object): Ruta del archivo CSV o buffer.

    Retorna:
        pandas.DataFrame: DataFrame validado con exactamente dos filas y
        las columnas 'x' y 'y'.

    Lanza:
        ValueError: Si el archivo está vacío, mal formado o no cumple las
        validaciones.
    """
    try:
        datos = pd.read_csv(origen_csv)

    except pd.errors.EmptyDataError:
        raise ValueError("El archivo CSV está completamente vacío.")

    except pd.errors.ParserError:
        raise ValueError(
            "El archivo CSV tiene un formato inválido o está dañado."
        )

    except Exception as e:
        raise ValueError(
            f"No se pudo leer el archivo CSV: {e}"
        ) from e

    validar_filas_csv(datos)
    validar_columnas_csv(datos)
    validar_numericos_csv(datos)

    return datos


def extraer_coordenadas(datos):
    """
    Extrae coordenadas de dos puntos desde un DataFrame previamente validado.

    Supone que el DataFrame proviene de cargar_csv(), por lo que ya contiene
    exactamente dos filas y las columnas 'x' y 'y'.

    Parámetros:
        datos (pandas.DataFrame): DataFrame validado.

    Retorna:
        tuple: (x_1, y_1, x_2, y_2) como valores float.
    """
    x_1 = float(datos.iloc[0]["x"])
    y_1 = float(datos.iloc[0]["y"])
    x_2 = float(datos.iloc[1]["x"])
    y_2 = float(datos.iloc[1]["y"])

    return x_1, y_1, x_2, y_2


def calculo_recta(x_1, y_1, x_2, y_2):
    """
    Calcula la pendiente (m) y la intersección con el eje y de una recta.

    Lanza ValueError si las coordenadas x son iguales (línea vertical).

    Parámetros:
        x_1, y_1: Coordenadas del primer punto.
        x_2, y_2: Coordenadas del segundo punto.

    Retorna:
        tuple: (m, b), donde m es la pendiente y b la ordenada al origen.
    """
    if x_1 == x_2:
        raise ValueError(
            "No se puede realizar el cálculo "
            "(x1 y x2 no pueden ser iguales)."
        )

    m = (y_2 - y_1) / (x_2 - x_1)
    b = y_1 - (m * x_1)

    return m, b


def generar_rango_x(x_1, x_2, extrapolacion):
    """
    Genera el rango entero de x para interpolación y extrapolación.

    El intervalo incluye únicamente los enteros comprendidos entre x_1 y
    x_2. Los valores extrapolados comienzan después del extremo mayor.

    Parámetros:
        x_1 (float): Coordenada x del primer punto.
        x_2 (float): Coordenada x del segundo punto.
        extrapolacion (int): Cantidad de valores posteriores a generar.

    Retorna:
        numpy.ndarray: Arreglo ordenado de valores enteros de x.

    Lanza:
        ValueError: Si extrapolacion es menor que 1.
    """
    if extrapolacion < 1:
        raise ValueError(
            "La extrapolación debe ser mayor o igual a 1."
        )

    inicio = math.ceil(min(x_1, x_2))
    fin = math.floor(max(x_1, x_2))

    return np.arange(inicio, fin + extrapolacion + 1)


def generar_tabla(x_1, x_2, m, b, extrapolacion=5):
    """
    Genera una tabla de interpolación y predicción extrapolada.

    Utiliza los enteros comprendidos entre los dos puntos y agrega
    valores posteriores calculados mediante la ecuación de la recta.

    Parámetros:
        x_1 (float): Coordenada x del primer punto.
        x_2 (float): Coordenada x del segundo punto.
        m (float): Pendiente de la recta.
        b (float): Ordenada al origen.
        extrapolacion (int): Cantidad de valores posteriores.

    Retorna:
        pandas.DataFrame: Tabla con las columnas x e y proyectado.
    """
    x = generar_rango_x(x_1, x_2, extrapolacion)
    y = (m * x) + b

    return pd.DataFrame({
        "x": x,
        "y proyectado": y
    })


def generar_grafica(x_1, y_1, x_2, y_2, m, b, extrapolacion=5):
    """
        Genera la gráfica de la recta y los puntos originales.

        Dibuja la recta desde el menor valor de x hasta el último valor
        extrapolado y representa P1 y P2 con marcadores individuales.

        Parámetros:
            x_1, y_1: Coordenadas del primer punto.
            x_2, y_2: Coordenadas del segundo punto.
            m (float): Pendiente de la recta.
            b (float): Ordenada al origen.
            extrapolacion (int): Cantidad de valores posteriores.

        Retorna:
            matplotlib.figure.Figure: Figura lista para mostrarse.
        """
    rango = generar_rango_x(x_1, x_2, extrapolacion)

    x_inicio = min(x_1, x_2)
    x_fin = rango[-1]

    x_linea = np.linspace(x_inicio, x_fin, 200)
    y_linea = (m * x_linea) + b

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
            x_linea, y_linea,
            color="blue",
            linewidth=2,
            label=f"y = {m:.2f}x + {b:.2f}"
        )

    ax.scatter(
            x_1, y_1,
            color="red",
            s=70,
            zorder=3,
            label=f"P1 ({x_1:g}, {y_1:g})"
        )

    ax.scatter(
            x_2, y_2,
            color="green",
            s=70,
            zorder=3,
            label=f"P2 ({x_2:g}, {y_2:g})"
        )

    ax.set_title("Recta ajustada")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()

    return fig