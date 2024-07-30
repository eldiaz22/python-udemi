class Vehiculo:
    def __init__(self,color,ruedas) :
        self.color = color
        self.ruedas = ruedas

    def __str__(self) :
        return f'Color: {self.color}, Ruedas: {self.ruedas}'
    
    
    
class bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo}"
        
        
class auto(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return f"{super().__str__()} velocidad: {self.velocidad} km"