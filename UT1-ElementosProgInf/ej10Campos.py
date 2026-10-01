#sabiendo que un campo de futbol de largo esta entre 90 y 120m
#y de ancho entre 45 y 90
#Escribre un programa que piede al usuario
#1-superficio en metros cuadrados (entre 1 y 99999)
#2. Un numero q es la estimacion de cuantas campos de futbol son
#Devulve verdado o falso si existen campos de futbol validos para es estimacion

def estimacion_es_correcta(superficie, estimacion):
    if superficie <= 0 or superficie >= 100000:
        return False

    if estimacion <= 0 or estimacion >= 100000:
        return False

    superficie_minima = 90 * 45
    superficie_maxima = 120 * 90

    minimo_total = superficie_minima * estimacion
    maximo_total = superficie_maxima * estimacion

    if minimo_total <= superficie <= maximo_total:
        return True
    else:
        return False


superficie = int(input("Introduce la superficie: "))
estimacion = int(input("Introduce el número de campos: "))

resultado = estimacion_es_correcta(superficie, estimacion)

print(resultado)