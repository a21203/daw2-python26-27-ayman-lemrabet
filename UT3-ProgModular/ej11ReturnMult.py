#en python una funcion puede devolver varias valores
def operar(n1 :{__add__,__sub__,__mul__},n2):
    return n1+n2, n1-n2, n1*n2

suma, resta, producto = operar(n1:12,n2:5)
print(suma)
print(resta)
print(producto)