from manejos import Manejo_archivo

with Manejo_archivo("prueba2.txt") as archivo:
    print(archivo.read())