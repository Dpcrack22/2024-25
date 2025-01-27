# Lista que contiene todos los correos, tanto válidos como inválidos, en una sola variable
correos = [
    "a@b.com", "a.b@c.com", "a.b@c.d.es",
    ".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com",
    "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com", "awer@wer.com",
    "awer@wer.commmm", "..@wer.commmm"
]

# Proceso para validar cada correo sin usar funciones definidas con `def`
print("Resultado de la validación de correos:")
for correo in correos:
    # Buscamos la posición de la arroba (@), que es necesaria para dividir el correo en usuario y dominio
    ini = correo.find("@")

    # Comprobamos que la arroba esté presente y que no esté al principio del correo
    if ini == -1 or ini == 0:
        print(f"{correo}: No válido")  # Si no hay arroba o está al inicio, el correo es inválido
        continue  # Saltamos al siguiente correo en la lista

    # Dividimos el correo en dos partes: usuario y dominio
    usuario = correo[:ini]  # Parte antes de la arroba (@)
    dominio = correo[ini + 1:]  # Parte después de la arroba (@)

    # Comenzamos la validación del usuario, asegurándonos de que sea alfanumérico y sin puntos consecutivos
    es_valido = True  # Suponemos que es válido hasta que se demuestre lo contrario
    for i in range(len(usuario)):
        # Verificamos que cada carácter sea alfanumérico o un punto
        if not (usuario[i].isalnum() or usuario[i] == "."):
            es_valido = False  # Si no es alfanumérico ni punto, es inválido
            break  # Terminamos la validación del usuario

        # Comprobamos que no haya puntos consecutivos en el usuario
        if i > 0 and usuario[i] == "." and usuario[i - 1] == ".":
            es_valido = False  # Si hay puntos consecutivos, es inválido
            break  # Terminamos la validación del usuario

    # Iniciamos la validación del dominio
    puntos = 0  # Contador para verificar que hay al menos un punto en el dominio
    for i in range(len(dominio)):
        # Verificamos que cada carácter en el dominio sea alfanumérico o un punto
        if not (dominio[i].isalnum() or dominio[i] == "."):
            es_valido = False  # Si hay un carácter no válido, el correo es inválido
            break  # Terminamos la validación del dominio

        # Verificamos las posiciones de los puntos en el dominio
        if dominio[i] == ".":
            # Si el dominio comienza, termina o tiene puntos consecutivos, es inválido
            if i == 0 or i == len(dominio) - 1 or dominio[i - 1] == ".":
                es_valido = False
                break  # Terminamos la validación del dominio
            puntos += 1  # Contamos los puntos válidos en el dominio

    # Validación final: verificamos que haya al menos un punto en el dominio
    if puntos < 1:
        es_valido = False  # Si no hay puntos en el dominio, el correo es inválido

    # Imprimimos el resultado final de la validación para cada correo
    print(f"{correo}: {'Válido' if es_valido else 'No válido'}")
