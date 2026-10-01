#programa que pide dos numeros a y b e indica sila suma es positiva negativa o cero
num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))

if num1+num2 >=0:
    print("Suma positiva")
elif num1+num2 < 0:
    print("Suma negativa")
else:
    print("La suma es cero")
    