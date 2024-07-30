#la forma ams optima para hacer conexion con base de datos

from logger_base import log
import mysql.connector
from mysql.connector import pooling
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'root'
    _PASSWORD = 'diazjunior22'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(pool_name="mi_pool",
                                                        pool_size=cls._MAX_CON,
                                                        host=cls._HOST,
                                                        user=cls._USERNAME,
                                                        password=cls._PASSWORD,
                                                        database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()  # para salir del programa
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        conexion.close()  # Se cierra la conexión para regresarla al pool
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()  # Cierra todas las conexiones del pool


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
    # Asegúrate de liberar las conexiones cuando ya no las necesites
