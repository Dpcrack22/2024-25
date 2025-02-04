# Lista de jugadores, donde cada jugador es una lista con su DNI y nombre
jugadores2 = [["11411111L", "Manolo"], ["44444444L", "Jose"], ["44444444A", "Angelao"]]
lista_jugadores_encontrados = []  # Lista donde se almacenarán los jugadores encontrados

while True:
    lista_jugadores_encontrados = []  # Limpiar la lista de jugadores encontrados al inicio de cada iteración

    # Mostrar las opciones del menú al usuario
    print("1) Buscar por Nombre")
    print("2) Buscar por DNI")
    print("3) Salir")
    opc = input("Elige una opción: ")

    # Opción 1: Buscar por Nombre
    if opc == "1":
        name = input("Introduce el nombre: ").lower()  # Pedimos el nombre en minúsculas para hacer la búsqueda case-insensitive
        print("Usuarios encontrados:")
        # Iteramos sobre la lista de jugadores para buscar el nombre ingresado
        for i in range(len(jugadores2)):
            if name in jugadores2[i][1].lower():  # Comprobamos si el nombre contiene el texto ingresado (sin distinguir mayúsculas)
                lista_jugadores_encontrados.append(jugadores2[i])  # Si se encuentra, agregamos el jugador a la lista

    # Opción 2: Buscar por DNI
    elif opc == "2":
        dni = input("Introduce el DNI: ")
        print("Usuarios encontrados:")
        # Iteramos sobre la lista de jugadores para buscar el DNI ingresado
        for i in range(len(jugadores2)):
            if dni in jugadores2[i][0]:  # Comprobamos si el DNI contiene el texto ingresado
                lista_jugadores_encontrados.append(jugadores2[i])  # Si se encuentra, agregamos el jugador a la lista

    # Mostrar los jugadores encontrados ordenados por nombre
    print("Ordenamos por nombre".center(40, "*"))
    # Ordenamos la lista `lista_jugadores_encontrados` por el nombre (índice 1 de cada sublista) utilizando el método de ordenamiento de burbuja
    for i in range(len(lista_jugadores_encontrados) - 1):
        for j in range(len(lista_jugadores_encontrados) - 1 - i):
            if lista_jugadores_encontrados[j][1] > lista_jugadores_encontrados[j + 1][1]:
                # Si el nombre del jugador actual es mayor que el del siguiente, los intercambiamos
                aux = lista_jugadores_encontrados[j]
                lista_jugadores_encontrados[j] = lista_jugadores_encontrados[j + 1]
                lista_jugadores_encontrados[j + 1] = aux

    print("Ordenado ya")
    # Imprimir los jugadores encontrados ordenados por nombre
    for i in range(len(lista_jugadores_encontrados)):
        dni = lista_jugadores_encontrados[i][0]
        nombre = lista_jugadores_encontrados[i][1]
        print(dni.ljust(15) + nombre.ljust(15))  # Mostramos el DNI y el nombre alineados

    # Mostrar los jugadores encontrados ordenados por DNI
    print("Ordenamos por DNI".center(30, "*"))
    # Ordenamos la lista `lista_jugadores_encontrados` por el DNI (índice 0 de cada sublista) utilizando el método de ordenamiento de burbuja
    for i in range(len(lista_jugadores_encontrados) - 1):
        for j in range(len(lista_jugadores_encontrados) - 1 - i):
            if lista_jugadores_encontrados[j][0] > lista_jugadores_encontrados[j + 1][0]:
                # Si el DNI del jugador actual es mayor que el del siguiente, los intercambiamos
                aux = lista_jugadores_encontrados[j]
                lista_jugadores_encontrados[j] = lista_jugadores_encontrados[j + 1]
                lista_jugadores_encontrados[j + 1] = aux

    print("Ordenado ya")
    # Imprimir los jugadores encontrados ordenados por DNI
    for i in range(len(lista_jugadores_encontrados)):
        dni = lista_jugadores_encontrados[i][0]
        nombre = lista_jugadores_encontrados[i][1]
        print(dni.ljust(15) + nombre.ljust(15))  # Mostramos el DNI y el nombre alineados
