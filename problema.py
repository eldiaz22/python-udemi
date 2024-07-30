
for i in range(1,10+1):
    if i != 5:
        resultado = i * 5
        print(f"{i} x 5 = {resultado}")
        
        
        
        
        
import random

def juego():
    def elecion():

        pc_elecion = ["piedra","papel","tijera"]
        elecion_pc = random.choice(pc_elecion)
        return elecion_pc , player_elecion
    
    def mensajes():
        mensajes_aleatorios = ["vamos que tu puedes"," ganale a esa maquina", "confio en ti"]
        mensaje_final = random.choice(mensajes_aleatorios)
        return mensaje_final

    intentos = 5
    puntos = 0
    ciclo = 0
    while intentos != 0:
        if ciclo == 0:
            print("Empezemos El Juego")
        if ciclo != 0:
            print( mensajes())
        player_elecion = input("Elije Piedra , Papel , O Tijera: ")
        player_elecion.lower  
        pc = elecion()   
        
        if player_elecion == "piedra" and pc == "papel" or  player_elecion == "papel" and pc == "piedra"  or  player_elecion == "tijera " and pc == "papel":
            print("GANASTE")
            puntos =  puntos + 5 
            print(f"Ahora Tienes {puntos} puntos")
            
        else: 
            print("Perdiste")
            intentos = intentos - 1
            print(f"TE QUEDAN {intentos} intentos")
        ciclo+=1
        
    else: print("SE HA TERMINADO EL JUEGO")



juego()



bienvenidad = "hola $"

    