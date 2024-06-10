# se crea diccionario de Usuario:

usuarios = {"cesia":"123"}

# se crea la funcion para registrar un usuario

def registrar_usuario(usuario, clave):
    
    if usuario in usuarios:
        print(f"el usuario  '{usuario}' ya se encuentra en uso.Por favor intenta con otro nombre")
        return False
    else:
        usuarios[usuario] = clave
        print(f"usuario'{usuarios}' registrado de manera exitosa")
        return True
    

# se crea funcion para validar Usuario

def validar_usuario(usuario,clave):
    
    if usuario in usuarios and usuarios[usuario] == clave:
        return True
    else:
        return False