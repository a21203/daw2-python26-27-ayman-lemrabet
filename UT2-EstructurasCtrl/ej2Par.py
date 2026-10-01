#ej2Par lee un numero y dice si es par o impar
try:
    num = int(input("Numero"))
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Debes introducir un numero")
