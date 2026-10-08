try:
  #gestion de errores
  numero1 = int(input("Ingrese un numero: "))
  numero2 = int(input("Ingrese un numero: "))
  resultado = numero1 / numero2
  print(f"El resultado es: {resultado}")
except ValueError:
    print("Error debe ser un numero")
    #Mostrar informacion del error:
    print(type(error))
    print(error.args)
    print(error)
except ZeroDivisionError:
    print("Error debe ser un numero distinto de 0")
except Exception as e: #cpatura cualquier excpcion no espicificada
   print(f"ocurrio un error inesperado{e}")
finally: #se ejecuta..
   print("Texto que va en el finally")

else: #el bloque else de un try solo se ejecuta si no se produce ninguna excepcion
    print("Programa terminado sin errores")