import math
class Punto():
    """ Representacion de un punto en el plano x,y"""
def __init__(self,x:int=0,y:int=0):
        self.x = x
        self.y = y
def distancia(self, otroPuntoQueMeDigan):
    dx = self.x - otroPuntoQueMeDigan
    dy = self.y - otroPuntoQueMeDigan



#declaro una variable objeto que sea el tipo Pur
punto1= Punto()
print(punto2.x, punto2.y)
punto2 = Punto(x:18, y:29)
print(punto2.x, punto2.y)
print(punto1.distancia(punto2))