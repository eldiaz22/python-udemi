class Area :
    def __init__(self,base,altura) :
        self.base = base
        self.altura = altura        
    def calcular_area(self):
        return self.base * self.altura
    
    
    
base = int(input("Ingrese la base del Triangulo"))
altura = int(input("ingrese la altura"))


triangulo_area = Area(base,altura)
print(f"LA AREA DEL TRIANGULO FUE: {triangulo_area.calcular_area()}")


