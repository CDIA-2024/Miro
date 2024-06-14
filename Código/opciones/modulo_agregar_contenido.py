def main_menu():
    op = 0
    while op != 5:
        print("¿Que tipo de contenido desea agregar?")
        print(" 1. Pelicula")
        print(" 2. Serie")
        print(" 3. Anime")
        print(" 4. Video Juego")
        print(" 5. Volver al Menu Principal")

        op = int(input("Elija una opción: "))
    
        if op <= 4:
            ti = input("Ingrese el titulo del contenido a agregar: ")
        elif op == 5:
            print("Volviendo al menu principal")
        else:
            print("Opción inválida, por favor eliga un contenido del menú")
    
def titulo():
    ()
#opcion_agregar_contenido()
# en esta seccion se podra agregar elementos a la lista ya formada.
#para eso se le debera dar un argumento a la funcion.
