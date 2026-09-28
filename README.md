# Ajuste de Recta y Predicción Interactiva con Streamlit

Aplicación web en Python que lee un archivo `.csv` con dos puntos, calcula la recta que pasa por ellos, la grafica junto a los puntos originales y genera una tabla de valores interpolados y de predicción.

## Información del alumno

- **Nombre:** Lopez Angulo Marco Adel
- **Matrícula:** 2403230096
- **Asignatura:** Ciencia de Datos
- **Cuatrimestre:** 7mo

## Contexto matemático

Dados dos puntos P1(x1, y1) y P2(x2, y2) con x1 ≠ x2:

```
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1
y = m * x + b
```

- `m` es la pendiente y `b` la ordenada al origen.
- Con la recta se interpolan los valores enteros entre x1 y x2, y se predicen valores posteriores (extrapolación).

## Estructura del proyecto

```
.
├── app.py             # Interfaz en Streamlit
├── recta.py           # Lógica numérica y de datos (sin Streamlit)
├── pruebas_csv/       # Archivos CSV para probar las validaciones
├── requirements.txt   # Dependencias
└── README.md
```

### `recta.py`

| Función | Responsabilidad |
|---|---|
| `validar_filas_csv` | Comprueba que el archivo tenga exactamente 2 filas |
| `validar_columnas_csv` | Comprueba que existan las columnas `x` e `y` |
| `validar_numericos_csv` | Comprueba que no haya celdas vacías ni texto en `x` e `y` |
| `cargar_csv` | Lee el archivo con pandas y aplica las tres validaciones |
| `extraer_coordenadas` | Obtiene `(x_1, y_1, x_2, y_2)` del DataFrame validado |
| `calculo_recta` | Calcula `m` y `b` (lanza `ValueError` si x1 = x2) |
| `generar_rango_x` | Genera los enteros entre los dos puntos más los valores de extrapolación |
| `generar_tabla` | Construye el DataFrame con las columnas `x` e `y proyectado` |
| `generar_grafica` | Devuelve la figura de Matplotlib con los puntos y la recta |

Todas las validaciones lanzan `ValueError` con un mensaje claro, que `app.py` atrapa y muestra en pantalla.

### `app.py`

Contiene únicamente la interfaz: carga del archivo, selección de la cantidad de valores a predecir, mensajes de error, métricas de `m` y `b`, tabla y gráfica.

## Formato del archivo CSV

Debe contener exactamente dos filas y las columnas `x` e `y`, con valores numéricos:

```
x,y
1,3
8,14
```

## Instalación

```bash
pip install -r requirements.txt
```

Librerías utilizadas: `streamlit`, `pandas`, `numpy`, `matplotlib`.

## Ejecución

```bash
streamlit run app.py
```

## Pruebas

La carpeta `pruebas_csv/` contiene archivos para verificar cada validación:

- **Válidos:** puntos normales, invertidos, con decimales y con negativos.
- **Con error:** tres filas, una fila, sin encabezado, columna con otro nombre, separador distinto de coma, texto en `x`, celda vacía, archivo vacío y dos puntos con la misma `x`.

Cada archivo con error rompe una sola regla, para confirmar que la aplicación muestra el mensaje correspondiente y no un error de Python.

## Bitácora de desarrollo

- Función `calculo_recta` con validación de x iguales.
- Carga del CSV con pandas y validaciones de filas, columnas y valores numéricos.
- Extracción de coordenadas y cálculo de `m` y `b`.
- Interfaz en Streamlit con métricas y manejo de errores.
- Tabla de interpolación y predicción, y gráfica con Matplotlib.
- Archivos CSV de prueba para las validaciones.