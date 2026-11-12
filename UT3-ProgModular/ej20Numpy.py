



#generar un matriz con valores del 1 al 10
mat = np.arange(1,10).reshape((3,3))
print("mat=\n", mat)
#acceder a una celda
print("fila2, columna2 es: ", mat[1,1])
#acceder a una fila
print("fila2 es: ", mat[1,:])
#acceder a una columna
print("Col 3 es: \n", mat[:,2:3])
#aplicar filtros
print("los mayores de 5 son:",mat[mat>5])
#la media aplicada a matrices
print("",np.mean(mat))
#media de las filas
print("Media filas:"; np.mean(mat axis))