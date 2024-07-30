class Persona : 
    def __init__(self):
        self.nombre ="Junior"
        self.apellido = "diaz"
        self.edad = 18



persona2 = Persona()

print(persona2.nombre)

class Persona : 
    def __init__(self,nombre,apellido,edad,*tuplas ,**dicionario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tuplas = tuplas
        self.dicionario = dicionario