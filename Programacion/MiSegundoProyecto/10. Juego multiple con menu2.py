# jugadores = {"11111111L": {"Nombre": "Pedro Martinez", "dados": [], "puntos": 4},
#              "22222222K": {"Nombre": "Pedro Sanchez", "dados": [], "puntos": 5},
#              "33333333S": {"Nombre": "Lola Indigo", "dados": [], "puntos": 2},
#              "44444444L": {"Nombre": "Andres iniesta", "dados": [], "puntos": 5}}

base_jugadores = {"11111111L": "Pedro Martinez", "22222222K": "Pedro Sanchez", "33333333S": "Lola Indigo",
                  "44444444L": "Andres iniesta"}

cabecera_00 = ""

jugadores = {}
salir = False
flg_00 = True
flg_01 = False
flg_02 = False
flg_021 = False
flg_03 = False
flg_031 = False


while not salir:

    while flg_00:
        opc = input("Selecciona una Opcion:")
        if not opc.isdigit():
            print("Only numeric options")
            input("Enter para continuar: ")
        elif int(opc) not in range(1,5):
            print("Option out of range:")
            input("Enter para continuar: ")
        else:
            opc = int(opc)

        if opc == 1:
            flg_01 = True
            flg_00 = False

        if opc == 2:
            flg_02 = True
            flg_00 = False

        if opc == 3:
            flg_03 = True
            flg_00 = False

        if opc == 4:
            print("Chauuu")
            flg_00 = False
            salir = True


    while flg_01:






    while flg_021:
        lista_dnis_disponibles = list(base_jugadores.keys())
        lista_jugadores_seleccionados = []
        sel_jug = False

        while not sel_jug:
            menu = "Jugadores Disponibles".center(50, "=") + "\n"

            # Generación del menú de jugadores disponibles
            for i in range(1, len(lista_dnis_disponibles) + 2):
                if i == len(lista_dnis_disponibles) + 1:
                    menu += str(i) + ") Go Back\n"
                else:
                    menu += str(i) + ") " + base_jugadores[lista_dnis_disponibles[i - 1]] + "\n"

            menu += "Jugadores Seleccionados".center(50, "=") + "\n"
            for i in range(1, len(lista_jugadores_seleccionados) + 1):
                menu += str(i) + ") " + base_jugadores[lista_jugadores_seleccionados[i - 1]] + "\n"

            print(menu)
            opc = input("Opción: ")
            deseleccionar = False

            if opc.startswith("-"):
                opc = opc[1:]
                deseleccionar = True

            if not opc.isdigit():
                print("Solo se permiten opciones numéricas")
            else:
                opc = int(opc)
                if opc == len(lista_dnis_disponibles) + 1:
                    # Opción "Go Back" seleccionada
                    flg_021 = False
                    sel_jug = True  # Termina el bucle de selección
                elif opc < 1 or opc > len(lista_dnis_disponibles) + (1 if deseleccionar else 0):
                    print("Opción fuera de rango")
                elif deseleccionar:
                    if 1 <= opc <= len(lista_jugadores_seleccionados):
                        lista_dnis_disponibles.append(lista_jugadores_seleccionados[opc - 1])
                        lista_jugadores_seleccionados.pop(opc - 1)
                    else:
                        print("Opción de deselección fuera de rango")
                else:
                    lista_jugadores_seleccionados.append(lista_dnis_disponibles[opc - 1])
                    lista_dnis_disponibles.pop(opc - 1)

        for dni in lista_jugadores_seleccionados:
            jugadores[dni] = {"nombre": base_jugadores[dni], "dados": [], "puntos": 4}
        print(jugadores)
