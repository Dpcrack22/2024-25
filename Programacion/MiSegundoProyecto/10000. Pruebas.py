ranking = "Manuel Casado:3:58;Alba Rodriguez:2:54;Esther Vallejo:10:49;Alvaro Ballejo:10:67"
datos = ""
menu_ranking = ("Ranking".center(50, "*")) + "\n" + "Nombre".ljust(25) + "Partidas".ljust(10) + "Puntos Totales".ljust(15) + "\n" + "*"*50 + "\n"
print(menu_ranking)
new_player = "Pedro Torres"
new_points = "50"
tmp_ranking = ranking + ";"
found = False

if new_player in tmp_ranking:
    for i in range(tmp_ranking.count(";")):
        if i == 0:
            ini = 0
            fin = tmp_ranking.find(";")
        else:
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]
        games = player[sep1 + 1:sep2]
        points = player[sep2 + 1:]
        if new_player == name:
            tmp_ranking = tmp_ranking[:ini] + name + ":" + str(int(games)+1) + ":" + str(int(points)+int(new_points)) + ";" + tmp_ranking[fin+1:]
            found = True
            break
else:
    for i in range(tmp_ranking.count(";")):
        if i == 0:
            ini = 0
            fin = tmp_ranking.find(";")
        else:
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]
        games = player[sep1 + 1:sep2]
        points = player[sep2 + 1:]
        if int(new_points) > int(points):
            tmp_ranking = tmp_ranking[:ini] + new_player + ":" + str(1) + ":" + str(new_points) + ";" + tmp_ranking[ini:]
            found = True
            break
    if not found:
        tmp_ranking += new_player + ":" + str(1) + ":" + str(new_points) + ";"

ranking_ordenado = ""
while tmp_ranking:
    max_points = -1
    max_player = ""
    ini_max = 0
    fin_max = 0
    for i in range(tmp_ranking.count(";")):
        if i == 0:
            ini = 0
            fin = tmp_ranking.find(";")
        else:
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        points = player[sep2 + 1:]
        if int(points) > max_points:
            max_points = int(points)
            max_player = player
            ini_max = ini
            fin_max = fin
    ranking_ordenado += max_player + ";"
    tmp_ranking = tmp_ranking[:ini_max] + tmp_ranking[fin_max + 1:]

tmp_ranking = ranking_ordenado



players = tmp_ranking.split(";")
for player in players:
    if player:
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]
        games = player[sep1 + 1:sep2]
        points = player[sep2 + 1:]
        print("{:<25} {:<10} {:<15}".format(name, games, points))
input("Enter: ")
tmp_ranking = ranking_ordenado
ranking_ordenado_por_partidas = ""
while tmp_ranking:
    max_games = -1
    max_player = ""
    ini_max = 0
    fin_max = 0
    for i in range(tmp_ranking.count(";")):
        if i == 0:
            ini = 0
            fin = tmp_ranking.find(";")
        else:
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        games = player[sep1 + 1:sep2]
        if int(games) > max_games:
            max_games = int(games)
            max_player = player
            ini_max = ini
            fin_max = fin
    ranking_ordenado_por_partidas += max_player + ";"
    tmp_ranking = tmp_ranking[:ini_max] + tmp_ranking[fin_max + 1:]

tmp_ranking = ranking_ordenado_por_partidas

print("\n" + ("Ranking Ordenado por Partidas Jugadas").center(50, "*"))
print(("{:<25} {:<10} {:<15}".format("Nombre", "Partidas", "Puntos Totales")))
print("*" * 50)

players = tmp_ranking.split(";")
for player in players:
    if player:
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]
        games = player[sep1 + 1:sep2]
        points = player[sep2 + 1:]
        print("{:<25} {:<10} {:<15}".format(name, games, points))

input("Enter:")
