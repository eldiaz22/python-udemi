try:
    archivo = open("manejo-archivo\\pueba2.txt", "r")
    print(archivo.read())
# readlines
    for line in archivo:
        print(line.read())
except Exception as e:
    print(e)
    
finally: archivo.close()