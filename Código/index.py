#index.py
import time
from opciones import (modulo_anime, 
                     modulo_peliculas,
                     modulo_series,
                     modulo_juegos, 
                     modulo_lista, 
                     modulo_reseñas,                
                     modulo_agregar_contenido,                                              
                     modulo_perfil,
                     config)


def limpiar_pantalla():
    print("\033[H\033[J", end="")

def mensaje_formateado(mensaje=None, color=None, estilo=None, caracter=None):
    mensaje_formateado = ""
    if mensaje is not None:
        mensaje_formateado += f"{color}{(estilo if estilo is not None else '')}{mensaje}{config.colores.RESET}"
    if caracter is not None:
        mensaje_formateado += f"{color}{(estilo if estilo is not None else '')}{caracter}{config.colores.RESET}"

    print(mensaje_formateado)


def login():
    intentos = 0
    sesion_iniciada = False

    while intentos <= 3:
        limpiar_pantalla ()
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROJO)
        mensaje_formateado("      Usuario o contraseña     ", config.colores.ROJO, config.colores.NEGRITA)
        mensaje_formateado("          incorrectos          ", config.colores.ROJO, config.colores.NEGRITA)
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROJO)

        usuario = input(mensaje_formateado("Usuario: ", config.colores.CYAN, config.colores.NEGRITA))
        clave = input(mensaje_formateado("contraseña: ", config.colores.CYAN, config.colores.NEGRITA))
        
        if validar_usuario(usuario, clave):
            limpiar_pantalla()
            mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE)
            mensaje_formateado("        Inicio de sesión       ", config.colores.VERDE, config.colores.NEGRITA)
            mensaje_formateado("            exitoso            ", config.colores.VERDE, config.colores.NEGRITA)
            mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE)
            time.sleep(2)
            sesion_iniciada = True
            break
        else: 
            limpiar_pantalla ()
            mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROJO)
            mensaje_formateado("      Usuario o contraseña     ", config.colores.ROJO, config.colores.NEGRITA)
            mensaje_formateado("          incorrectos          ", config.colores.ROJO, config.colores.NEGRITA)
            mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROJO)
            intentos += 1
            print(f"intentos restantes: {3 - intentos}")
            time.sleep(2)

        opcion_intentar = 0

        if opcion_intentar == input("¿Desea intentar de nuevo? S/N"):
            if opcion_intentar.lower() != "s":
                break

        if not sesion_iniciada and intentos >= 3:
            mensaje_formateado("No se pudo iniciar sesión", config.colores.AMARILLO)
            opcion_registro = input(mensaje_formateado("¿Desea Registrarse? S/N", config.colores.NEGRITA)) 
            if opcion_registro.lower() == "s":
                registrar_usuario()
            else:
                mensaje_formateado("Usuario Bloqueado, ha utilizado más de 3 intentos", config.colores.ROJO)
                mensaje_formateado("Intentelo de nuevo más tarde", config.colores.NEGRITA)
                time.sleep(2)
        return sesion_iniciada
    
def menu_principal():
    opcion = 0

    while opcion != 9:
        limpiar_pantalla()
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.MENTA)
        mensaje_formateado("         Menú Principal        ", config.colores.ROSA_CLARO config.colores.NEGRITA)
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.MENTA)
        print(" 1. Anime")
        print(" 2. Películas")
        print(" 3. Series")
        print(" 4. Juegos")
        print(" 5. Mis Listas")
        print(" 6. Mis Reseñas")
        print(" 7. Agregar Contenido")
        print(" 8. Ver Perfil")
        print(" 9. Salir")
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.MENTA)

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
                modulo_lista.opcion_listas()
        if opcion == 6:
                modulo_reseñas.opcion_resena()
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
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.CYAN)
        mensaje_formateado("          BIENVENIDO           ", config.colores.ROSA_CLARO, config.colores.NEGRITA)
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.CYAN)
        print(" 1. Iniciar sesión")
        print(" 2. Registrarse")
        print(" 3. Salir")
        mensaje_formateado(config.caracteres_especiales.GUION, config.colores.CYAN)

        opcion_inicio = int(input("Seleccione una opción: "))

        if opcion_inicio == 1:
            if login():
                menu_principal()
            else:
                break
        elif opcion_inicio == 2:
            registrar_usuario()
        elif opcion_inicio == 3:
            print("Gracias por usar Miru ♡")
            mensaje_formateado("Saliendo del Programa...", config.colores.LIMA)
            break
        else:
            print("Opción inválida, por favor seleccione una opción del menú ")
        
    time.sleep(2)










        

