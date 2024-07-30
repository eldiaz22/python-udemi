from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM personas ORDER BY id_personas'
    _INSERTAR = 'INSERT INTO personas(nombre, apellido, correo) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE personas SET nombre=%s, apellido=%s, correo=%s WHERE id_personas=%s'
    _ELIMINAR = 'DELETE FROM personas WHERE id_personas=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:  #para no cerrarlo manualmente
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall() # recuperar todos los datos de personas
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.correo)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f"Persona insertada{persona}")
                conexion.commit()
            return cursor.rowcount
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion()  as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.correo, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                conexion.commit()
                return cursor.rowcount
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion() as c:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Objeto eliminado: {persona}')
                c.commit()
                return cursor.rowcount

                
            
if __name__ == '__main__':
    
    #insertas
    # persona1 = Persona(nombre="duan",apellido="kiaz",correo="jdiadddddz@gmail.com")
    # personas_insertada = PersonaDAO.insertar(persona1)
    # log.debug(personas_insertada)
    
        # Actualizar un registro
    # persona1 = Persona(50,'Juan Carlos', 'Juarez', 'cjjuarez@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    
    
    # Eliminar un registro
    persona1 = Persona(id_persona=49)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    
    #selecionar
    # personas = PersonaDAO.seleccionar()
    # for persona in personas:
    #     log.debug(persona)