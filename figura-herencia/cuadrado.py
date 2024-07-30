from color import Color 
from figura import Figura_geometrica

class Cuadrado(Figura_geometrica,Color):
    def __init__(self, lado ,color):
        #super().__init__(lado)
        Figura_geometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
        
    def calcular_area(self):
        return self.alto * self.ancho