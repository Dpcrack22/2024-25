import random

# Diccionario que almacena los jugadores y sus datos (DNI, nombre, teléfonos y puntos).
players = {
    "47474747R": {"name": "Pedro Javier Morales", "tfn": ["+0034345345345"], "points": 12},
    "24536425T": {"name": "Maite Lopez Miravet", "tfn": ["+0034234234235", "+0034239999235"], "points": 15},
    "76767676H": {"name": "Marta Garcia Suarez", "tfn": ["+0075766576575"], "points": 21},
    "84848484I": {"name": "Aitana Sanchez Castillejos", "tfn": ["+0088823303445"], "points": 16},
    "12345623I": {"name": "Sergio Alarcon Navas", "tfn": ["+0066688221122"], "points": 12}
}

# Menús para mostrar opciones al usuario.
menu0 = "Menu".center(15, "x") + "\n1) New Player\n2) Search Player\n3) List Players\n4) Play\n5) Exit"
menu01 = "MenuBuscar".center(15, "x") + "\n1) By Name\n2) By DNI\n3) By tlf\n4) Go back"
menu02 = "MenuBuscar".center(15, "x") + "\n1) List by DNI\n2) List by Name\n3) List by Points\n4) Go back"
dni_letters = "T;R;W;A;G;M;Y;F;P;D;X;B;N;J;Z;S;Q;V;H;L;C;K;E;"
cabeceraRanking = "Name".ljust(30) + "DNI".ljust(15) + "Points".ljust(8) + "Tlf".ljust(17) + "\n" + ("*" * 70)

# Variables para controlar el flujo del programa
telefonos = []
newDNI = ""
name = ""
flag00 = True  # Control principal del bucle
flag01 = True  # Menú principal
flag02 = False  # Búsqueda de jugadores
flag03 = False  # Listar jugadores
flag04 = False  # Jugar

# Bucle principal
while flag00:
    while flag01:
        print(menu0)  # Muestra el menú principal
        opc = input("Opcion: ")  # Solicita al usuario una opción
        if not opc.isdigit():  # Verifica que la opción sea numérica
            print("Introduce una opción numérica")
        elif int(opc) < 1 or int(opc) > 5:  # Verifica que la opción esté en el rango correcto
            print("Opción no válida")
        else:
            opc = int(opc)  # Convierte la opción a entero
            if opc == 1:
                flag011 = True  # Activar la opción de agregar nuevo jugador
                flag01 = False
            elif opc == 2:
                flag02 = True  # Activar la opción de búsqueda de jugadores
                flag01 = False
            elif opc == 3:
                flag03 = True  # Activar la opción de listar jugadores
                flag01 = False
            elif opc == 4:
                flag04 = True  # Activar la opción de jugar
                flag01 = False
            elif opc == 5:
                flag00 = False  # Salir del bucle principal
                flag01 = False

    # Sección para agregar un nuevo jugador
    while flag011:
        name = input("Introduce el nombre y apellido: ")  # Solicita el nombre del jugador
        # Verifica que el nombre sea alfabético
        for i in range(len(name)):
            if name[i].isalpha() or not name[i] == "":
                flag0111 = True  # El nombre es válido
                flag011 = False
            else:
                print("El nombre solo puede contener letras")

    while flag0111:
        print("\nIntroduce el NIE:\n")  # Solicita el NIE (Número de Identidad de Extranjero)
        newDNI = input()  # Captura el NIE
        if len(newDNI) == 9:  # Verifica que el NIE tenga 9 caracteres
            letra_nie = int(newDNI[:8]) % 23  # Calcula la letra correspondiente
            # Obtiene la letra del DNI
            for i in range(letra_nie + 1):
                if i == 0:
                    inicio = 0
                    final = dni_letters.index(";")
                else:
                    inicio = final + 1
                    final = dni_letters.index(";", inicio)
            letra_seleccionada = dni_letters[inicio:final]
            if not newDNI[:8].isdigit():
                input("DNI no válido, los primeros 8 números deben ser dígitos\nPresiona Enter para continuar...")
            elif not newDNI[8:].isalpha():
                input("DNI no válido, la letra debe ser alfabética\nPresiona Enter para continuar...")
            elif letra_seleccionada.upper() != newDNI[8:].upper():
                input("DNI no válido, letra incorrecta\nPresiona Enter para continuar...")
            else:
                newDNI = newDNI[:8] + newDNI[8:].upper()  # Asegura que la letra esté en mayúsculas
                print("NIE aceptado")
                flag0113 = True  # NIE válido
                flag0111 = False
        else:
            input("NIE no válido, debe tener 8 números y 1 letra al final\nPresiona Enter para continuar...")

    # Sección para introducir teléfonos
    while flag0113:
        tlfCuantity = input("¿Cuántos números de teléfono deseas introducir? ")
        if not tlfCuantity.isdigit():  # Verifica que sea un número
            print("Introduce una opción numérica")
        else:
            tlfCuantity = int(tlfCuantity)  # Convierte a entero
            tlfIntroduced = True
            while tlfIntroduced:
                for i in range(tlfCuantity):  # Bucle para introducir la cantidad de teléfonos deseada
                    tlf = input("Introduce el teléfono {}: ".format(i + 1))
                    # Validaciones del número de teléfono
                    if len(tlf) != 14:
                        print("Teléfono incorrecto, debe tener '+' al principio y 13 números")
                    elif tlf[:1] != "+":
                        print("El teléfono debe empezar con '+'")
                    elif not tlf[1:].isdigit():
                        print("El teléfono solo puede contener números")
                    else:
                        telefonos.append(tlf)  # Agrega el teléfono a la lista
                        tlfIntroduced = False
            # Agrega el nuevo jugador al diccionario de jugadores
            players[newDNI] = {"name": name, "tfn": telefonos, "points": 0}
            input("Jugador creado exitosamente ")
            flag01 = True
            flag0113 = False

    # Sección para buscar jugadores
    while flag02:
        print(menu01)  # Muestra el menú de búsqueda
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("Introduce una opción numérica")
        elif int(opc) < 1 or int(opc) > 5:
            print("Opción no válida")
        else:
            opc = int(opc)
            if opc == 1:
                flag021 = True
                flag01 = False
            elif opc == 2:
                flag022 = True
                flag01 = False
            elif opc == 3:
                flag023 = True
                flag01 = False
            elif opc == 4:
                flag01 = True
                flag02 = False

    # Sección para listar jugadores
    while flag03:
        print(menu02)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("Introduce una opción numérica")
        elif int(opc) < 1 or int(opc) > 4:
            print("Opción no válida")
        else:
            opc = int(opc)
            if opc == 1:
                flag031 = True
                flag03 = False
            elif opc == 2:
                flag032 = True
                flag03 = False
            elif opc == 3:
                flag033 = True
                flag03 = False
            elif opc == 4:
                flag01 = True
                flag03 = False

    # Listar jugadores por DNI
    while flag031:
        jugadores = list(players.items())  # Convierte el diccionario a una lista de tuplas
        print(cabeceraRanking)
        n = len(jugadores)
        # Ordena los jugadores por DNI
        for i in range(n):
            for j in range(0, n - i - 1):
                if jugadores[j][0] > jugadores[j + 1][0]:
                    jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]
        for jugador in jugadores:
            Dni_jugador = jugador[0]
            datos_jugador = jugador[1]
            nombre_jugador = str(datos_jugador["name"])
            puntos_jugador = str(datos_jugador["points"])
            # Imprime la información del jugador
            for i in range(len(datos_jugador["tfn"])):
                telefono = datos_jugador["tfn"][i]
                print(nombre_jugador.ljust(29), Dni_jugador.ljust(15), puntos_jugador.ljust(5), telefono.ljust(17))
        input("Presiona Enter para volver")
        flag03 = True
        flag031 = False

    # Listar jugadores por nombre
    while flag032:
        jugadores = list(players.items())
        print(cabeceraRanking)
        n = len(jugadores)
        # Ordena los jugadores por nombre
        for i in range(n):
            for j in range(0, n - i - 1):
                if jugadores[j][1]["name"] > jugadores[j + 1][1]["name"]:
                    jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]
        for jugador in jugadores:
            Dni_jugador = jugador[0]
            datos_jugador = jugador[1]
            nombre_jugador = str(datos_jugador["name"])
            puntos_jugador = str(datos_jugador["points"])
            for i in range(len(datos_jugador["tfn"])):
                telefono = datos_jugador["tfn"][i]
                print(nombre_jugador.ljust(29), Dni_jugador.ljust(15), puntos_jugador.ljust(5), telefono.ljust(17))
        input("Presiona Enter para volver")
        flag03 = True
        flag032 = False

    # Listar jugadores por puntos
    while flag033:
        jugadores = list(players.items())
        print(cabeceraRanking)
        n = len(jugadores)
        # Ordena los jugadores por puntos
        for i in range(n):
            for j in range(0, n - i - 1):
                if jugadores[j][1]["points"] > jugadores[j + 1][1]["points"]:
                    jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]
        for jugador in jugadores:
            Dni_jugador = jugador[0]
            datos_jugador = jugador[1]
            nombre_jugador = str(datos_jugador["name"])
            puntos_jugador = str(datos_jugador["points"])
            for i in range(len(datos_jugador["tfn"])):
                telefono = datos_jugador["tfn"][i]
                print(nombre_jugador.ljust(29), Dni_jugador.ljust(15), puntos_jugador.ljust(5), telefono.ljust(17))
        input("Presiona Enter para volver")
        flag03 = True
        flag033 = False

    # Sección para jugar
    while flag04:
        jugadores = list(players.items())
        print(cabeceraRanking)
        for jugador in jugadores:
            Dni_jugador = jugador[0]
            datos_jugador = jugador[1]
            nombre_jugador = str(datos_jugador["name"])
            puntos_jugador = str(datos_jugador["points"])
            for i in range(len(datos_jugador["tfn"])):
                telefono = datos_jugador["tfn"][i]
                print(nombre_jugador.ljust(29), Dni_jugador.ljust(15), puntos_jugador.ljust(5), telefono.ljust(17))

        jugadorok = True
        # Seleccionar el primer jugador
        while jugadorok:
            jugador1 = input("Selecciona el DNI del primer jugador: ")
            datos_jugador1 = []
            for jugador in jugadores:
                if jugador1 in jugador[0]:
                    datos_jugador1.append(jugador[1]["name"])
                    jugadorok = False
                else:
                    print("El jugador no existe, introduce uno correcto")

        jugadorok = True
        # Seleccionar el segundo jugador
        while jugadorok:
            jugador2 = input("Selecciona el DNI del segundo jugador: ")
            datos_jugador2 = []

            for jugador in jugadores:
                if jugador2 in jugador[0]:
                    if jugador1 == jugador2:
                        print("No puedes seleccionar el mismo jugador, introduce otro")
                    else:
                        datos_jugador2.append(jugador[1]["name"])
                        jugadorok = False
                else:
                    print("El jugador no existe, introduce uno correcto")

        input("Presiona Enter para jugar ")
        # Tirar los dados
        dice1 = random.randrange(0, 6)
        dice2 = random.randrange(0, 6)
        print("Dado de {} = {} ".format(datos_jugador1, dice1))
        print("Dado de {} = {} ".format(datos_jugador2, dice2))
        if dice1 < dice2:
            resta = str(dice2 - dice1)
            print(datos_jugador2[0] + " gana " + resta)
            for jugador in players:
                if jugador1 == jugador:
                    players[jugador]["points"] += int(resta)  # Actualiza los puntos del jugador 2
        elif dice1 == dice2:
            print("Empate")
        else:
            resta = str(dice1 - dice2)
            print(datos_jugador1[0] + " gana " + resta)
            for jugador in players:
                if jugador1 == jugador:
                    players[jugador]["points"] += int(resta)  # Actualiza los puntos del jugador 1

        flag01 = True
        flag04 = False
