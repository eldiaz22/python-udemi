import psycopg2

conexion = psycopg2.connect(user='postgres',password='diazjunior22',host='localhost',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
            cursor.execute(sentencia, valores) #para hacer culsulta
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()