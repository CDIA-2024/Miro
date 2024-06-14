import mysql.connector

def crearLista():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
    cursor = conn.cursor()
    cor = input("Correo del usuario: ")
    cursor.execute("select id_usuario, correo from usuario where correo = %s",(cor,))
    correo = cursor.fetchone()
    id_user = int(correo[0])
    print(id_user)
    nombre = input("Nombre para la lista: ")
    fecha = input("Ingresar fecha (AAAA-MM-DD): ")
    contenido = input("Tipo de contenido (pelicula, serie, juego o anime): ")
    if contenido == "pelicula":
        cursor.execute('''
        select c.id_contenido, c.titulo, c.anio_lanzamiento from contenido c inner join pelicula p on c.id_contenido = p.id_contenido;
        ''')
        titulos = cursor.fetchall()
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        agregar = input("Cual de estos titulos desea agregar a la lista?(Seleccione el Id)")
        cursor.execute("select * from contenido where id_contenido = %s",(agregar,))
        id_cont = cursor.fetchone() 
        cont = int(id_cont[0])
        agregar = int(agregar)
        if cont == agregar:
            print("Si entro")
            cursor.execute("""INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES (%s, %s, %s, %s)""",
                           (fecha, id_user, agregar, nombre))
            conn.commit()

    elif contenido == "serie":
        cursor.execute('''
        select c.id_contenido, c.titulo, c.anio_lanzamiento from contenido c inner join serie p on c.id_contenido = p.id_contenido;
        ''')
        titulos = cursor.fetchall()
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
    elif contenido == "juego":
        cursor.execute('''
        select c.id_contenido, c.titulo, c.anio_lanzamiento from contenido c inner join videojuego p on c.id_contenido = p.id_contenido;
        ''')
        titulos = cursor.fetchall()
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
    elif contenido == "anime":
        cursor.execute('''
        select c.id_contenido, c.titulo, c.anio_lanzamiento from contenido c inner join anime p on c.id_contenido = p.id_contenido;
        ''')
        titulos = cursor.fetchall()
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
