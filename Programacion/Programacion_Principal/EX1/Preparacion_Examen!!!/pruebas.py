
ranking = "Manuel Casado:3:58;Alba Rodriguez:2:54;Esther Vallejo:10:49;Alvaro Ballejo:10:67"

menu_ranking = ("Ranking".center(50, "*")) + "\n" + "Nombre".ljust(25) + "Partidas".ljust(10) + "Puntos Totales".ljust(15) + "\n" + "*"*50 + "\n"
menu = ("Que quieres hacer:" + "\n" + " 1. Añadir jugador" + "\n" + " 2. Jugar" + "\n" + " 3. Ver Ranking" + "\n" + " 4. Exit" + "\n" + " Seleccione un numero: ")
#print(menu)


# jugadores = ranking.split(";")
# jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[2]), reverse=True)
# print(jugadores_puntos)
# print(jugadores)
# for registro in jugadores_puntos:
#     if registro:
#         partes = registro.split(":")
#         if len(partes) < 2:
#             print("Registro no valido".format(registro))
#             continue
#
#         nombre = partes[0]
#         partidas = partes[1]
#         puntos = partes[2]
#
#         rankin_mod = nombre.ljust(25) + partidas.rjust(5) + puntos.rjust(15)
#         print(rankin_mod)

while True:
    opc = input(menu)

    if not opc.isdigit():
        print("Opción no válida. Solo se permiten números.")
        input("Presiona Enter para continuar...")
        continue

    opc = int(opc)

    if opc < 1 or opc > 6:
        print("Opción fuera de rango. Introduce un número del 1 al 8.")
        input("Presiona Enter para continuar...")
        continue

    if opc == 1:
        nombre = input("Añade un nombre con apellidos")
        partidas_nuevo = "0"
        puntos_nuevo = "0"
        nuevo_jugador = "{}:{}:{}".format(nombre,partidas_nuevo,puntos_nuevo)
        ranking += nuevo_jugador + (";")
        print(ranking)

    if opc == 2:
        print("NO FUNCIONA")

    if opc == 3:
        jugadores = ranking.split(";")
        jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[2]), reverse=True)
        #print(jugadores_puntos)
        #print(jugadores)
        print(menu_ranking)
        for registro in jugadores_puntos:
            if registro:
                partes = registro.split(":")
                if len(partes) < 2:
                    print("Registro no valido".format(registro))
                    continue

                nombre = partes[0]
                partidas = partes[1]
                puntos = partes[2]

                rankin_mod = nombre.ljust(25) + partidas.rjust(5) + puntos.rjust(15)
                print(rankin_mod)
        print("Quieres ordenarlo diferente? \n 1.Por Nombre \n 2.Por partidas jugadas \n 3.Salir")
        opcion1 = input("Escribe una opcion: ")
        if opcion1 == 1:
            jugadores = ranking.split(";")
            jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[2]), reverse=True)
            # print(jugadores_puntos)
            # print(jugadores)
            print(menu_ranking)
            for registro in jugadores_puntos:
                if registro:
                    partes = registro.split(":")
                    if len(partes) < 2:
                        print("Registro no valido".format(registro))
                        continue

                    nombre = partes[0]
                    partidas = partes[1]
                    puntos = partes[2]

                    rankin_mod = nombre.ljust(25) + partidas.rjust(5) + puntos.rjust(15)
                    print(rankin_mod)
            if opcion1 == 2:
                jugadores = ranking.split(";")
                jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[2]), reverse=True)
                # print(jugadores_puntos)
                # print(jugadores)
                print(menu_ranking)
                for registro in jugadores_puntos:
                    if registro:
                        partes = registro.split(":")
                        if len(partes) < 2:
                            print("Registro no valido".format(registro))
                            continue

                        nombre = partes[0]
                        partidas = partes[1]
                        puntos = partes[2]

                        rankin_mod = nombre.ljust(25) + partidas.rjust(5) + puntos.rjust(15)
                        print(rankin_mod)


