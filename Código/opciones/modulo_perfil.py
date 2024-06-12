#se definie la funcion perfil de usuario

class Perfil_de_usuario:
    def __init__(self, nombre, email, cumpleaños):
        self.nombre = nombre
        self.email = email
        self.cumpleaños = cumpleaños
        self.lista_favorita = []# aca podríamaos crear una tabla llamda lista favorita

    def add_contenido_favorito(self, contenido_titulo):
        self.lista_favorita.append(contenido_titulo)

    def display_profile(self):
        print(f"Nombre: {self.nombre}")
        print(f"Correo electrónico: {self.email}")
        print(f"Cumpleaños: {self.cumpleaños}")
        print("Lista multimedia favorita:")
        for contenido in self.lista_favorita:
            print(f"- {contenido}")

# Creamos un perfil de usuario
mi_perfil = Perfil_de_usuario(nombre="Yesica", email="yesica@gmail.com", cumpleaños="06/03/1995")

# Agregar contenido multimedia favorito
mi_perfil.lista_favorita.append("TOM RAIDER")
mi_perfil.lista_favorita.append("The Dark Knight")
mi_perfil.lista_favorita.append("SHOGUN")

# Mostrar el perfil
mi_perfil.display_profile()
