class circulo():
    def __init__(self, radio):
        self.set_radio(radio)

    def set_radio(self, radio) : {_ge_}:
     if (radio >= 0):
         self.radio = set_radio
     else:
         self._radio=0
         raise ValueError("Radio debe ser positivo.")
     def get_radio(self):
         print("Estoy devolviendo el valor del radio")
         return self._radio


     circ1= circulo(10)
    print(circ1.get_radio())
     circ2=circulo(20)