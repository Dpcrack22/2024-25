"""
Vamos a hacer un programa el cual teine un diccionario de jugadores de basketball con las siguientes caracteristicas:
- Cada jugador tiene un nombre.
- Cada jugador tiene una velocidad y una precision
- Cada jugador tiene su altura y su peso
Todo esto dividido de las siguiente manera:
nombre{"velocidad": velocidad, "precision": precision, "altura": altura, "peso": peso}

Con esto vamos a crear un programa el cual tendra un menu que nos muestre las siguientes opciones:
1. Añadir un jugador
2. Mostrar todos los jugadores
3. Buscar un jugador
4. Salir

Si seleccionamos la opcion 1, nos pedira que introduzcamos los datos del jugador y lo añadira a la cadena de strings de jugadores.
Si seleccionamos la opcion 2, nos mostrara otro menu con las siguientes opciones:
1. Mostrar por nombre
2. Mostrar por velocidad
3. Mostrar por precision
4. Mostrar por altura
5. Mostrar por peso
6. Volver al menu principal

Si seleccionamos la opcion 3, nos mostrara otro menu con las siguientes opciones:
1. Buscar por nombre
2. Buscar por precision
3. Buscar por altura
4. Volver al menu principal

"""

jugadores = {"Michael Jordan": {"velocidad": 90, "precision": 95, "altura": 198, "peso": 98},
            "LeBron James": {"velocidad": 88, "precision": 92, "altura": 206, "peso": 113},
            "Kobe Bryant": {"velocidad": 85, "precision": 93, "altura": 198, "peso": 96}}
menu00 = "Menu Principal".center(50, "*") + "\n1. Añadir un jugador\n2. Mostrar todos los jugadores\n3. Buscar un jugador\n4. Salir\n" + "*" * 50
menu02 = "Menu Mostrar Jugadores".center(50, "*") + "\n1. Mostrar por nombre\n2. Mostrar por velocidad\n3. Mostrar por precision\n4. Mostrar por altura\n5. Mostrar por peso\n6. Volver al menu principal\n" + "*" * 50
menu03 = "Menu Buscar Jugadores".center(50, "*") + "\n1. Buscar por nombre\n2. Buscar por precision\n3. Buscar por altura\n4. Volver al menu principal\n" + "*" * 50

salir = True
flag_00 = True
flag_01 = False
flag_02 = False
flag_03 = False
flag_04 = False

while salir:
    while flag_00:
        print(menu00)
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
            print("Por favor, ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion not in range(1, 5):
                print("Opción no válida, por favor intente de nuevo.")
            else:
                if opcion == 1:
                    flag_01 = True
                    flag_00 = False
                elif opcion == 2:
                    flag_02 = True
                    flag_00 = False
                elif opcion == 3:
                    flag_03 = True
                    flag_00 = False
                elif opcion == 4:
                    salir = False
                    print("Saliendo del programa...")


    while flag_01:
        print("Añadir un jugador".center(50, "*"))
        while True:
            nombre = input("Ingrese el nombre del jugador: ")
            for i in range(len(jugadores)):
                if nombre in jugadores:
                    print("El jugador {} ya existe. Por favor, ingrese un nombre diferente.".format(nombre))
            else:
                break
        while True:
            velocidad = input("Ingrese la velocidad del jugador: ")
            if not velocidad.isdigit():
                print("Por favor, ingrese un valor numérico válido para velocidad.")
            else:
                break
        
        while True:
            precision = input("Ingrese la precisión del jugador: ")
            if not precision.isdigit():
                print("Por favor, ingrese un valor numérico válido para precisión.")
            else:
                break
        while True:
            altura = input("Ingrese la altura del jugador: ")
            if not altura.isdigit():
                print("Por favor, ingrese un valor numérico válido para altura.")
            else:
                break
        while True:
            peso = input("Ingrese el peso del jugador: ")
            if not peso.isdigit():
                print("Por favor, ingrese un valor numérico válido para peso.")
            else:
                break

        jugadores[nombre] = {
            "velocidad": int(velocidad),
            "precision": int(precision),
            "altura": int(altura),
            "peso": int(peso)
        }

        

        flag_01 = False
        flag_00 = True

    while flag_02:
        print(menu02)
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
            print("Por favor, ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion not in range(1, 7):
                print("Opción no válida, por favor intente de nuevo.")
            else:
                if opcion == 1:
                    datos = ""
                    lista_nombres = list(jugadores.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if lista_nombres[i] > lista_nombres[i+1]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                
                    for name in lista_nombres:
                        datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                    
                    print("Jugadores".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                    print(datos)
                    input("Presione Enter para continuar...")

                if opcion == 2:
                    datos = ""
                    lista_nombres = list(jugadores.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if jugadores[lista_nombres[i]]["velocidad"] < jugadores[lista_nombres[i+1]]["velocidad"]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                
                    for name in lista_nombres:
                        datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                    
                    print("Jugadores".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                    print(datos)
                    input("Presione Enter para continuar...")

                
                if opcion == 3:
                    datos = ""
                    lista_nombres = list(jugadores.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if jugadores[lista_nombres[i]]["precision"] < jugadores[lista_nombres[i+1]]["precision"]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                
                    for name in lista_nombres:
                        datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                    
                    print("Jugadores".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                    print(datos)
                    input("Presione Enter para continuar...")

                if opcion == 4:
                    datos = ""
                    lista_nombres = list(jugadores.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if jugadores[lista_nombres[i]]["altura"] < jugadores[lista_nombres[i+1]]["altura"]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                
                    for name in lista_nombres:
                        datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                    
                    print("Jugadores".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                    print(datos)
                    input("Presione Enter para continuar...")
                
                if opcion == 5:
                    datos = ""
                    lista_nombres = list(jugadores.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if jugadores[lista_nombres[i]]["peso"] < jugadores[lista_nombres[i+1]]["peso"]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                
                    for name in lista_nombres:
                        datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                    
                    print("Jugadores".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                    print(datos)
                    input("Presione Enter para continuar...")

                elif opcion == 6:
                    flag_02 = False
                    flag_00 = True

    while flag_03:
        print(menu03)
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
            print("Por favor, ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion not in range(1, 5):
                print("Opción no válida, por favor intente de nuevo.")
            else:
                encontrado = False
                datos = ""
                if opcion == 1:
                    nombre = input("Ingrese el nombre del jugador a buscar: ")
                    for name in jugadores:
                        if nombre.lower() in name.lower():
                            encontrado = True
                            datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                    if encontrado:
                        print("Jugador encontrado:".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                        print(datos)
                        input("Presione Enter para continuar...")
                    else:
                        print("Jugador no encontrado.")
                        input("Presione Enter para continuar...")

                if opcion == 2:
                    precision = input("Ingrese la precisión del jugador a buscar: ")
                    if not precision.isdigit():
                        print("Por favor, ingrese un valor numérico válido para precisión.")
                    else:
                        precision = int(precision)
                        for name in jugadores:
                            if jugadores[name]["precision"] == precision:
                                encontrado = True
                                datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                        
                        if encontrado:
                            print("Jugador encontrado:".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                            print(datos)
                            input("Presione Enter para continuar...")
                        else:
                            print("Jugador no encontrado.")
                            input("Presione Enter para continuar...")

                if opcion == 3:
                    altura = input("Ingrese la altura del jugador a buscar: ")
                    if not altura.isdigit():
                        print("Por favor, ingrese un valor numérico válido para altura.")
                    else:
                        altura = int(altura)
                        for name in jugadores:
                            if jugadores[name]["altura"] == altura:
                                encontrado = True
                                datos += name.ljust(20) + str(jugadores[name]["velocidad"]).rjust(10) + str(jugadores[name]["precision"]).rjust(10) + str(jugadores[name]["altura"]).rjust(10) + str(jugadores[name]["peso"]).rjust(10) + "\n"
                        
                        if encontrado:
                            print("Jugador encontrado:".center(60, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10) + "\n" + "*" * 60)
                            print(datos)
                            input("Presione Enter para continuar...")
                        else:
                            print("Jugador no encontrado.")
                            input("Presione Enter para continuar...")

                elif opcion == 4:
                    flag_03 = False
                    flag_00 = True