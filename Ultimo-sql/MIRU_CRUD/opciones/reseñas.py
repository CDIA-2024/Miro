import mysql.connector
from mysql.connector import Error
from datetime import date

# Función para crear conexión a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='miru_1.1.1',
            user='root',
            password='CIK:830_'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Función para obtener el ID de usuario
def get_user_id(email):
    connection = create_connection()
    
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id_usuario FROM usuario WHERE correo = %s", (email,))
        user_id = cursor.fetchone()
        
        if user_id:
            return user_id[0]
        else:
            print("Usuario no encontrado.")
            return None

    except Error as e:
        print(f"Error al obtener el ID de usuario: {e}")
        return None

    finally:
        cursor.close()
        connection.close()

# Función para listar reseñas del usuario
def listar_reseñas(email):
    user_id = get_user_id(email)
    if user_id is None:
        return False

    connection = create_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        query = """
        SELECT r.id_reseña, c.titulo, r.fecha, r.texto, r.puntuacion
        FROM reseña r
        JOIN contenido c ON r.id_contenido = c.id_contenido
        WHERE r.id_usuario = %s
        """
        cursor.execute(query, (user_id,))
        reseñas = cursor.fetchall()
        
        for reseña in reseñas:
            print(f"ID: {reseña[0]}, Título: {reseña[1]}, Fecha: {reseña[2]}, Texto: {reseña[3]}, Puntuación: {reseña[4]}")
        return True

    except Error as e:
        print(f"Error al listar reseñas: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función para filtrar reseñas
def filtrar_reseñas(email, puntuacion=None, tipo_contenido=None):
    user_id = get_user_id(email)
    if user_id is None:
        return False

    connection = create_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        query = """
        SELECT r.id_reseña, c.titulo, r.fecha, r.texto, r.puntuacion
        FROM reseña r
        JOIN contenido c ON r.id_contenido = c.id_contenido
        JOIN genero g ON c.id_genero = g.id_genero
        WHERE (%s IS NULL OR r.puntuacion = %s)
        AND (%s IS NULL OR g.nombre = %s)
        AND r.id_usuario = %s
        """
        cursor.execute(query, (puntuacion, puntuacion, tipo_contenido, tipo_contenido, user_id))
        reseñas = cursor.fetchall()
        
        for reseña in reseñas:
            print(f"ID: {reseña[0]}, Título: {reseña[1]}, Fecha: {reseña[2]}, Texto: {reseña[3]}, Puntuación: {reseña[4]}")
        return True

    except Error as e:
        print(f"Error al filtrar reseñas: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función para agregar una nueva reseña
def agregar_reseña(email, id_contenido, texto, puntuacion):
    user_id = get_user_id(email)
    if user_id is None:
        return False

    connection = create_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        
        # Insertar nueva reseña
        query = """
        INSERT INTO reseña (fecha, texto, puntuacion, id_usuario, id_contenido) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (date.today(), texto, puntuacion, user_id, id_contenido))
        connection.commit()

        print("Reseña agregada exitosamente.")
        return True

    except Error as e:
        connection.rollback()
        print(f"Error al agregar la reseña: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función principal para manejar reseñas
def main_menu():
    email = input("Ingrese su correo electrónico: ")
    print("1. Listar mis reseñas")
    print("2. Filtrar reseñas")
    print("3. Agregar nueva reseña")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        listar_reseñas(email)
    elif choice == '2':
        puntuacion = input("Filtrar por puntuación (dejar en blanco para omitir): ")
        puntuacion = int(puntuacion) if puntuacion else None
        tipo_contenido = input("Filtrar por tipo de contenido (dejar en blanco para omitir): ")
        filtrar_reseñas(email, puntuacion, tipo_contenido)
    elif choice == '3':
        id_contenido = int(input("Ingrese el ID del contenido: "))
        texto = input("Ingrese el texto de la reseña: ")
        puntuacion = int(input("Ingrese la puntuación de la reseña: "))
        agregar_reseña(email, id_contenido, texto, puntuacion)
    else:
        print("Opción no válida.")
