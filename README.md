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

Con la recta calculada se interpolan valores entre x1 y x2, y se predicen valores para x > x2.

## Estructura del proyecto

```
.
├── app.py             # Interfaz en Streamlit
├── recta.py           # Lógica numérica (sin Streamlit)
├── puntos.csv         # Archivo de ejemplo
└── requirements.txt   # Dependencias
```

- **`recta.py`**: funciones de cálculo de `m` y `b` (con validación cuando x1 = x2), lectura y validación del CSV, y generación de la tabla.
- **`app.py`**: carga del archivo, mensajes de error y despliegue de resultados, gráfica y tabla.

## Formato del archivo CSV

Debe contener exactamente dos filas y las columnas `x` e `y`:

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

## Notas

- Si los dos puntos tienen la misma coordenada x, la aplicación muestra un aviso, porque no se puede calcular la pendiente.
- La lógica de cálculo está separada de la interfaz para poder reutilizarla y probarla por separado.

## Bitácora de desarrollo

- Función `calculo_recta` con validación de x iguales.
- Pruebas del cálculo con casos normales y de error.