from empleado import Empleado
from gerente import Gerente

def imprimir_detalle(objecto):
    print(objecto)
    print(type(objecto))
    if isinstance (objecto, Gerente):
        print(objecto.departamento)
    


empleado1 = Empleado("juan carlos", 50000)

gerente1 = Gerente("junior perez", 5000, "Barranquilla")

imprimir_detalle(gerente1)
