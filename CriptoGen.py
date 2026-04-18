#___Generador de contraseñas muy seguras__


#Pense poner la libreria randoms pero no, secrets es mucho mas seguro.
#¿Y priorizamos la segueridad de el usuario no...?
#Aprendi mucho sobre la seguridad en mi curso de ciberseguridad y los usuarios aman y deberian tener una seguridad de calidad, no?

import secrets
import string

#Definimos los caracteres que vamos a usar en nuestra contraseña, aqui puse letras(ascii_letters), digitos(.digits), y signos de puntuacion(.puntuation)(Los signos de puntuacion son estos: . , ¿? ¡! ... Solo son unos ejemplos, por si se te olvidaron jeje

caracteres = string.ascii_letters + string.digits + string.punctuation
continuar = "si"

# 2. El bucle envuelve todo el proceso de creación de la contraseña (para crear bucles se utiliza "while")
while continuar.lower() == "si":
    try:
        longitud = int(input("Ingrese el tamaño de la contraseña: "))

#Por si a alguien se le ocurre poner 0 o numero negativos jeje:
    except ValueError:
        print("Error: Ingrese un número entero (ej: 12).")
        continue 

    #Por si a alguien se le ocurre utilizar utilizar numero negativos o directamente "0"
    if longitud <= 0:
        print("Error: La longitud debe ser mayor a 0.")
        continue

    # Generamos la contraseña dentro del bucle, osea el while de arribita(Linea 16)

    contrasena = "".join(secrets.choice(caracteres) for i in range(longitud))
    
    print("La contraseña generada es: " + contrasena)
    
    # Preguntamos si quiere volver a crear otra contraseña, si pones "no" terminaremos con el programa osea podras cerrarlo.
    continuar = input("\n¿Desea crear otra contraseña? (si/no): ")

print("Programa finalizado correctamente, puedes cerrarlo. =3")
