class Persona : 
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self.nombre } {self.apellido} {self.edad}")


persona1 = Persona("junior","diaz", 18)
# persona.mostrar_detalle()
# Persona.mostrar_detalle(persona1) # otra forma
persona1.telefono = "52656556" # si se define asi nose comporte con los demas objectos
print(persona1.telefono)


# modificar atributos del objecto   directamente
#persona.nombre = "juan"
