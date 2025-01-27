import random  # Importamos la librería para generar números aleatorios

# Diccionario con información de los jugadores: DNI como clave, y valores con nombre, lista de dados y puntos
jugadores = {
    "11111111L": {"Nombre": "Pedro Martinez", "dados": [], "puntos": 0},
    "22222222K": {"Nombre": "Pedro Sanchez", "dados": [], "puntos": 0},
    "33333333S": {"Nombre": "Lola Indigo", "dados": [], "puntos": 0},
    "44444444L": {"Nombre": "Andres Iniesta", "dados": [], "puntos": 0}
}

# Cabecera para mostrar la tabla de jugadores en un formato legible
cabecera = "Jugadores".center(40, "*") + "\n" + "DNI".ljust(10) + "Nombre".ljust(20) + "Puntos".rjust(10) + "\n" + "*" * 40

maximo_puntos = 0  # Variable para controlar cuando un jugador alcanza los puntos necesarios para finalizar
lista_inicial = list(jugadores.keys())  # Lista de DNIs de los jugadores
numero_dados = 10  # Número de dados que tirará cada jugador

# Bucle principal: continúa mientras ningún jugador tenga 20 o más puntos
while maximo_puntos < 20:

    lista_jugadores_aleatorios = []  # Lista para almacenar los jugadores que participarán en la ronda actual

    # Seleccionamos aleatoriamente dos jugadores únicos para competir
    while len(lista_jugadores_aleatorios) != 2:
        num = random.randrange(4)  # Generamos un índice aleatorio entre 0 y 3
        if lista_inicial[num] not in lista_jugadores_aleatorios:  # Verificamos que no esté repetido
            lista_jugadores_aleatorios.append(lista_inicial[num])

    print(lista_jugadores_aleatorios)  # Mostramos los jugadores seleccionados (para depuración)

    # Cada jugador tira sus dados
    for k in range(2):  # Iteramos sobre los dos jugadores seleccionados
        for i in range(numero_dados):  # Cada jugador tira el número de dados especificado
            longitud_lista_dados = len(jugadores[lista_jugadores_aleatorios[k]]["dados"])
            dados = random.randint(1, 6)  # Generamos un valor aleatorio de dado entre 1 y 6

            # Insertamos el dado en la lista del jugador en orden descendente
            if len(jugadores[lista_jugadores_aleatorios[k]]["dados"]) == 0:
                jugadores[lista_jugadores_aleatorios[k]]["dados"].append(dados)
            else:
                for j in range(len(jugadores[lista_jugadores_aleatorios[k]]["dados"])):
                    if dados > jugadores[lista_jugadores_aleatorios[k]]["dados"][j]:
                        jugadores[lista_jugadores_aleatorios[k]]["dados"].insert(j, dados)
                        break

            # Si no se insertó en el bucle anterior, añadimos al final
            if longitud_lista_dados == len(jugadores[lista_jugadores_aleatorios[k]]["dados"]):
                jugadores[lista_jugadores_aleatorios[k]]["dados"].append(dados)

    # Comparamos los dados de ambos jugadores para asignar puntos
    for i in range(numero_dados):
        if jugadores[lista_jugadores_aleatorios[0]]["dados"][i] > jugadores[lista_jugadores_aleatorios[1]]["dados"][i]:
            jugadores[lista_jugadores_aleatorios[0]]["puntos"] += 1
        elif jugadores[lista_jugadores_aleatorios[0]]["dados"][i] < jugadores[lista_jugadores_aleatorios[1]]["dados"][i]:
            jugadores[lista_jugadores_aleatorios[1]]["puntos"] += 1

    # Actualizamos el máximo de puntos
    for k in range(2):
        if jugadores[lista_jugadores_aleatorios[k]]["puntos"] > maximo_puntos:
            maximo_puntos = jugadores[lista_jugadores_aleatorios[k]]["puntos"]

        # Limpiamos los dados del jugador para la próxima ronda
        jugadores[lista_jugadores_aleatorios[k]]["dados"].clear()

    # Mostramos la tabla ordenada por puntos
    print(cabecera)
    for players in jugadores:
        nombre = jugadores[players]["Nombre"]
        puntos = jugadores[players]["puntos"]
        print(players.ljust(10) + nombre.ljust(20) + str(puntos).rjust(10))

    # Pausamos el programa para continuar la próxima ronda
    input("Enter para continuar: ")
