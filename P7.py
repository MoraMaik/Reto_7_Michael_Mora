# Solicitar al usuario que ingrese un número entre 2 y 50
numero = int(input("Ingrese un número entre 2 y 50: "))

# Verificar que el número esté en el rango permitido
if numero < 2 or numero > 50:
    print("El número ingresado no está en el rango permitido.")
else:
    print(f"Divisores de {numero}:")
    # Utilizar un ciclo for para encontrar los divisores del número
    for divisor in range(1, numero + 1):
        # Si el número es divisible por divisor, imprimirlo
        if numero % divisor == 0:
            print(divisor)
