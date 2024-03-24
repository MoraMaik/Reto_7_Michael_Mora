# Inicializamos las variables
numero = 1
imprimir_impares = True  # Bandera para controlar cuándo imprimir números impares

# Usamos un ciclo while que se ejecuta mientras el número sea menor o igual a 1000
while numero <= 1000:
    if imprimir_impares:
        # Imprime el número si es impar
        if numero % 2 != 0:
            print(numero)
        # Cambia la bandera para empezar a imprimir pares cuando llegamos a 999
        if numero == 999:
            imprimir_impares = False
    else:
        # Imprime el número si es par
        if numero % 2 == 0:
            print(numero)
    
    # Incrementamos el número para la próxima iteración
    numero += 1
