import random
jugadores = {"11111111L":{"Nombre":"Pedro Martinez","dados":[],"puntos":0},
            "22222222K":{"Nombre":"Pedro Sanchez","dados":[],"puntos":0},
            "33333333S":{"Nombre":"Lola Indigo","dados":[],"puntos":0},
            "44444444L":{"Nombre":"Andres iniesta","dados":[],"puntos":0}}
cabecera = "Jugadores".center(40,"*")+"\n"+"DNI".ljust(10) + "Nombre".ljust(20) + "Puntos".rjust(10) + "\n"+"*"*40

maximo_puntos = 0
lista_inicial = list(jugadores.keys())
numero_dados = 10

while maximo_puntos < 20:

    lista_jugadores_aleatorios = []


    while len(lista_jugadores_aleatorios) != 2:
        num = random.randrange(4)
        if lista_inicial[num] not in lista_jugadores_aleatorios:
            lista_jugadores_aleatorios.append(lista_inicial[num])
    print(lista_jugadores_aleatorios)
    #Probamos con un jugador que seria lista_jugadores_aleatorios[0]

    for k in range(2):
        for i in range(numero_dados):
            longitud_lista_dados = len(jugadores[lista_jugadores_aleatorios[k]]["dados"])
            dados = random.randint(1,6)
            if len(jugadores[lista_jugadores_aleatorios[k]]["dados"]) == 0:
                jugadores[lista_jugadores_aleatorios[k]]["dados"].append(dados)
            else:
                for j in range(len(jugadores[lista_jugadores_aleatorios[k]]["dados"])):
                    if dados > (jugadores[lista_jugadores_aleatorios[k]]["dados"][j]):
                        jugadores[lista_jugadores_aleatorios[k]]["dados"].insert(j,dados)
                        break
            if longitud_lista_dados == len((jugadores[lista_jugadores_aleatorios[k]]["dados"])):
                jugadores[lista_jugadores_aleatorios[k]]["dados"].append(dados)

        #print(jugadores[lista_jugadores_aleatorios[k]])

#COmparamos dados y establecemos puntos
    for i in range(numero_dados):
        if jugadores[lista_jugadores_aleatorios[0]]["dados"][i] >  jugadores[lista_jugadores_aleatorios[1]]["dados"][i]:
            jugadores[lista_jugadores_aleatorios[0]]["puntos"] += 1
        elif jugadores[lista_jugadores_aleatorios[0]]["dados"][i] <  jugadores[lista_jugadores_aleatorios[1]]["dados"][i]:
            jugadores[lista_jugadores_aleatorios[1]]["puntos"] += 1
    # print(jugadores[lista_jugadores_aleatorios[0]])
    # print(jugadores[lista_jugadores_aleatorios[1]])
    # if (jugadores[lista_jugadores_aleatorios[0]])["puntos"] > maximo_puntos:
    #     maximo_puntos == jugadores[lista_jugadores_aleatorios[0]]["puntos"]
    # if (jugadores[lista_jugadores_aleatorios[1]])["puntos"] > maximo_puntos:
    #     maximo_puntos == jugadores[lista_jugadores_aleatorios[1]]["puntos"]
    for k in range(2):
        if (jugadores[lista_jugadores_aleatorios[k]])["puntos"] > maximo_puntos:
            maximo_puntos == jugadores[lista_jugadores_aleatorios[k]]["puntos"]
        jugadores[lista_jugadores_aleatorios[k]]["dados"].clear()

#Ordenamos tabla ordenada por puntos

    jugadores2 = list(jugadores.copy())
    #print(jugadores2)
    print(cabecera)
    for players in jugadores:
        nombre = (jugadores[players]["Nombre"])
        puntos = (jugadores[players]["puntos"])
        print(players.ljust(10) + nombre.ljust(20) + str(puntos).rjust(10))


    input("Enter para continuar: ")

















# lista_ids_ordenada_puntos = []
# for key in jugadores:
#     if len(lista_ids_ordenada_puntos) == 0:
#         lista_ids_ordenada_puntos.append(key)
#     else:
#         len_lista_ids_ordenada_puntos = len(lista_ids_ordenada_puntos)
#         for i in range(len(lista_ids_ordenada_puntos)):
#             if jugadores[key]["puntos"] > jugadores[lista_ids_ordenada_puntos[i]]["puntos"]:
#                 lista_ids_ordenada_puntos.insert(i,key)
#                 break
#         if len_lista_ids_ordenada_puntos == len(lista_ids_ordenada_puntos):
#             lista_ids_ordenada_puntos.append(key)
# print(lista_ids_ordenada_puntos)
#
# for dni in lista_ids_ordenada_puntos:
#      nombre =(lista_ids_ordenada_puntos[dni]["Nombre"])
#      puntos =(lista_ids_ordenada_puntos[dni]["puntos"])
#      print(dni.ljust(10) + nombre.ljust(20) + str(puntos).rjust(10))