import random

jugadores = {"999999999Y": {"nombre": "Pedrito casador", "Puntos": 0, "dados": []},
             "888888888Y": {"nombre": "Manolo casador", "Puntos": 0, "dados": []},
             "999929999Y": {"nombre": "Alexis Texas", "Puntos": 0, "dados": []},
             "885588888Y": {"nombre": "Scarlet jonny", "Puntos": 0, "dados": []}
             }
ranking = "Ranking".center(41, "*") + "\n" + "Dni".ljust(10) + "Nombre".ljust(20) + "Puntos".rjust(11) + "\n" + "*" * 41
puntos_maximos = 0
lista_ordenada = []
lista_inicial = list(jugadores.keys())

num_dados = 10
#print("a")
while puntos_maximos < 20:
    #print("aaa")
    lista_jugadores_elatorios = []
    while len(lista_jugadores_elatorios) != 2:
        num = random.randrange(4)
        if lista_inicial[num] not in lista_jugadores_elatorios:
            lista_jugadores_elatorios.append(lista_inicial[num])
    print(lista_jugadores_elatorios)
    for k in range(2):
        for i in range(num_dados):
            longitud_lista_dados = len(jugadores[lista_jugadores_elatorios[k]]["dados"])
            dado = random.randint(1, 6)
            if len(jugadores[lista_jugadores_elatorios[k]]["dados"]) == 0:
                jugadores[lista_jugadores_elatorios[k]]["dados"].append(dado)
            else:
                for j in range(len(jugadores[lista_jugadores_elatorios[k]]["dados"])):
                    if dado > jugadores[lista_jugadores_elatorios[k]]["dados"][j]:
                        jugadores[lista_jugadores_elatorios[k]]["dados"].insert(j, dado)
                        break
            if longitud_lista_dados == len(jugadores[lista_jugadores_elatorios[k]]["dados"]):
                jugadores[lista_jugadores_elatorios[k]]["dados"].append(dado)
        print(jugadores[lista_jugadores_elatorios[k]]["dados"])

    input("Enter to continue...")
    for i in range(num_dados):
        if jugadores[lista_jugadores_elatorios[0]]["dados"][i] > jugadores[lista_jugadores_elatorios[1]]["dados"][i]:
            jugadores[lista_jugadores_elatorios[0]]["Puntos"] += 1
        elif jugadores[lista_jugadores_elatorios[0]]["dados"][i] < jugadores[lista_jugadores_elatorios[1]]["dados"][i]:
            jugadores[lista_jugadores_elatorios[1]]["Puntos"] += 1

    for k in range(2):
        if jugadores[lista_jugadores_elatorios[k]]["Puntos"] > puntos_maximos:
            puntos_maximos = jugadores[lista_jugadores_elatorios[k]]["Puntos"]
        jugadores[lista_jugadores_elatorios[k]]["dados"].clear()
        nombre = jugadores[lista_jugadores_elatorios[k]]["nombre"]
        dados = ""
        #for l in jugadores[lista_jugadores_elatorios[k]]["dados"]:

    print("Puntos maximos: ", puntos_maximos)
    print("Jugador 1:", jugadores[lista_jugadores_elatorios[1]]["Puntos"])
    print("Jugador 2:", jugadores[lista_jugadores_elatorios[0]]["Puntos"])