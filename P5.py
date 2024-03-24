# Solicitar al usuario que ingrese un número natural n
n = int(input("Ingrese un número natural n para calcular su factorial: "))

# Inicializar la variable factorial
factorial = 1

# Verificar si el número es negativo, cero o positivo
if n < 0:
    print("El factorial no se define para números negativos.")
else:
    # Calcular el factorial usando un ciclo while
    numero_actual = n
    while numero_actual > 1:
        factorial *= numero_actual
        numero_actual -= 1

    # Imprimir el resultado
    print(f"El factorial de {n} es {factorial}.")
