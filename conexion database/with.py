import psycopg2

conexion = psycopg2.connect(user="postgres",password="diazjunior22",host="localhost", database= "test_db")


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia1 = "SELECT * FROM personas WHERE id_persona in (1,2,3)"
            #id_persona = input("proporciona el valor de id: ")
            cursor.execute(sentencia1) # proporcionamos la sentencia sql y los valores 
            registro = cursor.fetchall() # para llamar los datos
            for un in registro:
                print(un)
except Exception as e:
    print("Error en la conexion")

finally:
    conexion.close()