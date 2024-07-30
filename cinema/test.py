from lista import Lista
from name_movie import movie


opciones = None

while opciones != 4:
    print("OPCIONES")
    print(f"OPCION 1 AGRER UNA PELICULAR\n OPCIONES 2 VER LISTA DE PELICULA \n 3 ELIMINAR PELICULA \n 4 SALIR")
    opciones = int(input("INGRESE UNA OPCION: "))
    if opciones == 1:
        name_pelicula = input("INGRESE EL NOMBRE DE LA PELICULA: ")
        pelicula =  movie(name_pelicula)
        Lista.agregar_movie(pelicula)
        
    elif opciones == 2:
        Lista.mostrar_movies()

    elif opciones == 3:
        movie.eliminar_movie()

    elif opciones == 4:
        print("GRACIAS POR USAR EL PROGRAMA")
        break