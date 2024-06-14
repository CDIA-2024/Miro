import mysql.connector
from mysql.connector import Error

# Función para crear conexión a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='miru',
            user='root',
            password='CIK:830_'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Se Crear la tabla de perfiles de usuario-se debe asociar .
# se debe asociar a la tabla de listas de preferencia
# se debe asociar a lastablas reseñas

def mostrar_perfil(user_id):
    cursor.execute("SELECT nombre, correo, cumpleanos FROM usuarios WHERE id = ?", (user_id,))
    perfil = cursor.fetchone()
    if perfil:
        nombre, correo, cumpleanos = perfil
        print(f"Nombre de usuario: {nombre}")
        print(f"correo: {correo}")
        print(f"Año_de_nacimiento: {Año de Nacimiento}")
    else:
        print("Usuario no encontrado.")
## se define la funcion para mostrar listas guardadas,debe 
# estar conectado a la base de datos de la lista de preferencia

def mostrar_listas(user_id):
    cursor.execute("SELECT nombre FROM listas WHERE user_id = ?", (user_id,))
    listas = cursor.fetchall()
    if listas:
        print("Listas guardadas:")
        for lista in listas:
            print(f"- {lista[0]}")
    else:
        print("No se encontraron listas guardadas para este usuario.")

# se define la funcion mis reseñas, 
#se debe conectar con la tabla base de datos  de reseñas, revisar los argumentos
# en el codigo uso UNION  ALL : para combinar las reseñas de peliculas,juegos,animes

def mostrar_resenas(user_id):
    cursor.execute("""
        SELECT pelicula, calificacion FROM resenas WHERE user_id = ?
        UNION ALL
        SELECT anime, calificacion FROM resenas_anime WHERE user_id= ?
        UNION ALL
        SELECT juego, calificacion FROM resenas_juego WHERE user_id = ?
    """, (user_id, user_id,user_id))
    resenas = cursor.fetchall()
    if resenas:
        print("Reseñas:")
        for item, calificacion in resenas:
            print(f"- {item}: {calificacion} estrellas")
    else:
        print("No se encontraron reseñas para este usuario.")








# Cerrar la conexión a la base de datos
conn.close()
