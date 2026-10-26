def factorial(n: (__lt__, __eq__, __mul__, __sub__)):
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Resultado: 120