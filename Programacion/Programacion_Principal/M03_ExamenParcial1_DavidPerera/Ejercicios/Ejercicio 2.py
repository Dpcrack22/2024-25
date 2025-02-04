import random

menu = "The Best Game In The World".center(40, "=") + "\n" + "1) Set Player" + "\n" + "2) Set Bot" + "\n" + "3) Add Bot" + "\n" + "4) Play" + "\n" + "5) Ranking""\n" + "6) Exit"  "\n" +"Selecciona una opción: "


ranking = ""
TotalJugador1 = 0
TotalBot = 0
name_chek = False
bot_chek = False
bots="Bot0-Bot1-Bot2-Bot3"
bots1 = ""

flag00 = True

while True:

    opcion = input(menu)
    if opcion.isalpha():
        print("Only numeric options")
        input("Dale enter para continuar:")

    elif int(opcion) <= 0 or int(opcion) >6:
        print("Option out of range")
        input("Dale enter para continuar:")

    opcion = int(opcion)

    if opcion == 1:
        NombresJugador = input("Dame un nombre: ")
        if NombresJugador.isalpha():
            continue
        else:
            print("Wrong Username. Try Again")
            input("Dale enter para continuar:")
        name_check = True














    # if opcion == 4:
    #     if not name_chek:
    #         print("Before Play, Set the Username.")
    #         input("Presiona enter para continuar...")
    #         continue
    #
    #     if not bot_chek:
    #         print("Before Play, Set the Bot.")
    #         input("Presiona enter para continuar...")
    #         continue
    #
    #     TotalJugador1 = 0
    #     TotalBot = 0
    #
    #     for i in range(50):
    #         print("Turno {}".format(i + 1).center(40, "*"))  # Imprime el número de turno centrado.
    #
    #         PuntosDados = random.randint(1, 6)
    #         PuntosDados2 = random.randint(1, 6)
    #         PuntosDadosBot = random.randint(1, 6)
    #         PuntosDadosBot2 = random.randint(1, 6)
    #
    #         print("Tus dados: {} y {}. Dados del Bot: {} y {}".format(PuntosDados, PuntosDados2, PuntosDadosBot, PuntosDadosBot2))
    #
    #         if (PuntosDados + PuntosDados2) % 2 == 0:
    #             TotalJugador1 += max(PuntosDados, PuntosDados2)
    #             print("Suma de tus dados es par. Se suma el mayor dado: {}".format(max(PuntosDados, PuntosDados2)))
    #         else:
    #             TotalJugador1 -= min(PuntosDados, PuntosDados2)
    #             print("Suma de tus dados es impar. Se resta el menor dado: {}".format(min(PuntosDados, PuntosDados2)))
    #
    #         if (PuntosDadosBot + PuntosDadosBot2) % 2 == 0:
    #             TotalBot += max(PuntosDadosBot, PuntosDadosBot2)
    #             print("Suma de los dados del Bot es par. Se suma el mayor dado: {}".format(max(PuntosDadosBot, PuntosDadosBot2)))
    #         else:
    #             TotalBot -= min(PuntosDadosBot, PuntosDadosBot2)
    #             print("Suma de los dados del Bot es impar. Se resta el menor dado: {}".format(min(PuntosDadosBot, PuntosDadosBot2)))
    #
    #
    #         print("Puntos Totales Bot = {}, Puntos de {} = {}".format(TotalBot, NombresJugador, TotalJugador1))
    #         print("-" * 40)
    #
    #
    #     print("\nTotal {} = {}, Total Bot = {}".format(NombresJugador, TotalJugador1, TotalBot))
    #
    #     if TotalJugador1 > TotalBot:
    #         print("{} gana!".format(NombresJugador))
    #
    #
    #         if NombresJugador in ranking:
    #             lista_ranking = ranking.split("*")
    #             ranking = ""
    #             for jugador in lista_ranking:
    #                 if NombresJugador in jugador:
    #                     nombre, puntos = jugador.split(":")
    #                     puntos = str(int(puntos) + TotalJugador1)
    #                     jugador_actualizado = "{}:{}".format(nombre, puntos)
    #                     ranking += jugador_actualizado + "*"
    #                 else:
    #                     ranking += jugador + "*"
    #         else:
    #             ranking += "{}:{}*".format(NombresJugador, TotalJugador1)
    #
    #     elif TotalBot > TotalJugador1:
    #         print("Bot gana!")
    #     else:
    #         print("¡Es un empate!")
    #
    #



