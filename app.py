### Nombre:     Lopez Angulo Marco Adel
### Matricula:  2403230096
### Asignatura: Ciencia de Datos
### Fecha:      09/27/2026

from recta import calculo_recta

m, b = calculo_recta(1, 3, 8, 14)
print(f"Pendiente (m): {m}")
print(f"Origen en y (b): {b}")

def probar_puntos(x_1, y_1, x_2, y_2):
    try: 
        m,b = calculo_recta(x_1, y_1, x_2, y_2)
        print(f"Puntos ({x_1}, {y_1} y {x_2}, {y_2} -> m = {m}, b = {b})")
    except ValueError as e:
        print(f"Puntos ({x_1}, {y_1} y {x_2}, {y_2} -> Error: {e}")

probar_puntos(1, 3, 8, 14)
probar_puntos(2,3,2,9)