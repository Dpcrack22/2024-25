# Cadena inicial con información de los jugadores en el formato "Nombre:Partidas:Puntos"
ranking = "Manuel Casado:3:58;Alba Rodriguez:2:54;Esther Vallejo:10:49;Alvaro Ballejo:10:67"
datos = ""  # Variable auxiliar para almacenar datos adicionales (no se usa en este código)

# Generamos el encabezado del menú de ranking
menu_ranking = ("Ranking".center(50, "*")) + "\n" + "Nombre".ljust(25) + "Partidas".ljust(10) + "Puntos Totales".ljust(15) + "\n" + "*" * 50 + "\n"
print(menu_ranking)  # Mostramos el menú inicial

# Datos del nuevo jugador
new_player = "Pedro Torres"  # Nombre del nuevo jugador a agregar o actualizar
new_points = "50"  # Puntos del nuevo jugador

# Se añade un separador al final del ranking para facilitar el manejo de datos
tmp_ranking = ranking + ";"

# Verificamos si el nuevo jugador ya está en el ranking
if new_player in tmp_ranking:
    print("Incrementamos partidas y puntos")  # Mensaje informativo

    # Recorremos los jugadores del ranking para actualizar sus datos si coincide con el nuevo jugador
    for i in range(tmp_ranking.count(";")):  # Iteramos por cada jugador usando el número de separadores (;)
        if i == 0:  # Caso especial para el primer jugador
            ini = 0
            fin = tmp_ranking.find(";")
        else:  # Para los demás jugadores
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)

        print(tmp_ranking[ini:fin])  # Mostramos al jugador actual (para depuración)

        # Extraemos datos del jugador actual
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]  # Nombre del jugador
        games = player[sep1 + 1:sep2]  # Número de partidas
        points = player[sep2 + 1:]  # Puntos totales

        # Si encontramos al nuevo jugador, actualizamos sus datos
        if new_player == name:
            # Actualizamos partidas y puntos del jugador
            tmp_ranking = tmp_ranking[:ini] + name + ":" + str(int(games) + 1) + ":" + str(int(points) + int(new_points)) + ";" + tmp_ranking[fin + 1:]

else:
    print("Lo añadimos")  # Mensaje informativo

    # Recorremos el ranking para insertar al nuevo jugador en el lugar correspondiente
    for i in range(tmp_ranking.count(";")):
        if i == 0:  # Caso especial para el primer jugador
            ini = 0
            fin = tmp_ranking.find(";")
        else:  # Para los demás jugadores
            ini = fin + 1
            fin = tmp_ranking.find(";", ini)

        print(tmp_ranking[ini:fin])  # Mostramos al jugador actual (para depuración)

        # Extraemos datos del jugador actual
        player = tmp_ranking[ini:fin]
        sep1 = player.find(":")
        sep2 = player.find(":", sep1 + 1)
        name = player[:sep1]  # Nombre del jugador
        games = player[sep1 + 1:sep2]  # Número de partidas
        points = player[sep2 + 1:]  # Puntos totales

        # Si los puntos del nuevo jugador son mayores que los del jugador actual, lo insertamos aquí
        if int(new_points) > int(points):
            tmp_ranking = tmp_ranking[:ini] + new_player + ":" + str(1) + ":" + str(new_points) + ";" + tmp_ranking[ini:]
            break  # Salimos del bucle una vez insertado

# Mostramos el ranking actualizado
print(tmp_ranking)

# Esperamos entrada del usuario antes de finalizar
input("Enter:")

# Recorremos de nuevo el ranking para mostrar los jugadores
tmp_ranking = ranking + ";"
for i in range(tmp_ranking.count(";")):
    if i == 0:  # Caso especial para el primer jugador
        ini = 0
        fin = tmp_ranking.find(";")
    else:  # Para los demás jugadores
        ini = fin + 1
        fin = tmp_ranking.find(";", ini)

    print(tmp_ranking[ini:fin])  # Mostramos al jugador actual (para depuración)

    # Extraemos datos del jugador actual
    player = tmp_ranking[ini:fin]
    sep1 = player.find(":")
    sep2 = player.find(":", sep1 + 1)
    name = player[:sep1]  # Nombre del jugador
    games = player[sep1 + 1:sep2]  # Número de partidas
    points = player[sep2 + 1:]  # Puntos totales
