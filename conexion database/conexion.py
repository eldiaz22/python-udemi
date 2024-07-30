# py -m pip install psycopg2

import psycopg2
try:
    conexion = psycopg2.connect(user="postgres",password="diazjunior22",host="localhost", database= "test_db")
    print("real")
    cursor = conexion.cursor()
    sentencia1 = "SELECT * FROM personas" #formato sql
    cursor.execute(sentencia1) #llamar la sentencia 
    registro = cursor.fetchone()
    print(registro)

except:
    print("hola")

finally:
    conexion.close()
    cursor.close()
