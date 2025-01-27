# Diccionario inicial con datos de los jugadores
jugadores = {
    "11111111L": {"Nombre": "Pedro Martinez", "dados": [], "vida": 100, "puntos": 2},
    "22222222K": {"Nombre": "Pedro Sanchez", "dados": [], "vida": 100, "puntos": 22},
    "33333333S": {"Nombre": "Zola Indigo", "dados": [], "vida": 130, "puntos": 12},
    "44444444L": {"Nombre": "Andres Iniesta", "dados": [], "vida": 300, "puntos": 233},
    "4442444L": {"Nombre": "Bebecita", "dados": [], "vida": 300, "puntos": 233},
    "4444144L": {"Nombre": "Xavier", "dados": [], "vida": 300, "puntos": 233},
}

# Bucle principal que permite al usuario interactuar repetidamente con el menú
while True:
    # Mostrar las opciones disponibles
    print("1) Buscar por Nombre")
    print("2) Buscar por DNI")
    print("3) Salir")
    opc = input("Elige una opción: ")  # Solicitar al usuario que elija una opción

    # Opción 1: Buscar por Nombre
    if opc == "1":
        # Solicitar al usuario el nombre a buscar
        nombre = input("Introduce el nombre a buscar: ").lower()  # Convertir a minúsculas para búsqueda insensible a mayúsculas
        encontrado = False  # Variable para verificar si se encuentra un jugador

        # Recorrer el diccionario de jugadores
        for dni, datos in jugadores.items():
            # Usar el método .find() para buscar coincidencias parciales en el nombre
            if datos["Nombre"].lower().find(nombre) != -1:  # Comprobar si el nombre contiene la búsqueda
                print(f"DNI: {dni}, Datos: {datos}")  # Mostrar los datos del jugador encontrado
                encontrado = True  # Marcar como encontrado

        # Si no se encuentra ningún jugador con el nombre proporcionado
        if not encontrado:
            print("No se encontró ningún jugador con ese nombre.")

    # Opción 2: Buscar por DNI
    elif opc == "2":
        # Solicitar al usuario el DNI a buscar
        dni = input("Introduce el DNI a buscar: ")
        encontrado = False  # Variable para verificar si se encuentra un jugador

        # Recorrer el diccionario de jugadores
        for llave, valor in jugadores.items():
            # Usar el método .find() para buscar coincidencias parciales en el DNI
            if llave.find(dni) != -1:  # Comprobar si el DNI contiene la búsqueda
                print(f"DNI: {llave}, Datos: {valor}")  # Mostrar los datos del jugador encontrado
                encontrado = True  # Marcar como encontrado

        # Si no se encuentra ningún jugador con el DNI proporcionado
        if not encontrado:
            print("No se encontró ningún jugador con ese DNI.")

    # Opción 3: Salir del programa
    elif opc == "3":
        print("Saliendo del programa...")  # Mensaje de salida
        break  # Finalizar el bucle y salir del programa

    # Manejo de opciones inválidas
    else:
        print("Opción inválida. Intenta nuevamente.")  # Mostrar mensaje de error si la opción no es válida
