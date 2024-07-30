class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __add__(self,other):
        return  self.nombre + other.nombre
    
    def __sub__(self,otro):
        return self.edad - otro.edad

    
    
persona1= Persona("carlos", 60)
persona2 = Persona("pepe", 50)

print(persona1  + persona2)
print(persona1 - persona2)