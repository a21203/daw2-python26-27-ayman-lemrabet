def validar_edad(edad):
    if not isinstance(edad, int):
        print("debe ser un numero")
        raise TypeError("La edad debe ser un numero natural")
    #validamos que la edad este entre 1 y 100
    if not 1 < edad < 100:
        raise ValueError("La edad debe ser un numero natural")
    return edad
try:
    mi_edad = validar_edad("30asdf")
    mi_edad_validada = validar_edad(mi_edad)
except TypeError as e:
    print(f"Error al validar la edad: {e}")
