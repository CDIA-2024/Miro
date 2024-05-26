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
        Escribir "       Inicio de Sesi�n"       
        Escribir "==============================="
        
        Escribir "Usuario: "
        Leer usuario
        Escribir "Contrase�a: "
        Leer Clave
		// Validaci�n del usuario y contrase�a (simulaci�n)
        Si usuario = "usuario1" y Clave = "contrasena123" Entonces
            Limpiar Pantalla
            Escribir "==============================="
            Escribir "   Inicio de Sesi�n Exitoso"   
            Escribir "==============================="
            // Aqu� ir�a la l�gica despu�s de un inicio de sesi�n exitoso
            Esperar 2 segundos // Esperar 2 segundos antes de continuar
            // Se puede agregar un bucle o men� principal despu�s del login aqu�
            // Iniciar men� principal
            intentos <- 3 // Romper el bucle de login exitoso
        Sino
			
            Limpiar Pantalla
            Escribir "=========================="
            Escribir "   Usuario o contrase�a"
            Escribir "      incorrectos"
            Escribir "=========================="
			intentos <- intentos + 1
            Escribir "Intentos restantes: ", 3 - intentos
            Esperar 2 segundos // Esperar 2 segundos para que el usuario vea el mensaje
			
        FinSi
		
	Hasta Que intentos = 3
	
	Si intentos == 3 y usuario <> usuario1 y clave <> contrasena123  Entonces
		Escribir ('Usuario Bloqueado. Utilizo 3 intentos')
		Escribir ('Intentelo de nuevo m�s tarde')
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
			Escribir '  6. MIS RESE�AS'
			Escribir '  7. AGREGAR CONTENIDO'
			Escribir '  8. VER PERFIL'
			Escribir '  9. SALIR'
			Escribir "========================"
			
			Escribir "Por favor, seleccione una opci�n: "
			Leer opcion
			
			Seg�n opcion Hacer
			
				1:
					Escribir 'Anime'
					// c�digo para la Opci�n Anime
				2:
					Escribir 'Pel�culas'
					// c�digo para la Opci�n Pel�culas
				3:
					Escribir 'Series'
					// c�digo para la Opci�n Series
				4:
					Escribir 'Juegos'
					// c�digo para la Opci�n Juegos
				5:
					Escribir 'Listas'
					// c�digo para la Opci�n Mis Listas
				6: 
					Escribir 'Rese�as'
					// c�digo para la Opcion Mis Rese�as
				7:
					Escribir 'Gracias por aportar a la Base de Datos de nuestra media traker'
					// c�digo para la Opci�n Agegar Contenido
				8:
					Escribir 'Perfil'
					// c�digo para la Opci�n Ver Perfil		
				9:
					Escribir 'Saliendo del programa...'
					// c�digo para la Opci�n Salir
				De Otro Modo:
					Escribir "Opci�n incorrecta. Por favor, elija una opci�n v�lida del men�."
					
			FinSeg�n
			//Esperar unos segundos antes de mostrar el men� nuevamente 
			//para que el usuario pueda ver el mensaje antes de que el men� se refresque
			Esperar 2 Segundos
			
		Hasta Que opcion = 9
		
	FinSi
	
FinAlgoritmo
