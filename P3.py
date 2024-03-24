# Solicitamos al usuario que ingrese un número natural n.
n = int(input("Ingrese un número natural n (n ≥ 2): "))

# Verificamos si n cumple con la condición de ser mayor o igual a 2.
if n < 2:
    print("El número ingresado no cumple con la condición (n ≥ 2).")
else:
    # Ajustamos n al número par más cercano menor o igual a n.
    if n % 2 != 0:
        n -= 1
    
    # Utilizamos una bandera para controlar el ciclo while.
    continuar = True

    # Iniciamos el ciclo while.
    while continuar:
        print(n)
        
        # Decrementamos n en 2 para obtener el próximo número par descendente.
        n -= 2
        
        # Si n es menor que 2, cambiamos la bandera para detener el ciclo.
        if n < 2:
            continuar = False
