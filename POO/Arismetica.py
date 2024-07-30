class Arismetica:
    """
    CLASE ARISMETIC AAPRA REALIZAR LAS OPERACIONES DE SUMAR RESTAR 
    """
    def __init__(self,operando_a,operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b
        #metedos de las clases
    def sumar(self):
        return self.operando_a + self.operando_b     
    def restar(self):
        return self.operando_a - self.operando_b
    def multiplicar (self):
        return self.operando_a * self.operando_b
    def division(self):
        return self.operando_a / self.operando_b
    
    
    
arismetica1 = Arismetica(5,5)

print(arismetica1.sumar())



division1 = Arismetica(45,4)
print(f"su division fue {division1.division():.1f}")
