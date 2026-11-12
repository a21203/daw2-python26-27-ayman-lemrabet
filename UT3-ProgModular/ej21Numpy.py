import numpy as np
#leenos el archivo csv con los datos
#ña cargamos a una matriz y quito la primera fila
iris = np.load('./iris.csv', skiprows=1, delimiter=',',)
print("Matriz de datos de iris: \n",iris.shape)
print("5 primeras filas: \n",iris[:5,: ])
#media de esas filas
print("5 primeras filas: \n", np.mean(iris[:5,:])
#media por columna
print("Media por columna:\n",np.mean(iris, axis=0))
#dime cada caracteristica el valor minimo (min)


#dime las filas que tienen un largo de petalo mayor a 5.0


#De las filas 50 a 99, muestra solo largo y ancho del petlo