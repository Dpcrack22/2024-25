import random
# Diccionario base con los jugadores: DNI como clave y nombre como valor
base_jugadores = {
    "11111111L": "Pedro Martinez",
    "22222222K": "Pedro Sanchez",
    "33333333S": "Lola Indigo",
    "44444444L": "Andres Iniesta"
}

# Diccionario para el ranking, donde se almacenarán las estadísticas de cada jugador
ranking_risk = {}

# Cabecera que se mostrará en el ranking para la salida por pantalla
cabecera = (
        "Jugadores".center(40, "*") + "\n"  # Centra el título "Jugadores" en 40 caracteres con. asteriscos
        + "Nombre".ljust(20) + "Partidas".rjust(10) + "Puntos".rjust(10) + "\n"  # Ajusta el formato de las columnas
        + "*" * 40  # Línea de separación
)

# Definición del máximo de puntos necesarios para ganar
maximo_puntos = 100

# Número de dados que se usan en cada partida
numero_dados = 10

# Variable que indica si el juego sigue en curso
juego_en_curso = True

# Bucle principal que mantiene el juego activo hasta que alguien alcance el máximo de puntos
while juego_en_curso:
    # Selección aleatoria de dos jugadores para cada partida
    jugadores_partida = random.sample(list(base_jugadores.keys()), 2)
    print(
        f"\nJugadores seleccionados para esta partida: {base_jugadores[jugadores_partida[0]]} y {base_jugadores[jugadores_partida[1]]}")

    # Lanzamiento de dados para los dos jugadores, generando 10 dados para cada uno
    dados_jugador_1 = sorted([random.randint(1, 6) for _ in range(numero_dados)], reverse=True)
    dados_jugador_2 = sorted([random.randint(1, 6) for _ in range(numero_dados)], reverse=True)

    # Inicialización de puntos para ambos jugadores
    puntos_jugador_1 = 0
    puntos_jugador_2 = 0

    # Comparación de los dados lanzados por cada jugador
    for i in range(numero_dados):
        if dados_jugador_1[i] > dados_jugador_2[i]:
            puntos_jugador_1 += 1
        elif dados_jugador_1[i] < dados_jugador_2[i]:
            puntos_jugador_2 += 1

    # Determinación del ganador de la ronda en base a los puntos obtenidos
    if puntos_jugador_1 > puntos_jugador_2:
        ganador_dni = jugadores_partida[0]
        ganador_puntos = puntos_jugador_1
    elif puntos_jugador_1 < puntos_jugador_2:
        ganador_dni = jugadores_partida[1]
        ganador_puntos = puntos_jugador_2
    else:
        ganador_dni = None  # Si hay empate, no se asigna un ganador
        print("Empate en esta ronda, no se asignan puntos adicionales.")

    # Si hay un ganador, actualizamos su puntaje y el número de partidas jugadas en el ranking
    if ganador_dni:
        if ganador_dni not in ranking_risk:
            # Si el jugador no está en el ranking, lo agregamos con su primer punto
            ranking_risk[ganador_dni] = {"games": 1, "points": ganador_puntos}
        else:
            # Si ya está en el ranking, incrementamos las partidas y los puntos
            ranking_risk[ganador_dni]["games"] += 1
            ranking_risk[ganador_dni]["points"] += ganador_puntos
        print(f"Ganador de la ronda: {base_jugadores[ganador_dni]} con {ganador_puntos} puntos.")

    # Si un jugador alcanza el límite de puntos, terminamos el juego
    if ganador_dni and ranking_risk[ganador_dni]["points"] >= maximo_puntos:
        juego_en_curso = False

    # Muestra el ranking ordenado por puntos
    print("\nRanking Actualizado por Puntos".center(40, "*"))
    print(cabecera)
    ranking_ordenado_puntos = sorted(ranking_risk.items(), key=lambda x: x[1]["points"], reverse=True)
    for dni, stats in ranking_ordenado_puntos:
        nombre = base_jugadores[dni]
        games = stats["games"]
        points = stats["points"]
        print(nombre.ljust(20) + str(games).rjust(10) + str(points).rjust(10))

    # Muestra el ranking ordenado por partidas jugadas
    print("\nRanking Actualizado por Partidas".center(40, "*"))
    print(cabecera)
    ranking_ordenado_partidas = sorted(ranking_risk.items(), key=lambda x: x[1]["games"], reverse=True)
    for dni, stats in ranking_ordenado_partidas:
        nombre = base_jugadores[dni]
        games = stats["games"]
        points = stats["points"]
        print(nombre.ljust(20) + str(games).rjust(10) + str(points).rjust(10))

    # Si el juego sigue, pide al usuario presionar Enter para continuar
    if juego_en_curso:
        input("\nPresiona Enter para continuar...")

# Al finalizar el juego, mostramos los rankings finales por puntos y por partidas
print("\n" + "Ranking Final por Puntos".center(40, "*"))
print(cabecera)
for dni, stats in ranking_ordenado_puntos:
    nombre = base_jugadores[dni]
    games = stats["games"]
    points = stats["points"]
    print(nombre.ljust(20) + str(games).rjust(10) + str(points).rjust(10))

print("\n" + "Ranking Final por Partidas".center(40, "*"))
print(cabecera)
for dni, stats in ranking_ordenado_partidas:
    nombre = base_jugadores[dni]
    games = stats["games"]
    points = stats["points"]
    print(nombre.ljust(20) + str(games).rjust(10) + str(points).rjust(10))
