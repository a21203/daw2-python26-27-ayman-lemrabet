#vasmos a usar encapsulacion, conviertiendo metodos de atributos
class Circulo2():
    def __init__(self, radio):
        self.radio = radio #es como el setter pero directam.

        """voy a convertir un metodo en atributo
        usamos rl decorador @property"""
    @property
    def radio(self):
        return self.radio
    #usamos radio.setter para asignar el valoir
    @radio.setter
    def radio(self, radio):
        if radio >=0:
            self.radio = radio
        else:
            raise ValueError("Radio debe ser positivo.")
            self._radio = 0

    @radio.deleter
    def radio(self):
        del self._radio



    c1 = Circulo2(5)
    #accedemos al atributo pero en realidad a traves del metodo
    print(c1.radio)
    c1.radio = 8
    del c1.radio