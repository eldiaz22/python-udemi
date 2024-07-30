from monitor import Monitor
from  mouse import Mouse
from teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self,nombre,teclado,mouse,monitor):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._teclado = teclado
        self._mouse = mouse
        self._monitor = monitor
    
    def __str__(self):
        return f"""
            {self._nombre}: {self._id_computadora}
            Teclado: {self._teclado}
            Mouse: {self._mouse}
            Monitor: {self._monitor}
        
    
            """
       
       
if __name__ == "__main__":     
    teclado1 = Teclado("HP", "USB")
    mouse1 = Mouse("ACE", "BLUTO")
    monitor1 = Monitor("X" , "USB")
    compu = Computadora("GAMER",teclado1 , mouse1 , monitor1)
    print(compu)