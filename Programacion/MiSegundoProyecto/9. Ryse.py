import random

jugadores = {"11111111L":{"Nombre":"Pedro Martinez","dados":[],"puntos":4},
            "22222222K":{"Nombre":"Pedro Sanchez","dados":[],"puntos":5},
            "33333333S":{"Nombre":"Lola Indigo","dados":[],"puntos":2},
            "44444444L":{"Nombre":"Andres iniesta","dados":[],"puntos":5}}
cabecera = "Jugadores".center(40,"*")+"\n"+"DNI".ljust(10) + "Nombre".ljust(20) + "Puntos".rjust(10) + "\n"+"*"*40

lista_participantes = list(jugadores.keys())
while len(lista_participantes) > 1:
    lista_jugadores_aleatorios = []
    while len(lista_jugadores_aleatorios) < 2:
        num = random.randrange(len(lista_participantes))
        if lista_participantes[num] not in lista_jugadores_aleatorios:
            lista_jugadores_aleatorios.append((lista_participantes[num]))

    print(lista_jugadores_aleatorios)

    turno = random.randrange(2)
    for i in range(9):
        longitud_lista_dados = len(jugadores[lista_jugadores_aleatorios[turno%2]]["dados"])
        dados = random.randint(1, 6)
        if len(jugadores[lista_jugadores_aleatorios[turno%2]]["dados"]) == 0:
            jugadores[lista_jugadores_aleatorios[turno%2]]["dados"].append(dados)
        else:
            for j in range(len(jugadores[lista_jugadores_aleatorios[turno%2]]["dados"])):
                if dados > (jugadores[lista_jugadores_aleatorios[turno%2]]["dados"][j]):
                    jugadores[lista_jugadores_aleatorios[turno%2]]["dados"].insert(j, dados)
                    break
        if longitud_lista_dados == len((jugadores[lista_jugadores_aleatorios[turno%2]]["dados"])):
            jugadores[lista_jugadores_aleatorios[turno%2]]["dados"].append(dados)

    for i in range(6):
        longitud_lista_dados = len(jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"])
        dados = random.randint(1, 6)
        if len(jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"]) == 0:
            jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"].append(dados)
        else:
            for j in range(len(jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"])):
                if dados > (jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"][j]):
                    jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"].insert(j, dados)
                    break
        if longitud_lista_dados == len((jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"])):
            jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"].append(dados)

    print(jugadores[lista_jugadores_aleatorios[0]])
    print(jugadores[lista_jugadores_aleatorios[1]])

    for i in range(6):
        if jugadores[lista_jugadores_aleatorios[turno%2]]["dados"][i] > jugadores[lista_jugadores_aleatorios[(turno+1)%2]]["dados"][i]:
            jugadores[lista_jugadores_aleatorios[(turno + 1) % 2]]["puntos"] -= 1
        else:
            jugadores[lista_jugadores_aleatorios[turno % 2]]["puntos"] -= 1

        if jugadores[lista_jugadores_aleatorios[turno % 2]]["puntos"] == 0:
            print("Eliminamos a", lista_participantes[turno % 2])
            lista_participantes.remove(lista_jugadores_aleatorios[turno % 2])
            break
        if jugadores[lista_jugadores_aleatorios[(turno + 1) % 2]]["puntos"] == 0:
            print("Eliminamos a", lista_participantes[(turno + 1) % 2])
            lista_participantes.remove(lista_jugadores_aleatorios[(turno + 1) % 2])
            break

    #jugadores[lista_jugadores_aleatorios[turno % 2]]["dados"]
    #jugadores[lista_jugadores_aleatorios[(turno + 1) % 2]]["dados"]

    jugadores2 = list(jugadores.copy())
    #print(jugadores2)
    print(cabecera)
    for players in jugadores:
        nombre = (jugadores[players]["Nombre"])
        puntos = (jugadores[players]["puntos"])
        print(players.ljust(10) + nombre.ljust(20) + str(puntos).rjust(10))

    if len(lista_participantes) == 1:
        print()
    input("Enter")
