# Lista inicial con correos electrónicos, tanto válidos como incorrectos
mails_incorrectos = [".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com", 
                     "asdf..@awe.com", "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com",
                     "awer@wer.com", "awer@wer.commmm", "..@wer.commmm", "a@b.com", 
                     "a.b@c.com", "a.b@c.com", "a.b@c.d.es"]

# Variable para indicar si el correo es válido o no
valido = False

# Iteramos sobre cada correo de la lista
for correo in mails_incorrectos:
    # Encontramos la posición del carácter "@"
    inicio = 0
    final = correo.find("@")
    
    # Extraemos la parte del usuario (antes del "@") y eliminamos los puntos con .replace()
    usuario = correo[inicio:final].replace(".", "")
    print(usuario)  # Mostramos la parte del usuario para depuración

    # Extraemos la parte del dominio (después del "@")
    dominio = correo[final + 1:]
    
    # Separamos el dominio en dos partes: antes y después del primer "."
    final2 = dominio.find(".")  # Encuentra el primer punto en el dominio
    inicio_dominio = dominio[inicio:final2]  # Parte antes del primer "."
    print(inicio_dominio)  # Mostramos el inicio del dominio para depuración
    
    final_dominio = dominio[final2 + 1:]  # Parte después del primer "."
    print(final_dominio)  # Mostramos la parte final del dominio para depuración

    # Validamos la parte del usuario
    if not usuario.isalnum() or correo[inicio:final].startswith(".") or correo[inicio:final].find("..") != -1:
        print("La parte usuario '{}' del correo no es correcta".format(correo[inicio:final]))
        valido = False

    # Validamos la parte inicial del dominio
    elif not inicio_dominio.isalnum():
        print("La parte del dominio '{}' del correo no es correcta".format(inicio_dominio))
        valido = False

    # Validamos la parte final del dominio (su longitud debe estar entre 1 y 3 caracteres)
    elif not 1 <= len(final_dominio) < 4:
        print("La parte final del dominio '{}' del correo no es correcta".format(final_dominio))
        valido = False

    # Si todas las validaciones pasan, el correo es válido
    else:
        valido = True

    # Mostramos el resultado para el correo actual
    if valido:
        print("El correo '{}' es válido.".format(correo))
    else:
        print("El correo '{}' es inválido.".format(correo))

    # Separador para distinguir resultados de cada correo
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
