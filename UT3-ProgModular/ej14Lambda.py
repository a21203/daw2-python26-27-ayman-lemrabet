# Funciones Lambda, funciones pequeñas que se definen en una línea

# Forma clásica de definir una función
def cuadrado_orig(x):
    return x**2


# La misma función utilizando lambda
cuadrado = lambda x: x**2

print(cuadrado(2))

# Lambda utilizada directamente
print((lambda x: x**2)(3))

# Lambda para saludar
print((lambda nombre: "Hola " + nombre)("Federico"))

saludar = lambda nombre: "Hola " + nombre

# Lambda con dos parámetros
suma = lambda a, b: a + b

print(suma(2, 3))


# Lista de tuplas con números y textos
pares = [
    (1, "uno"),
    (2, "dos"),
    (3, "tres"),
    (4, "cuatro"),
    (5, "cinco")
]

# Ordena por el valor de key
# pair[1] devuelve el segundo elemento (el texto)
pares.sort(key=lambda pair: pair[1])

print(pares)