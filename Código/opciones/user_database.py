usuarios = {}

def registrar_usuario():
    print("Registro de nuevo usuario")
    usuario = input("Ingrese el nombre de usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre de usuario.")
        return
    clave = input("Ingrese la contraseña: ")
    usuarios[usuario] = clave
    print("Usuario registrado con éxito.")

def validar_usuario(usuario, clave):
    return usuarios.get(usuario) == clave
