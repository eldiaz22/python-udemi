from logger_base import log
#import psycopg2 as bd
import pymysql as mysql
import sys

class Conexion:
    _DATABASE = 'test_db'
    #_USERNAME = 'postgres'
    _USERNAME = 'root'
    _PASSWORD = 'diazjunior22'
    #_DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls): # para los classmetodos se coloca cls
        if cls._conexion is None:
            try:
                cls._conexion = mysql.connect(
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           #port=cls._DB_PORT,
                                           host=cls._HOST,
                                           database=cls._DATABASE)
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()  #para termina la conexion si hay un error
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor
        
if __name__ == "__main__":
    Conexion.obtenerConexion()