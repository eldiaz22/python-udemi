class Volumen_cubo:
    def __init__(self, ancho,profundo,alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto
    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundo
    
    