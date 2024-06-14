import mysql.connector
from mysql.connector import Error

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


# Crear tabla de preferencias.
#CREATE TABLE IF NOT EXISTS preferencias_usuario()
   # id usuario PRIMARY KEY,
    #email TEXT,
    #receive_news BOOLEAN

# definimos una funcion de preferencia de usaurios

def preferencias_usuario():
    while True:
        eleccion= input("¿Deseas recibir novedades en tu correo?(si/no)").lower()
        if eleccion in ["sí","si","s","SI","SÍ","S"]:
            return True 
        elif eleccion["No","no","n","N"]:
            return False
        else:
            print("Por favor , responde si/no")       


preferencias_usuario()

def preferencias_guardadas():
    # cursor.execute("INSERT INTO user_preferences (email, receive_news) VALUES (?, ?)",
                   #(email, receive_news))
   # conn.commit()
    print("Preferencia guardada correctamente.")
preferencias_guardadas()










