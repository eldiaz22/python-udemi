from Entrada import entrada 

class Teclado(entrada): 
    contador_teclado = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca,tipo_entrada)
    def __str__(self):
        return f"ID:{self._id_teclado} {super().__str__()}"
    
    
if __name__ == "__main__":
    tecla = Teclado("Lenovo", "usb")
    print(tecla)



