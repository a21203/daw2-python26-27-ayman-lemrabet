#programa que lee el precio de venta original y el precio final
num1 = float(input("Dime el precio original: "))
num2 = float(input("Dime el precio final: "))
descuento = (num1-num2)/num2
print((float(num2) * 100) / float(num1))
