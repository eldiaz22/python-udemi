from producto import Producto
class Orden:
    contador_orden = 0
    def __init__(self, productos):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)
    
    def agregar_producto(self,producto):
        self._productos.append(producto)
        
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    def __str__(self) :
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "|"
        return f"Orden: {self._id_orden}, \n Productos: {productos_str}, total = {self.calcular_total()} "
    
    
if __name__ == "__main__":
    producto1 = Producto("Camisa", 100.00)
    producto2 = Producto("Pantalon", 150.00)
    productosx = [producto1,producto2]
    orden1 = Orden(productosx)
    print(orden1)
