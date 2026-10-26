# La modifica y la devuelve
# Recibe una función y devuelve una nueva llamada envoltura

def tablas(funcion):
    # Función envoltura
    # 1- Imprime una cabecera
    # 2- Ejecuta la función
    # 3- Imprime línea de cierre

    def envoltura(tabla: int = 1):
        print("Tabla del %i:" % tabla)
        print('-' * 15)  # Imprimir 15 -

        for numero in range(0, 11):
            funcion(numero, tabla)

        print('-' * 15)  # Imprimir 15 -

    return envoltura


# Los decoradores se escriben con @
# Se crea la función suma, se pasa como argumento a tablas
# tablas devuelve envoltura

@tablas
def suma(numero, tabla: int = 1):
    print('%2i + %2i = %3i' % (tabla, numero, tabla + numero))


suma(3)