
ranking = "Manuel Casado:3:58;Alba Rodriguez:2:54;Esther Vallejo:10:49;Alvaro Ballejo:10:67"
datos = ""
menu_ranking = ("Ranking".center(50, "*")) + "\n" + "Nombre".ljust(25) + "Partidas".ljust(10) + "Puntos Totales".ljust(15) + "\n" + "*"*50 + "\n"
print(menu_ranking)
new_player = "Pedro Torres"
new_points = "50"
tmp_ranking = ranking + ";"
if new_player in tmp_ranking:
    print("Incrementamos partidas y puntos")

    for i in range(tmp_ranking.count(";")):
        if i == 0:
            ini = 0
            fin = tmp_ranking.find(";")
        else:
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)
        print(tmp_ranking[ini:fin])
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]
        games = player[sep1 + 1:sep2]
        points = player[sep2 + 1:]
        if new_player == name:
            tmp_ranking = tmp_ranking[:ini] + name + ":" + str(int(games)+1) + ":" + str(int(points)+new_points) + ";" + tmp_ranking[fin+1:]


else:
    print("Lo añadimos")
    for i in range(tmp_ranking.count(";")):
        if i == 0:
            ini = 0
            fin = tmp_ranking.find(";")
        else:
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)
        print(tmp_ranking[ini:fin])
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]
        games = player[sep1 + 1:sep2]
        points = player[sep2 + 1:]
        if int(new_points) > int(points):
            tmp_ranking = tmp_ranking[:ini] + new_player + ":" + str(1) + ":" + str(new_points) + ";" + tmp_ranking[ini:]
            break
print(tmp_ranking)
input("Enter:")



tmp_ranking = ranking + ";"
for i in range(tmp_ranking.count(";")):
    if i == 0:
        ini = 0
        fin = tmp_ranking.find(";")
    else:
        ini = fin + 1
        fin = tmp_ranking.find(";",ini)
    print(tmp_ranking[ini:fin])
    player = tmp_ranking[ini:fin]
    sep1 = player.find(":")
    sep2 = player.find(":",sep1 + 1)
    name = player[:sep1]
    games = player[sep1+1:sep2]
    points = player[sep2 +1:]