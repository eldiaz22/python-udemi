class Persona: 
    contador_persona = 0
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        
    def __init__(self, nombre, edad):
        Persona.generar_siguiente_valor()
        self.id_persona = Persona.contador_persona
        self._nombre = nombre
        self._edad = edad
    
    def __str__(self) :
        return f'Persona [{self.id_persona} {self._nombre} {self._edad}]'
    
    
    
persona1 = Persona('Juan', 28)
print(persona1)
persona2 = Persona('Karla', 30)
persona = Persona('Juan', 28)

print(persona2)
print(f"Valor contador personas: {Persona.contador_persona}")