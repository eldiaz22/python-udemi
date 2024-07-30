class Persona : 
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre  #_para indicar para no poder acceder sugerencia
        self.apellido = apellido
        self.edad = edad
    @property  # para obtener
    def nombre(self):
        return self._nombre
    @nombre.setter  #metodo set
    def nombre(self,nombre):
        self._nombre = nombre

    def detalle(self):
        print(f"detalle{self._nombre} {self.apellido} {self.edad}")
        
        
        
persona1 = Persona("carlos","diaz",15)
persona1._nombre = "diaz"  # nose debe hacer porque _ esto es una mala practica

#si no debe modificar puede hacer esto 

#persona1.nombre()

print(__name__)

if __name__ == "__main__":
    pass