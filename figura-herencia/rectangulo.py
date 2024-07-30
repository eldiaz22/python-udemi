from figura import Figura_geometrica
from color import Color 

class Rectangulo(Figura_geometrica,Color):
    def __init__ (self, ancho, alto, color):
        Figura_geometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    def calcular_area (self):
        return self.alto * self.ancho
    def __str__(self) :
        return f"{Figura_geometrica.__str__()}{Color.__str__()}"
    