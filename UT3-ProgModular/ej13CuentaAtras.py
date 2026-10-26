# Función recursiva que cuenta hacia atrás desde
# un número dado hasta 0

def cuenta_atras(n):
    if n < 0:
        raise ValueError("El número debe ser positivo")

    # Caso base
    if n == 0:
        print("Fin")
    else:
        print(n)
        cuenta_atras(n - 1)


cuenta_atras(9)
