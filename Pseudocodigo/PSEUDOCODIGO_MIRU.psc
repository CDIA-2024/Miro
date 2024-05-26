Algoritmo PSEUDOCODIGO_EVIDENCIA2
	Definir usuario, clave Como Cadena
    Definir intentos Como Entero
	Definir opcion Como Entero
	Definir sesion_iniciada como logico
	sesion_iniciada <- Falso
    intentos <- 0
	Repetir
        Limpiar Pantalla
        Escribir "==============================="
        Escribir "       Inicio de Sesión"       
        Escribir "==============================="
        
        Escribir "Usuario: "
        Leer usuario
        Escribir "Contraseña: "
        Leer Clave
		// Validación del usuario y contraseña (simulación)
        Si usuario = "usuario1" y Clave = "contrasena123" Entonces
            Limpiar Pantalla
            Escribir "==============================="
            Escribir "   Inicio de Sesión Exitoso"   
            Escribir "==============================="
            // Aquí iría la lógica después de un inicio de sesión exitoso
            Esperar 2 segundos // Esperar 2 segundos antes de continuar
            // Se puede agregar un bucle o menú principal después del login aquí
            // Iniciar menú principal
            intentos <- 3 // Romper el bucle de login exitoso
        Sino
			
            Limpiar Pantalla
            Escribir "=========================="
            Escribir "   Usuario o contraseña"
            Escribir "      incorrectos"
            Escribir "=========================="
			intentos <- intentos + 1
            Escribir "Intentos restantes: ", 3 - intentos
            Esperar 2 segundos // Esperar 2 segundos para que el usuario vea el mensaje
			
        FinSi
		
	Hasta Que intentos = 3
	
	Si intentos == 3 y usuario <> usuario1 y clave <> contrasena123  Entonces
		Escribir ('Usuario Bloqueado. Utilizo 3 intentos')
		Escribir ('Intentelo de nuevo más tarde')
	FinSi
	
	Si usuario = "usuario1" y clave = "contrasena123"
		
		Repetir
			
			Limpiar Pantalla
			Escribir "========================"
			Escribir "     Menu Principal     "
			Escribir "========================"
			Escribir '  1. ANIME'
			Escribir '  2. PELICULAS'
			Escribir '  3. SERIES'
			Escribir '  4. JUEGOS'
			Escribir '  5. MIS LISTAS'
			Escribir '  6. MIS RESEÑAS'
			Escribir '  7. AGREGAR CONTENIDO'
			Escribir '  8. VER PERFIL'
			Escribir '  9. SALIR'
			Escribir "========================"
			
			Escribir "Por favor, seleccione una opción: "
			Leer opcion
			
			Según opcion Hacer
			
				1:
					Escribir 'Anime'
					// código para la Opción Anime
				2:
					Escribir 'Películas'
					// código para la Opción Películas
				3:
					Escribir 'Series'
					// código para la Opción Series
				4:
					Escribir 'Juegos'
					// código para la Opción Juegos
				5:
					Escribir 'Listas'
					// código para la Opción Mis Listas
				6: 
					Escribir 'Reseñas'
					// código para la Opcion Mis Reseñas
				7:
					Escribir 'Gracias por aportar a la Base de Datos de nuestra media traker'
					// código para la Opción Agegar Contenido
				8:
					Escribir 'Perfil'
					// código para la Opción Ver Perfil		
				9:
					Escribir 'Saliendo del programa...'
					// código para la Opción Salir
				De Otro Modo:
					Escribir "Opción incorrecta. Por favor, elija una opción válida del menú."
					
			FinSegún
			//Esperar unos segundos antes de mostrar el menú nuevamente 
			//para que el usuario pueda ver el mensaje antes de que el menú se refresque
			Esperar 2 Segundos
			
		Hasta Que opcion = 9
		
	FinSi
	
FinAlgoritmo
