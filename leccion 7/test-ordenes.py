from orden import Orden
from producto import Producto

producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 150.00)
producto3 = Producto("Relog", 5.000)
producto4  = Producto("zapato", 4.000)

lista_productos = [producto1,producto2]
lista_productos2 = [producto3,producto4]

orden1 = Orden(lista_productos)
orden2 = Orden(lista_productos2)
print(orden2)

orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
