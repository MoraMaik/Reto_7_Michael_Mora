# Inicialización de variables
poblacion_a = 25e6  # 25 millones de habitantes
poblacion_b = 18.9e6  # 18.9 millones de habitantes
tasa_crecimiento_a = 0.02  # Tasa de crecimiento anual del 2%
tasa_crecimiento_b = 0.03  # Tasa de crecimiento anual del 3%
ano_actual = 2022  # Año de inicio

# Ciclo while para calcular el año en que la población de B supera a la de A
while poblacion_b <= poblacion_a:
    # Actualización de poblaciones según las tasas de crecimiento
    poblacion_a += poblacion_a * tasa_crecimiento_a
    poblacion_b += poblacion_b * tasa_crecimiento_b
    # Incremento del año
    ano_actual += 1

# Imprimir el año en que la población de B supera a la de A
print(f"En el año {ano_actual}, la población del país B superará a la de A.")
