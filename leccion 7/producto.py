class Producto:
    contador_producto = 0
    def __init__(self, nombre,precio):
        Producto.contador_producto +=1
        self._id = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio #_ para indicar que nose debe modificar
    @property
    def precio(self): #metodo get para modificar
        return self._precio


    def __str__(self) :
        return f"Id Producto: {self._id}, (Nombre: {self._nombre}, Precio: {self._precio})" 
    
    
    
if __name__ == "__main__":
    producto1 = Producto("Camisa", 100.00)
    producto2 = Producto("Pantalon", 150.00)