try:
    archivo = open("manejo-archivo\\prueba2.txt", "w", encoding="utf8")
    archivo.write("AGREGAMOS UNA NUEVA LINEA")
    archivo.write("AGREGAMOS UNA NUEVA LINEA")

except Exception as e:
    print(e)
finally:
    archivo.close()