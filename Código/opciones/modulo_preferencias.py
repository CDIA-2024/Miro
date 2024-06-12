# primero deberemos realizar la conexxion con la base de datos
#Python

#import sqlite3

# Conexión a la base de datos (crea un archivo si no existe)
#conn = sqlite3.connect("user_preferences.db")
#cursor = conn.cursor()

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










