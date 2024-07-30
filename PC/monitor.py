class Monitor:
    contador_monitor = 0
    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño
    def __str__(self):
        return f"ID {self._id_monitor} MARCA: {self._marca} Tamaño: {self._tamaño}" 
    
if __name__ == "__main__":
    pantalla =  Monitor("LG", 27)
    print(pantalla)