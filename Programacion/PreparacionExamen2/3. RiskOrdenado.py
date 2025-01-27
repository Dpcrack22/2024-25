# Base de datos de jugadores y sus datos de ranking
base_datos_jugadores = {
    "11111111A": "Ana García",
    "22222222B": "Carla Sanders",
    "33333333C": "Pau Gómez",
    "44444444D": "Marcos Torres"
}

ranking_risk = {
    "11111111A": {"games": 3, "points": 25},
    "22222222B": {"games": 1, "points": 35},
    "33333333C": {"games": 2, "points": 50}
}

# Lista de DNIs para ordenar
dnis_ranking = list(ranking_risk.keys())

# Ordenar por DNI (descendente)
for i in range(len(dnis_ranking) - 1):
    cambio = False
    for j in range(len(dnis_ranking) - (i + 1)):
        if dnis_ranking[j + 1] > dnis_ranking[j]:
            cambio = True
            aux = dnis_ranking[j + 1]
            dnis_ranking[j + 1] = dnis_ranking[j]
            dnis_ranking[j] = aux
    if not cambio:
        break

# Mostrar ranking ordenado por DNI
print("Ordenado por DNI")
datos = ""
for dni in dnis_ranking:
    datos += dni.ljust(10) + base_datos_jugadores[dni].ljust(20)
    datos += str(ranking_risk[dni]["games"]).rjust(10)
    datos += str(ranking_risk[dni]["points"]).rjust(10) + "\n"

cabecera = "RANKING RISK".center(50, "*") + "\n"
cabecera += "DNI".ljust(10) + "Name".ljust(20) + "Games".rjust(10) + "Points".rjust(10) + "\n"
cabecera += "*" * 50 + "\n"
print(cabecera + datos)

# Ordenar por puntos (descendente)
for i in range(len(dnis_ranking) - 1):
    cambio = False
    for j in range(len(dnis_ranking) - (i + 1)):
        if ranking_risk[dnis_ranking[j + 1]]["points"] > ranking_risk[dnis_ranking[j]]["points"]:
            cambio = True
            aux = dnis_ranking[j + 1]
            dnis_ranking[j + 1] = dnis_ranking[j]
            dnis_ranking[j] = aux
    if not cambio:
        break

# Mostrar ranking ordenado por puntos
print("Ordenado por puntos")
datos = ""
for dni in dnis_ranking:
    datos += dni.ljust(10) + base_datos_jugadores[dni].ljust(20)
    datos += str(ranking_risk[dni]["games"]).rjust(10)
    datos += str(ranking_risk[dni]["points"]).rjust(10) + "\n"

print(cabecera + datos)

# Ordenar por partidas (descendente)
for i in range(len(dnis_ranking) - 1):
    cambio = False
    for j in range(len(dnis_ranking) - (i + 1)):
        if ranking_risk[dnis_ranking[j + 1]]["games"] > ranking_risk[dnis_ranking[j]]["games"]:
            cambio = True
            aux = dnis_ranking[j + 1]
            dnis_ranking[j + 1] = dnis_ranking[j]
            dnis_ranking[j] = aux
    if not cambio:
        break

# Mostrar ranking ordenado por partidas
print("Ordenado por partidas")
datos = ""
for dni in dnis_ranking:
    datos += dni.ljust(10) + base_datos_jugadores[dni].ljust(20)
    datos += str(ranking_risk[dni]["games"]).rjust(10)
    datos += str(ranking_risk[dni]["points"]).rjust(10) + "\n"

print(cabecera + datos)
