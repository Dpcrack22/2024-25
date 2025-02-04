
ranking = "Manuel Casado:3:58;Alba Rodriguez:2:54;Esther Vallejo:10:49;Alvaro Ballejo:10:67"

menu_ranking = ("Ranking".center(50, "*")) + "\n" + "Nombre".ljust(25) + "Partidas".ljust(10) + "Puntos Totales".ljust(15) + "\n" + "*"*50 + "\n"
menu = ("Que quieres hacer:" + "\n" + " 1. Mostrar ranking ordenado por nombre" + "\n" + " 2. Mostrar ranking por partidas" + "\n" + " 3. Mostrar ranking por puntos" + "\n" + " 4. Exit" + "\n" + " Seleccione un numero: ")

while True:
    print(menu_ranking)
    jugadores = ranking.split(";")
    jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[2]), reverse=True)
    # print(jugadores_puntos)
    # print(jugadores)
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
    opc = input(menu)

    if not opc.isdigit():
        print("Opción no válida. Solo se permiten números.")
        input("Presiona Enter para continuar...")
        continue

    opc = int(opc)

    if opc < 1 or opc > 4:
        print("Opción fuera de rango. Introduce un número del 1 al 8.")
        input("Presiona Enter para continuar...")
        continue

    if opc == 1:
        print(menu_ranking)
        jugadores = ranking.split(";")
        jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[0]))
        # print(jugadores_puntos)
        # print(jugadores)
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
        input("Enter para continuar: ")

    if opc == 2:
        print(menu_ranking)
        jugadores = ranking.split(";")
        jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[1]))
        # print(jugadores_puntos)
        # print(jugadores)
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
        input("Enter para continuar: ")

    if opc == 3:
        print(menu_ranking)
        jugadores = ranking.split(";")
        jugadores_puntos = sorted(jugadores, key=lambda x: (x.split(":")[2]), reverse=True)
        # print(jugadores_puntos)
        # print(jugadores)
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
        input("Enter para continuar: ")

    if opc == 4:
        break





