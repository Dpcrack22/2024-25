# Solicitamos al usuario que introduzca un correo.
correo = input("Dame un correo para verificar si es correcto o no: ")

# Buscamos la posición de la arroba (@) en el correo
ini = correo.find("@")

# Verificamos si no hay "@" o si está al inicio del correo
if ini == -1 or ini == 0:
    print("Este correo {} es incorrecto / no válido.".format(correo))

else:
    # Separamos el usuario (parte antes de la @) y el dominio (parte después de la @)
    usuario = correo[:ini]
    dominio = correo[ini + 1:]

    # Bandera que determinará si el correo es válido o no
    Valido = True

    # Validación de la parte de usuario (antes de la @)
    for j in range(len(usuario)):
        # Si el usuario contiene algo que no es alfanumérico o un punto, es inválido
        if not (usuario[j].isalnum() or usuario[j] == "."):
            Valido = False
            break
        # Si hay dos puntos consecutivos, es inválido
        if j > 0 and usuario[j] == "." and usuario[j - 1] == ".":
            Valido = False
            break

    # Inicializamos un contador de puntos en el dominio
    puntos = 0

    # Validación de la parte del dominio (después de la @)
    for j in range(len(dominio)):
        # El dominio debe ser alfanumérico o contener un punto
        if not (dominio[j].isalnum() or dominio[j] == "."):
            Valido = False
            break
        # Si el primer o último carácter es un punto, es inválido
        if dominio[j] == ".":
            if j == 0 or j == len(dominio) - 1 or dominio[j - 1] == ".":
                Valido = False
                break
            puntos += 1  # Contamos los puntos en el dominio

    # Si el dominio no contiene ningún punto, es inválido
    if puntos < 1:
        Valido = False

    # Mostramos si el correo es válido o no
    print(f"{correo}: {'Válido' if Valido else 'No válido'}")


# # Solicitamos al usuario que introduzca un correo.
# correo = input("Dame un correo para verificar si es correcto o no: ")
#
# # Buscamos la posición de la arroba (@) en el correo
# ini = correo.find("@")
#
# # Verificamos si no hay "@" o si está al inicio del correo
# if ini == -1 or ini == 0:
#     print("Este correo {} es incorrecto / no válido.".format(correo))
#
# else:
#     # Separamos el usuario (parte antes de la @) y el dominio (parte después de la @)
#     usuario = correo[:ini]
#     dominio = correo[ini + 1:]
#
#     # Bandera que determinará si el correo es válido o no
#     Valido = True
#     puntos_usuario = 0  # Contador para los puntos en la parte del usuario
#
#     # Validación de la parte de usuario (antes de la @)
#     for j in range(len(usuario)):
#         # Si el usuario contiene algo que no es alfanumérico o un punto, es inválido
#         if not (usuario[j].isalnum() or usuario[j] == "."):
#             Valido = False
#             break
#         # Si hay dos puntos consecutivos, es inválido
#         if j > 0 and usuario[j] == "." and usuario[j - 1] == ".":
#             Valido = False
#             break
#         # Contamos los puntos en el usuario
#         if usuario[j] == ".":
#             puntos_usuario += 1
#
#     # Si el usuario tiene más de 1 punto, es inválido
#     if puntos_usuario > 1:
#         Valido = False
#
#     # Inicializamos un contador de puntos en el dominio
#     puntos = 0
#
#     # Validación de la parte del dominio (después de la @)
#     for j in range(len(dominio)):
#         # El dominio debe ser alfanumérico o contener un punto
#         if not (dominio[j].isalnum() or dominio[j] == "."):
#             Valido = False
#             break
#         # Si el primer o último carácter es un punto, es inválido
#         if dominio[j] == ".":
#             if j == 0 or j == len(dominio) - 1 or dominio[j - 1] == ".":
#                 Valido = False
#                 break
#             puntos += 1  # Contamos los puntos en el dominio
#
#     # Si el dominio no contiene ningún punto, es inválido
#     if puntos < 1:
#         Valido = False
#
#     # Mostramos si el correo es válido o no
#     print(f"{correo}: {'Válido' if Valido else 'No válido'}")
