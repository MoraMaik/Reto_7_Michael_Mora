# Inicializar los límites inferior y superior del rango de números.
limite_inferior = 1
limite_superior = 100

# Iniciar el ciclo de adivinación.
while True:
    # Calcular el punto medio como nuestro próximo número a adivinar.
    intento = (limite_inferior + limite_superior) // 2
    
    # Preguntar al usuario sobre el intento.
    respuesta = input(f"¿El número es {intento}? (responde 'mayor', 'menor', 'igual'): ").lower()
    
    # Ajustar el rango basado en la respuesta.
    if respuesta == "mayor":
        limite_inferior = intento + 1
    elif respuesta == "menor":
        limite_superior = intento - 1
    elif respuesta == "igual":
        print(f"¡Adiviné! Tu número es {intento}.")
        break
    else:
        print("Respuesta no válida. Por favor, responde 'mayor', 'menor' o 'igual'.")
    
    # Si se cruzan los límites, significa que ha habido un error en las respuestas dadas.
    if limite_inferior > limite_superior:
        print("Parece que ha habido un error en las respuestas. No se puede adivinar bajo estas condiciones.")
        break
