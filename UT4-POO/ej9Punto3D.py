#uso de herencia
import math


class Punto():

    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, valor):
            self._x = valor
        @property
        def y(self):
            return self._y
        @x.setter
        def y(self, valor):
            self._y = valor
        def __str__(self):
            return "{0}:{1}".format(self.x, self.y)
        def distancia(self, otroPunto):
            dx = self.x - otroPunto.x
            dy = self.y - otroPunto.y
            return (dx*dx + dy*dy)**0.5

    class Punto3d:
        def __init__(self, x:int=0, y:int=0):
            #los valores x e y los inicializo en el padre
    super().__init__(x,y)
    @property
    def z(self):
        return self.z
    @z.setter
    def z(self, valor):
        self.z = valor

    def __str__(self):
        return super().__str__() + str(self.z)

    def distancia(self, otroPunto3D):
