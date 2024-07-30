import os

class Lista :
    ruta = "Pelicula.py"

    @classmethod
    def agregar_movie(cls,name):
        with open(cls.ruta,"a" , encoding="utf8" ) as archivo:
            archivo.writelines(f"{name}\n")
    def mostrar_movies(cls):
        with open(cls.ruta, "r") as archivo:
            archivo.read()
    def eliminar_movie(cls):
        with open(cls.ruta, "w") as archivo:
            os.remove(archivo)
            
            
