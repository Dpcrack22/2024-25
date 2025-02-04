import random  # Importa la librería random para generar números aleatorios (dados).

# Menú principal del juego, formateado y centrado.
menu = "The Best Game In The World".center(40, "=") + "\n" + \
       "1) New Game" + "\n" + "2) New Player" + "\n" + \
       "3) Show Ranking" + "\n" + "4) Exit" + "\n" + \
       "Selecciona una opción: "

# Inicializa el formato de la tabla de ranking (cabecera de la lista de puntuaciones).
ranking_header = "''''''''''''''''RANKING'''''''''''''''''".center(40) + "\n" + \
                 "NOMBRE".ljust(30) + "PUNTOS".rjust(10) + "\n" + "*" * 40 + "\n"

# Cadena para almacenar el ranking en formato "nombre:puntos*"
ranking = ""  # Almacena jugadores y sus puntos en formato string
name_check = False  # Verifica si ya se ha introducido el nombre del jugador.
TotalJugador1 = 0  # Puntos acumulados del jugador.
TotalBot = 0  # Puntos acumulados del bot.

# Bucle principal del juego, se repetirá hasta que el jugador elija salir.
while True:
    opc = input(menu)  # Muestra el menú y solicita una opción.

    # Validación de entrada: verifica que la opción sea numérica y esté en el rango de 1 a 4.
    if not opc.isdigit() or not 1 <= int(opc) <= 4:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
        continue  # Si la entrada es inválida, vuelve a mostrar el menú.

    opc = int(opc)  # Convierte la opción en un entero.

    # Opción 1: Comienza un nuevo juego.
    if opc == 1:
        # Verifica si el jugador ha introducido su nombre antes de empezar el juego.
        if not name_check:
            print("Por favor, introduce tu nombre antes de jugar.")
            input("Presiona enter para continuar...")
            continue  # Si no ha introducido su nombre, vuelve al menú.

        # Reinicia los puntos del jugador y del bot.
        TotalJugador1 = 0
        TotalBot = 0

        # Bucle para simular 50 turnos del juego de dados.
        for i in range(50):
            print("Turno {}".format(i + 1).center(40, "*"))  # Imprime el número de turno centrado.

            # Genera números aleatorios para los dados del jugador y del bot.
            PuntosDados = random.randint(1, 6)  # Dado 1 del jugador.
            PuntosDados2 = random.randint(1, 6)  # Dado 2 del jugador.
            PuntosDadosBot = random.randint(1, 6)  # Dado 1 del bot.
            PuntosDadosBot2 = random.randint(1, 6)  # Dado 2 del bot.

            # Muestra los valores de los dados tanto del jugador como del bot.
            print("Tus dados: {} y {}. Dados del Bot: {} y {}".format(PuntosDados, PuntosDados2, PuntosDadosBot, PuntosDadosBot2))

            # Encontrar el dado mayor y menor **sin max y min** para el jugador.
            if PuntosDados > PuntosDados2:
                mayor_jugador = PuntosDados
                menor_jugador = PuntosDados2
            else:
                mayor_jugador = PuntosDados2
                menor_jugador = PuntosDados

            # Encontrar el dado mayor y menor **sin max y min** para el bot.
            if PuntosDadosBot > PuntosDadosBot2:
                mayor_bot = PuntosDadosBot
                menor_bot = PuntosDadosBot2
            else:
                mayor_bot = PuntosDadosBot2
                menor_bot = PuntosDadosBot

            # Suma de los dados del jugador.
            if (PuntosDados + PuntosDados2) % 2 == 0:  # Si la suma de los dados del jugador es par...
                TotalJugador1 += mayor_jugador  # Suma el valor del dado mayor.
                print("Suma de tus dados es par. Se suma el mayor dado: {}".format(mayor_jugador))
            else:
                TotalJugador1 -= menor_jugador  # Resta el valor del dado menor si la suma es impar.
                print("Suma de tus dados es impar. Se resta el menor dado: {}".format(menor_jugador))

            # Suma de los dados del bot.
            if (PuntosDadosBot + PuntosDadosBot2) % 2 == 0:  # Si la suma de los dados del bot es par...
                TotalBot += mayor_bot  # Suma el valor del dado mayor del bot.
                print("Suma de los dados del Bot es par. Se suma el mayor dado: {}".format(mayor_bot))
            else:
                TotalBot -= menor_bot  # Resta el valor del dado menor si la suma es impar.
                print("Suma de los dados del Bot es impar. Se resta el menor dado: {}".format(menor_bot))

            # Muestra los puntos acumulados tanto del jugador como del bot tras cada turno.
            print("Puntos Totales Bot = {}, Puntos de {} = {}".format(TotalBot, NombresJugador, TotalJugador1))
            print("-" * 40)  # Línea divisoria entre turnos.

        # Después de 50 turnos, muestra el total de puntos de ambos.
        print("\nTotal {} = {}, Total Bot = {}".format(NombresJugador, TotalJugador1, TotalBot))

        # Determina quién ganó y actualiza el ranking.
        if TotalJugador1 > TotalBot:
            print("{} gana!".format(NombresJugador))
            # Añadimos o actualizamos el ranking en formato string "nombre:puntos*"
            # Si el jugador ya está en el ranking, actualizamos sus puntos.
            if NombresJugador in ranking:
                # Buscar y actualizar los puntos
                lista_ranking = ranking.split("*")
                ranking = ""
                for jugador in lista_ranking:
                    if NombresJugador in jugador:
                        nombre, puntos = jugador.split(":")
                        puntos = str(int(puntos) + TotalJugador1)  # Actualizamos los puntos
                        jugador_actualizado = "{}:{}".format(nombre, puntos)
                        ranking += jugador_actualizado + "*"
                    else:
                        ranking += jugador + "*"
            else:
                # Si el jugador no está, lo añadimos
                ranking += "{}:{}*".format(NombresJugador, TotalJugador1)

        elif TotalBot > TotalJugador1:
            print("Bot gana!")
        else:
            print("¡Es un empate!")

    # Opción 2: Permite al jugador introducir su nombre.
    elif opc == 2:
        NombresJugador = input("Dame un nombre: ")  # Solicita el nombre del jugador.
        name_check = True  # Marca que el nombre ha sido introducido.

    # Opción 3: Muestra el ranking de jugadores.
    elif opc == 3:
        # Submenú para ordenar el ranking
        sub_menu_ranking = """
        ========================================
                MOSTRAR RANKING
        ========================================
        1) Ordenar por Nombre
        2) Ordenar por Puntos
        3) Regresar al menú principal
        ========================================
        """
        while True:
            sub_opc = input(sub_menu_ranking)  # Submenú para ordenar el ranking

            if sub_opc == "1":  # Ordenar por Nombre
                print(ranking_header)  # Imprime la cabecera del ranking
                # Ordenamos los jugadores por nombre (antes del ":")
                jugadores = ranking.split("*")
                jugadores = sorted([jugador for jugador in jugadores if jugador], key=lambda x: x.split(":")[0])
                for jugador in jugadores:
                    nombre, puntos = jugador.split(":")
                    print("{:<30} {:>10}".format(nombre, puntos))
                input("Presiona enter para continuar...")

            elif sub_opc == "2":  # Ordenar por Puntos
                print(ranking_header)  # Imprime la cabecera del ranking
                # Ordenamos los jugadores por puntos (después del ":")
                jugadores = ranking.split("*")
                jugadores = sorted([jugador for jugador in jugadores if jugador], key=lambda x: int(x.split(":")[1]), reverse=True)
                for jugador in jugadores:
                    nombre, puntos = jugador.split(":")
                    print("{:<30} {:>10}".format(nombre, puntos))
                input("Presiona enter para continuar...")

            elif sub_opc == "3":  # Regresar al menú principal
                break  # Sale del submenú y regresa al menú principal
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    # Opción 4: Salir del juego.
    elif opc == 4:
        print("Saliendo del juego...")
        break  # Rompe el bucle y termina el juego.
