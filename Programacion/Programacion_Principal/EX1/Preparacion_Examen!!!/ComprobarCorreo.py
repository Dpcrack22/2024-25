# Lista de correos electrónicos a validar
correos = [
    "a@b.com", "a.b@c.com", "a.b@c.d.es",  # Ejemplos válidos
    ".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com",  # Ejemplos inválidos de usuarios
    "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com", "awer@wer.com",  # Ejemplos inválidos de dominios
    "awer@wer.commmm", "..@wer.commmm"  # Correos inválidos
]

# Imprime el resultado de la validación de los correos
print("Resultado de la validación de correos: ")

# Itera sobre cada correo en la lista para validarlo
for correo in correos:
    ini = correo.find("@")  # Encuentra la posición del "@" en el correo

    # Validación inicial: Verifica si no hay "@" o está en la primera posición
    if ini == -1 or ini == 0:
        print(f"{correo} Este es incorrecto / no valido")  # Mensaje de error
        continue  # Salta a la siguiente iteración del bucle

    # Separa el usuario y el dominio basados en la posición del "@"
    usuario = correo[:ini]  # Parte antes del "@"
    dominio = correo[ini + 1:]  # Parte después del "@"

    # Inicializa la variable de validación
    Valido = True

    # Validación del usuario (parte antes del "@")
    for i in range(len(usuario)):
        # Verifica que solo contenga caracteres alfanuméricos o puntos
        if not (usuario[i].isalnum() or usuario[i] == "."):
            Valido = False
            break
        # Verifica que no haya dos puntos consecutivos en el usuario
        if i > 0 and usuario[i] == "." and usuario[i - 1] == ".":
            Valido = False
            break

    # Inicializa la cuenta de puntos en el dominio
    puntos = 0

    # Validación del dominio (parte después del "@")
    for i in range(len(dominio)):
        # Verifica que solo contenga caracteres alfanuméricos o puntos
        if not (dominio[i].isalnum() or dominio[i] == "."):
            Valido = False
            break
        # Verifica la correcta ubicación de los puntos en el dominio
        if dominio[i] == ".":
            # No debe haber puntos al principio, al final o seguidos por otro punto
            if i == 0 or i == len(dominio) - 1 or dominio[i-1] == ".":
                Valido = False
                break
            puntos += 1  # Cuenta la cantidad de puntos en el dominio

    # Si el dominio no tiene al menos un punto, lo marca como inválido
    if puntos < 1:
        Valido = False

    # Imprime el resultado de la validación
    print(f"{correo}: {'Válido' if Valido else 'No válido'}")
