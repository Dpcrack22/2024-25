#Si gana cierto jugador, incluir en ranking mostrar por partidas y por puntos
import random

base_jugadores = {
    "11111111L": "Pedro Martinez",
    "22222222K": "Pedro Sanchez",
    "33333333S": "Lola Indigo",
    "44444444L": "Andres Iniesta"
}

ranking_risk = {}

cabecera = (
        "Jugadores".center(40, "*") + "\n"
        + "Nombre".ljust(20) + "Partidas".rjust(10) + "Puntos".rjust(10) + "\n"
        + "*" * 40
)

maximo_puntos = 100
numero_dados = 10
juego_en_curso = True

while juego_en_curso:
    jugadores_partida = random.sample(list(base_jugadores.keys()), 2)
    print(
        f"\nJugadores seleccionados para esta partida: {base_jugadores[jugadores_partida[0]]} y {base_jugadores[jugadores_partida[1]]}")

    dados_jugador_1 = sorted([random.randint(1, 6) for _ in range(numero_dados)], reverse=True)
    dados_jugador_2 = sorted([random.randint(1, 6) for _ in range(numero_dados)], reverse=True)

    puntos_jugador_1 = 0
    puntos_jugador_2 = 0

    for i in range(numero_dados):
        if dados_jugador_1[i] > dados_jugador_2[i]:
            puntos_jugador_1 += 1
        elif dados_jugador_1[i] < dados_jugador_2[i]:
            puntos_jugador_2 += 1

    if puntos_jugador_1 > puntos_jugador_2:
        ganador_dni = jugadores_partida[0]
        ganador_puntos = puntos_jugador_1
    elif puntos_jugador_1 < puntos_jugador_2:
        ganador_dni = jugadores_partida[1]
        ganador_puntos = puntos_jugador_2
    else:
        ganador_dni = None
        print("Empate en esta ronda, no se asignan puntos adicionales.")

    if ganador_dni:
        if ganador_dni not in ranking_risk:
            ranking_risk[ganador_dni] = {"games": 1, "points": ganador_puntos}
        else:
            ranking_risk[ganador_dni]["games"] += 1
            ranking_risk[ganador_dni]["points"] += ganador_puntos
        print(f"Ganador de la ronda: {base_jugadores[ganador_dni]} con {ganador_puntos} puntos.")

    if ganador_dni and ranking_risk[ganador_dni]["points"] >= maximo_puntos:
        juego_en_curso = False

    print("\nRanking Actualizado por Puntos".center(40, "*"))
    print(cabecera)
    ranking_ordenado_puntos = sorted(ranking_risk.items(), key=lambda x: x[1]["points"], reverse=True)
    for dni, stats in ranking_ordenado_puntos:
        nombre = base_jugadores[dni]
        games = stats["games"]
        points = stats["points"]
        print(nombre.ljust(20) + str(games).rjust(10) + str(points).rjust(10))

    print("\nRanking Actualizado por Partidas".center(40, "*"))
    print(cabecera)
    ranking_ordenado_partidas = sorted(ranking_risk.items(), key=lambda x: x[1]["games"], reverse=True)
    for dni, stats in ranking_ordenado_partidas:
        nombre = base_jugadores[dni]
        games = stats["games"]
        points = stats["points"]
        print(nombre.ljust(20) + str(games).rjust(10) + str(points).rjust(10))

    if juego_en_curso:
        input("\nPresiona Enter para continuar...")

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
