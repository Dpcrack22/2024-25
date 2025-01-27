# Diccionario inicial con datos de los jugadores: clave = DNI, valores = nombre, dados, vida y puntos
jugadores = {
    "11111111L": {"Nombre": "Pedro Martinez", "dados": [], "vida": 100, "puntos": 2},
    "22222222K": {"Nombre": "Pedro Sanchez", "dados": [], "vida": 100, "puntos": 22},
    "33333333S": {"Nombre": "Zola Indigo", "dados": [], "vida": 130, "puntos": 12},
    "44444444L": {"Nombre": "Andres iniesta", "dados": [], "vida": 300, "puntos": 233},
    "4442444L": {"Nombre": "Bebecita", "dados": [], "vida": 300, "puntos": 233},
    "4444144L": {"Nombre": "Xavier", "dados": [], "vida": 300, "puntos": 233},
}

# Bucle principal que permite al usuario interactuar repetidamente
while True:
    # Menú de opciones para el usuario
    print("1) Buscar por Nombre")
    print("2) Buscar por DNI")
    print("3) Salir")
    opc = input("Elige una opción: ")  # Entrada del usuario para elegir una opción

    # Opción 1: Buscar jugadores por su nombre (o parte del nombre)
    if opc == "1":
        nombre = input("Introduce el nombre a buscar: ").lower()  # Entrada de búsqueda, convertida a minúsculas
        encontrado = False  # Variable de control para saber si se encuentra un jugador
        for dni, datos in jugadores.items():  # Iteramos sobre el diccionario
            if nombre in datos["Nombre"].lower():  # Comparación ignorando mayúsculas
                print(f"DNI: {dni}, Datos: {datos}")  # Mostramos el DNI y los datos del jugador
                encontrado = True  # Marcamos como encontrado
        if not encontrado:  # Si no se encontró ningún jugador
            print("No se encontró ningún jugador con ese nombre.")

    # Opción 2: Buscar jugadores por su DNI
    elif opc == "2":
        dni = input("Introduce el DNI a buscar: ")  # Entrada del DNI a buscar
        encontrado = False  # Variable de control para saber si se encuentra un jugador
        for llave, valor in jugadores.items():  # Iteramos sobre el diccionario
            if llave == dni:  # Comparamos el DNI buscado con la clave actual
                print(f"DNI: {llave}, Datos: {valor}")  # Mostramos el DNI y los datos del jugador
                encontrado = True  # Marcamos como encontrado
        if not encontrado:  # Si no se encontró ningún jugador con ese DNI
            print("No se encontró ningún jugador con ese DNI.")

    # Opción 3: Salir del programa
    elif opc == "3":
        print("Saliendo del programa...")  # Mensaje de salida
        break  # Rompemos el bucle para finalizar el programa

    # Manejo de entrada no válida
    else:
        print("Opción inválida. Intenta nuevamente.")  # Mensaje de error para opciones no válidas
