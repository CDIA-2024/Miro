#index.py
import time
from opciones import modulo_anime, modulo_peliculas, modulo_series, modulo_juegos, modulo_listas, modulo_listas, modulo_resena, modulo_agregar_contenido, modulo_perfil

from opciones.user_database import usuarios, registrar_usuario, validar_usuario

def limpiar_pantalla():
    print("\033[H\033[J", end="")

def login():
    intentos = 0
    sesion_iniciada = False

    while intentos <= 3:
        limpiar_pantalla ()
        print ("===============================")
        print ("      Usuario o contraseña     ")
        print ("          incorrectos          ")
        print ("===============================")

        usuario = input("Usuario: ")
        clave = input("contraseña:")

        if validar_usuario(usuario, clave):
            limpiar_pantalla()
            print ("===============================")
            print ("        Inicio de sesión       ")
            print ("            exitoso            ")
            print ("===============================")
            time.sleep(2)
            sesion_iniciada = True
            break
        else: 
            limpiar_pantalla ()
        print ("===============================")
        print ("      Usuario o contraseña     ")
        print ("          incorrectos          ")
        print ("===============================")
        intentos += 1
        print(f"intentos restantes: {3 - intentos}")
        time.sleep(2)

        opcion_intentar = 0

        if opcion_intentar == input("¿Desea intentar de nuevo? S/N"):
            if opcion_intentar.lower() != "s":
                break

        if not sesion_iniciada and intentos >= 3:
            print("No se pudo iniciar sesión")
            opcion_registro = input("¿Desea Registrarse? S/N") 
            if opcion_registro.lower() == "s":
                registrar_usuario()
            else:
                print("Usuario Bloqueado, ha utilizado más de 3 intentos")
                print("Intentelo de nuevo más tarde")
                time.sleep(2)
        return sesion_iniciada
    
def menu_principal():
    opcion = 0

    while opcion != 9:
        limpiar_pantalla()
        print ("===============================")
        print ("         Menú Principal        ")
        print ("===============================")
        print(" 1. Anime")
        print(" 2. Películas")
        print(" 3. Series")
        print(" 4. Juegos")
        print(" 5. Mis Listas")
        print(" 6. Mis Reseñas")
        print(" 7. Agregar Contenido")
        print(" 8. Ver Perfil")
        print(" 9. Salir")
        print ("===============================")

        opcion = int(input("Por favor, seleccione una opción "))

        if opcion == 1:
                modulo_anime.opcion.anime()
        if opcion == 2:
                modulo_peliculas.opcion_peliculas()
        if opcion == 3:
                modulo_series.opcion_series()
        if opcion == 4:
                modulo_juegos.opcion_juegos()
        if opcion == 5:
                modulo_listas.opcion_listas()
        if opcion == 6:
                modulo_resena.opcion_resena()
        if opcion == 7:
                modulo_agregar_contenido.opcion_agregar_contenido()
        if opcion == 8:
                modulo_perfil.opcion_perfil()
        if opcion == 9:
                print("Saliendo del Programa...")
        else:
                print("Opción inválidad, por favor eliga una opción del menú")
          
        time.sleep(2)

if __name__ == "__main__":
 
    while True:
        limpiar_pantalla()
        print ("===============================")
        print ("         BIENVENIDO       ")
        print ("===============================")
        print(" 1. Iniciar sesión")
        print(" 2. Registrarse")
        print(" 3. Salir")
        print ("===============================")

        opcion_inicio = int(input("Seleccione una opción"))

        if opcion_inicio == 1:
            if login():
                menu_principal()
            else:
                break
        elif opcion_inicio == 2:
            registrar_usuario()
        elif opcion_inicio == 3:
            print("Saliendo del Programa...")
            break
        else:
            print("Opción inválida, por favor seleccione una opción del menú")
        
    time.sleep(2)










        

