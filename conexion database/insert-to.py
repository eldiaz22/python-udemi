# import psycopg2 para postgrest
import pymysql


#conexion = psycopg2.connect(user='postgres',password='diazjunior22',host='localhost',database='test_db')
conexion = pymysql.connect(host='127.0.0.1',user='root',passwd='diazjunior22',db='test_db')
if __name__ == "__main__" :
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO personas(nombre, apellido, correo) VALUES( %s, %s, %s)'
                valores = ('junior', 'Lara', 'clara@mail.com')
                cursor.execute(sentencia, valores)
                conexion.commit()
                registros_insertados = cursor.rowcount
                print(f'Registros Insertados: {registros_insertados}')
            
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    #finally:
        conexion.close()


