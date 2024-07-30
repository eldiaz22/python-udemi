class Persona : 
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def __str__(self) :
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}"
    
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad,sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo
    def __str__(self):
            return f"{super().__str__()} sueldo: {self.sueldo}"