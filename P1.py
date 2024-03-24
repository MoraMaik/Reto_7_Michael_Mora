# Inicializamos una bandera y un contador
continuar = True
numero = 1

# Usamos un ciclo while que se ejecuta mientras la bandera sea True
while continuar:
    # Imprime el número y su cuadrado
    print(f"{numero} - {numero**2}")
    
    # Incrementamos el número para la próxima iteración
    numero += 1
    
    # Verificamos si debemos detener el ciclo
    if numero > 100:
        continuar = False
