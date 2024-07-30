from monitor import Monitor
from  mouse import Mouse
from teclado import Teclado
from Computadora import Computadora
from orden import Orden




teclado1 = Teclado("HP", "USB")
mouse1 = Mouse("ACE", "BLUTO")
monitor1 = Monitor("X" , "USB")
pc = Computadora("GAMER",teclado1 , mouse1 , monitor1)



teclado2 = Teclado("HP", "USB")
mouse2 = Mouse("ACE", "BLUTO")
monitor2 = Monitor("X" , "USB")
pc2 = Computadora("OFFICER",teclado2 , mouse2 , monitor2)


computadoras = [pc,pc2]

orden1 = Orden(computadoras)
print(orden1)

teclado2 = Teclado("HP", "USB")
mouse2 = Mouse("ACE", "BLUTO")
monitor2 = Monitor("X" , "USB")
pc3 = Computadora("LENOVO",teclado2 , mouse1 , monitor2)


computadoras = [pc,pc2,pc3]

orden2 = Orden(computadoras)
print(orden2)