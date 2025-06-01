import random
Menu0 = "1)Set Player" + "\n" + "2)Set Bot" + "\n" + "3)Add Bot" + "\n" + "4)Play" + "\n" + "5)Ranking" + "\n" + "6)Exit" + "\n"

Salir = True

Username = ""
bots="Bot0-Bot1-Bot2-Bot3"
bot = ""
puntos_bot = 0
puntos_usuario = 0
dados_usuario = ""
dado_m_usuario = 0
dados_bot = ""
dado_m_bot = 0
tirada = 0
ranking = "Manuel Casado:3:58;Alba Rodriguez:2:54;Esther Vallejo:10:49"


while Salir:
    print(Menu0)
    opcion = input("Option: ")
    if not opcion.isdigit():
        print("Only numeric options")
    else:
        opcion = int(opcion)
        if opcion not in range(1,7):
            print("Option out of range")
        else:
            if opcion == 1:
                while True:
                    Username = input("Enter Username:")
                    if not Username.replace(" ","").isalpha():
                        print("Wrong Username. Try Again")
                    else:
                        break
            if opcion == 2:
                bots_aleatorios = bots
                bots_aleatorios += "-"
                #print(bots)
                total_bots = bots_aleatorios.count("-")
                #print(total_bots)
                indice_random = random.randint(0, total_bots - 1)
                inicio = 0
                for i in range(total_bots):  
                    final = bots_aleatorios.find("-",inicio)
                    if i == indice_random:
                        bot = bots_aleatorios[inicio:final]
                        break
                    inicio = final + 1
                    
                print("The Bot wil be", bot)
                    
                #print(bots)       
            if opcion == 3:
                while True:
                    bot_nuevo = input("Dame un nombre para el nbuevo bot: ")
                    if not bot_nuevo.isalnum():
                        print("bad name please try again: ")
                    else:
                        bots += "-"+bot_nuevo
                        #print(bots)
                        break
            if opcion == 4:
                tirada = 0
                puntos_bot = 0
                puntos_usuario = 0

                if Username == "" or bot == "":
                    print("Select a usertnem and a bot first")
                    input("Enter to continue")
                else:
                    for j in range(10):
                        tirada += 1
                        cadena = "Turno" , tirada
                        orden_tirada = random.randrange(1,3)
                        dados_usuario = ""
                        dado_m_usuario = 0
                        dados_bot = ""
                        dado_m_bot = 0

                        if orden_tirada == 1:
                            for i in range(25):
                                dado_bot = random.randrange(1,61)

                                if dado_m_bot < dado_bot:
                                    dado_m_bot = dado_bot
                                dados_bot += "{}-".format(dado_bot)

                            for i in range(15):
                                dado_usuario = random.randrange(1,61)

                                if dado_m_usuario < dado_usuario:
                                    dado_m_usuario = dado_usuario
                                dados_usuario += "{}-".format(dado_usuario)

                        if orden_tirada == 2:
                            for i in range(25):
                                dado_usuario = random.randrange(1,61)

                                if dado_m_usuario < dado_usuario:
                                    dado_m_usuario = dado_usuario
                                dados_usuario += "{}-".format(dado_usuario)

                            for i in range(15):
                                dado_bot = random.randrange(1,61)

                                if dado_m_bot < dado_bot:
                                    dado_m_bot = dado_bot
                                dados_bot += "{}-".format(dado_bot)
                        
                        if dado_m_bot == dado_m_usuario:
                            print("Turno",tirada)  
                            print("Dados {} = {}".format(Username,dados_usuario))
                            print("Dados mayor de {} = {}".format(Username,dado_m_usuario))
                            print("Dados {} = {}".format(bot,dados_bot))
                            print("Dados mayor de {} = {}".format(bot,dado_m_bot))
                            print("")
                            print("Draw: Nobody Wins Points")
                            print("")
                            print("Puntos of {} = {}".format(Username,puntos_usuario))
                            print("Puntos of {} = {}".format(bot,puntos_bot)) 
                            input("Enter to continue")                   
                        
                        
                        if dado_m_bot > dado_m_usuario:
                            puntos_bot += 2*(dado_m_bot-dado_m_usuario)
                            print("Turno",tirada)  
                            print("Dados {} = {}".format(Username,dados_usuario))
                            print("Dados mayor de {} = {}".format(Username,dado_m_usuario))
                            print("Dados {} = {}".format(bot,dados_bot))
                            print("Dados mayor de {} = {}".format(bot,dado_m_bot))
                            print("")
                            print("{} Wins {} Points".format(bot,2*(dado_m_bot-dado_m_usuario)))
                            print("")
                            print("Puntos of {} = {}".format(Username,puntos_usuario))
                            print("Puntos of {} = {}".format(bot,puntos_bot)) 
                            input("Enter to continue")    
                        
                        if dado_m_bot < dado_m_usuario:
                            puntos_usuario += 2*(dado_m_usuario-dado_m_bot)
                            print("Turno",tirada)  
                            print("Dados {} = {}".format(Username,dados_usuario))
                            print("Dados mayor de {} = {}".format(Username,dado_m_usuario))
                            print("Dados {} = {}".format(bot,dados_bot))
                            print("Dados mayor de {} = {}".format(bot,dado_m_bot))
                            print("")
                            print("{} Wins {} Points".format(Username,2*(dado_m_usuario-dado_m_bot)))
                            print("")
                            print("Puntos of {} = {}".format(Username,puntos_usuario))
                            print("Puntos of {} = {}".format(bot,puntos_bot))
                            input("Enter to continue")

                        if tirada == 10:
                            if puntos_usuario > puntos_bot:
                                print("{} wins the game with {} points".format(Username,puntos_usuario))
                                
                                # Vamos a recorrer el ranking y ver si el usuario ya existe
                                nuevo_ranking = ""
                                inicio = 0
                                encontrado = False
                                total = ranking.count(";") + 1

                                for i in range(total):
                                    fin = ranking.find(";", inicio)
                                    if fin == -1:
                                        fin = len(ranking)

                                    bloque = ranking[inicio:fin]

                                    separacion1 = bloque.find(":")
                                    separacion2 = bloque.find(":", separacion1+1)

                                    nombre = bloque[0:separacion1]
                                    partidas = int(bloque[separacion1+1:separacion2])
                                    puntos = int(bloque[separacion2+1:])

                                    if nombre == Username:
                                        partidas += 1
                                        puntos += puntos_usuario
                                        encontrado = True
                                    nuevo_ranking += "{}:{}:{};".format(nombre,partidas,puntos)
                                    inicio = fin + 1

                                if not encontrado:
                                    # Añadir el usuario al final, luego ordenamos
                                    nuevo_ranking += "{}:{}:{};".format(Username, 1, puntos_usuario)

                                # Ahora creamos una lista de jugadores para ordenar por puntos
                                jugadores = []
                                inicio = 0
                                while inicio < len(nuevo_ranking):
                                    fin = nuevo_ranking.find(";",inicio)
                                    if fin == -1:
                                        break
                                        
                                    bloque = nuevo_ranking[inicio:fin]

                                    sep1 = bloque.find(":")
                                    sep2 = bloque.find(":", sep1+1)

                                    nombre = bloque[0:sep1]
                                    partidas = int(bloque[sep1+1:sep2])
                                    puntos = int(bloque[sep2+1:])

                                    jugadores.append((nombre, partidas, puntos))

                                    inicio = fin + 1
                                # Ordenar manualmente por puntos descendentes (burbuja)
                                for i in range(len(jugadores)):
                                    for j in range(i+1, len(jugadores)):
                                        if jugadores[i][2] < jugadores[j][2]:
                                            jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

                                # Volver a construir el ranking como string
                                ranking = ""
                                for jugador in jugadores:
                                    ranking += "{}:{}:{};".format(jugador[0], jugador[1], jugador[2])

                                # Eliminar el ; final (opcional)
                                if ranking.endswith(";"):
                                    ranking = ranking[:-1]

                                input("Enter to continue")


                            if puntos_usuario < puntos_bot:
                                print("{} wins the game with {} points".format(bot,puntos_bot))
                                input("Enter to continue")

            if opcion == 5:
                while True:
                    print("1)Show Ranking By Total Points")
                    print("2)Show Ranking By Total Games")
                    print("3)Go Back")
                    subopcion = input("Option: ")
                    if subopcion == "3":
                        break
                    else:
                        jugadores = []
                        inicio = 0
                        while inicio < len(ranking):
                            fin = ranking.find(";", inicio)
                            if fin == -1:
                                fin = len(ranking)
                            
                            bloque = ranking[inicio:fin]
                            sep1 = bloque.find(":")
                            sep2 = bloque.find(":", sep1+1)
                            nombre = bloque[:sep1]
                            partidas = int(bloque[sep1+1:sep2])
                            puntos = int(bloque[sep2+1:])
                            jugadores.append((nombre, partidas, puntos))

                            if fin == len(ranking):
                                break
                            inicio = fin + 1

                        if subopcion == "1":
                            # Ordenamos por puntos
                            for i in range(len(jugadores)):
                                for j in range(i+1, len(jugadores)):
                                    if jugadores[i][2] < jugadores[j][2]:
                                        jugadores[i], jugadores[j] = jugadores[j], jugadores[i]
                        elif subopcion == "2":
                            # Ordenamos por partidas
                            for i in range(len(jugadores)):
                                for j in range(i+1, len(jugadores)):
                                    if jugadores[i][1] < jugadores[j][1]:
                                        jugadores[i], jugadores[j] = jugadores[j], jugadores[i]
                        print("\n{:<20} {:<20} {:<20}".format("Name", "Games", "Points"))
                        print("-"*60)
                        for jugador in jugadores:
                            print("{:<20} {:<20} {:<20}".format(jugador[0], jugador[1], jugador[2]))
                        print()
            if opcion == 6:
                Salir = False