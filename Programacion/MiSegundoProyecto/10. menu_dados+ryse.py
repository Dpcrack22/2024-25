# jugadores = {"11111111L":{"Nombre":"Pedro Martinez","dados":[],"puntos":4},
#             "22222222K":{"Nombre":"Pedro Sanchez","dados":[],"puntos":5},
#             "33333333S":{"Nombre":"Lola Indigo","dados":[],"puntos":2},
#             "44444444L":{"Nombre":"Andres iniesta","dados":[],"puntos":5}}

base_jugadores = {"11111111L":"Pedro Martinez", "22222222K":"Pedro Sanchez", "33333333S":"Lola Indigo", "44444444L":"Andres iniesta"}

jugadores = {}

flg_021 = True



while flg_021:

    lista_dnis_disponibles = list(base_jugadores.keys())
    lista_jugadores_seleccionados = []
    sel_jug = False
    while not sel_jug:

        menu = "Jugadores Disponibles".center(50,"=") + "\n"
        for i in range(1, len(lista_dnis_disponibles)+2):
            if i == len(lista_dnis_disponibles) + 1:
                menu += str(i)+")" + "Go Back" + "\n"
            else:
                menu += str(i)+")"+ base_jugadores[lista_dnis_disponibles[i-1]] + "\n"

        menu += "Jugadores Seleccionados".center(50,"=") + "\n"
        for i in range(1, len(lista_jugadores_seleccionados) + 1):
            menu += str(i) + ")" + base_jugadores[lista_dnis_disponibles[i - 1]] + "\n"

        print(menu)


        #input("ENter")

        opc = input("Opcion")
        deseleccionar = False
        if opc[0] == "-":
            opc = opc[1:]
            deseleccionar = True
        elif not opc.isdigit():
            print("Only numeric options")
        elif int(opc) not in range(0, len(lista_dnis_disponibles)+1) and not deseleccionar:
            print("Option not in range")
            input("Enter to continue: ")
        elif int(opc) not in range(1, len(lista_jugadores_seleccionados) + 1) and not deseleccionar:
            print("Option not in range")
            input("Enter to continue: ")
        else:
            opc = int(opc)
            if opc == 0:
                flg_021 = False
                flg_02 = True
            elif not deseleccionar:
                lista_jugadores_seleccionados.append(lista_dnis_disponibles[opc-1])
                lista_dnis_disponibles.remove(lista_dnis_disponibles[opc-1])
            else:
                lista_dnis_disponibles.append(lista_jugadores_seleccionados[opc-1])
                lista_jugadores_seleccionados.remove(lista_jugadores_seleccionados[opc-1])

    for dni in lista_jugadores_seleccionados:
        jugadores[dni] = {"nombre":base_jugadores[dni], "dados":[],"puntos":4}
    print(jugadores)


