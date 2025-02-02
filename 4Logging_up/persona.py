from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, correo=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo

    def __str__(self):
        return f'''
            Id Persona: {self._id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._correo}
        '''

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return  self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo


if __name__ == "__main__":
    persona1 = Persona(1,"juan","diaz","jdiaz@gmail.com")
    log.debug(persona1)
    #simular un insert 
    persona2 = Persona(nombre="juan", apellido="diaz", correo="jdiaz@gmail.com")
    log.debug(persona2)
    #simular un remove
    persona3 = Persona(id_persona = 1)
    log.debug(persona3)