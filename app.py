### Nombre:     Lopez Angulo Marco Adel
### Matricula:  2403230096
### Asignatura: Ciencia de Datos
### Fecha:      09/27/2026

import streamlit as st
from recta import (
    cargar_csv,
    extraer_coordenadas,
    calculo_recta,
    generar_tabla,
    generar_grafica
)

st.title("Cálculo de la ecuación de una recta")

archivo = st.file_uploader(
    "Selecciona un archivo CSV",
    type=["csv"]
)

if archivo is not None:
    try:
        datos = cargar_csv(archivo)

        coordenadas = extraer_coordenadas(datos)
        x_1, y_1, x_2, y_2 = coordenadas

        m, b = calculo_recta(*coordenadas)

        st.success("Cálculo realizado correctamente")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pendiente (m)", f"{m:.4f}")
        with col2:
            st.metric("Ordenada al origen (b)", f"{b:.4f}")

        st.subheader("Tabla de interpolación y predicción")

        tabla = generar_tabla(x_1, x_2, m, b)

        st.dataframe(
            tabla.style.format({
                "y proyectado": "{:.2f}"
            }),
            use_container_width=True
        )

        st.subheader("Visualización gráfica")

        figura = generar_grafica(
            x_1, y_1, x_2, y_2, m, b
        )

        st.pyplot(figura)

    except ValueError as e:
        st.error(str(e))