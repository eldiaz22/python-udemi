class Manejo_archivo:
    def __init__(self,nombre) :
        self.nombre = nombre
    
    def __enter__(self):
        print(f"obtenemos el recurso".center(50,"-"))
        self.nombre = open(self.nombre , "r" , encoding="utf8")
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Cerramos el recurso".center(50,"-"))
        if self.nombre:
            self.nombre.close()