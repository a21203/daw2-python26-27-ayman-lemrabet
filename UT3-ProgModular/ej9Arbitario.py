#funciones con parametros obligatorios y opcionales
#n primer argumrnto obligatorio y a partit de ahi argumentos adicionales
def sumar (n, *args):
    resultado = n
    for i in args:
        resultado += i
        return resultado

print(sumar(n:2,*args: 3))
print(sumar(n:3,*args4,5,6,7))
lista = [1,2,3,4,5,6,7,8]
print(sumar(*lista))