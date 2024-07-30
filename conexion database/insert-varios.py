import psycopg2

conexion = psycopg2.connect(user='postgres',password='diazjunior22',host='localhost',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Marcos', 'Cantu', 'mcantu@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
            )
            cursor.executemany(sentencia, valores) #para insertas varios valores
            # conexion.commit()   guardaddo
            registros_insertados = cursor.rowcount # ver cuantos registros hiciste
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()