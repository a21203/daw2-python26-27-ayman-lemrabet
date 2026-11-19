#vamos a crear la pimera clase, en MAY
class Clase()
    #atributos de la clase
    at_clase=1
    #defina un metodo que usa el atributo
    def metodo(self):
        #y este metodo tiene un atributo del objeto (no de la clase)
        self._objeto=3

 #crea un objeto de esta clase
 objeto = Clase()
#es del tipo
print(type(objeto))
#para ver el valor del atributo de la clase
print(objeto.at_clase)
#accesso al objeto
#llama al metodo para cree el valor
objeto.metodo()
print(