from Entrada import entrada


class Mouse(entrada):
    contador_mouse = 0
    def __init__(self,marca,tipo_entrada):
        Mouse.contador_mouse +=1   
        self._id_mouse = Mouse.contador_mouse
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
    def __str__(self):
        return f" ID : {self._id_mouse}  {super().__str__()}"
    
    
if __name__ == "__main__":
    mouse1 = Mouse("HP","USB")
    print(mouse1)