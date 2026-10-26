def saludar(nombre : str="pepe", **kwargs)
    cadena = nombre
    for valor in kwargs.values():
        cadena=cadena+" "+valor
    return "hola "+cadena
#parametro **kwargs

print(saludar())
print(saludar(nombre="pepe"))
print(saludar(nombre="joaquin"))
print(saludar(nombre="pepe", nombre2="juan", nombre3="alicia"))
