import random


menu="The Best Game In The World".center(40,"=") + "\n" + "1)New Game" + "\n" + "2)New Player" + "\n" + "3)Show Ranking" + "\n" + "4)Sortir" + "\n" + "Selecciona una opcion: "

llista = "''''''''''''''''RANKING'''''''''''''''''".center(40) + "\n" + "NOMBRE".ljust(30) + "PUNTOS".rjust(10) + "\n" + "*" * 40 + "\n"

name_check = False
ranking = {}
TotalJugador1 = 0
TotalBot = 0

while True:
    opc = input(menu)

    if not opc.isdigit() or not 1 <= int(opc) <= 4:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
        continue

    opc = int(opc)

    if opc == 1:
        if not name_check:
            print("Por favor, introduce tu nombre antes de jugar.")
            input("Presiona enter para continuar...")
            continue

        TotalJugador1 = 0
        TotalBot = 0

        for i in range(50):
            print("Turno {}".format(i + 1).center(40, "*"))

            PuntosDados = random.randint(1, 6)
            PuntosDados2 = random.randint(1, 6)

            PuntosDadosBot = random.randint(1, 6)
            PuntosDadosBot2 = random.randint(1, 6)

            print("Tus dados: {} y {}. Dados del Bot: {} y {}".format(PuntosDados, PuntosDados2, PuntosDadosBot, PuntosDadosBot2))

            if (PuntosDados + PuntosDados2) % 2 == 0:
                TotalJugador1 += max(PuntosDados, PuntosDados2)
                print("Suma de tus dados es par. Se suma el mayor dado: {}".format(max(PuntosDados, PuntosDados2)))
            else:
                TotalJugador1 -= min(PuntosDados, PuntosDados2)
                print("Suma de tus dados es impar. Se resta el menor dado: {}".format(min(PuntosDados, PuntosDados2)))


            if (PuntosDadosBot + PuntosDadosBot2) % 2 == 0:
                TotalBot += max(PuntosDadosBot, PuntosDadosBot2)
                print("Suma de los dados del Bot es par. Se suma el mayor dado: {}".format(max(PuntosDadosBot, PuntosDadosBot2)))
            else:
                TotalBot -= min(PuntosDadosBot, PuntosDadosBot2)
                print("Suma de los dados del Bot es impar. Se resta el menor dado: {}".format(min(PuntosDadosBot, PuntosDadosBot2)))

            print("Puntos Totales Bot = {}, Puntos de {} = {}".format(TotalBot, NombresJugador, TotalJugador1))
            print("-" * 40)

        print("\nTotal {} = {}, Total Bot = {}".format(NombresJugador, TotalJugador1, TotalBot))
        if TotalJugador1 > TotalBot:
            print("{} gana!".format(NombresJugador))
            ranking[NombresJugador] = ranking.get(NombresJugador, 0) + 1
        elif TotalBot > TotalJugador1:
            print("Bot gana!")
        else:
            print("¡Es un empate!")

    elif opc == 2:
        NombresJugador = input("Dame un nombre: ")
        name_check = True

    elif opc == 3:
        print(llista)
        for nombre, puntos in ranking.items():
            print("{:<30} {:>10}".format(nombre, puntos))
        input("Presiona enter para continuar...")

    elif opc == 4:
        print("Saliendo del juego...")
        break