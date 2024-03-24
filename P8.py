# Definir la función que verifica si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

# Inicializar el número de inicio
numero = 1

# Utilizar un ciclo while para iterar a través de los números del 1 al 100
while numero <= 100:
    if es_primo(numero):
        print(numero)
    numero += 1
