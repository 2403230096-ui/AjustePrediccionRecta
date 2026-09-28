
import pandas as pd


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