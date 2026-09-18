# primera clase en python

edad = 23

if edad >= 18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")

num = 3

if num >= 0:
    while num < 10:
        print(num)
        num += 1

    print("num final", num)

edad = 15
print(edad)

# variables de tipo booleano
azul = True

if azul:
    print("el cielo es azul")

# las expresiones entre parentesis, llaves o corchetes pueden ocupar varias lineas
dias = ['lunes', 'martes', 'miercoles',
        'jueves', 'viernes', 'sabado', 'domingo']

print("los dias son: ", dias)