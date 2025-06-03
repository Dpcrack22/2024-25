"""
Vamos a hacer un programa el cual teine una cadena de strings de jugadores de basketball con las siguientes caracteristicas:
- Cada jugador tiene un nombre.
- Cada jugador tiene una velocidad y una precision
- Cada jugador tiene su altura y su peso
Todo esto dividido de las siguiente manera:
nombre,velociadad:precision,altura;peso

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

jugadores = "LeBron James,30:90,206;113-Stephen Curry,28:95,191;86-Kobe Bryant,29:85,198;96"
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
        opcion = input("Selecciona una opcion: ")
        if not opcion.isdigit():
            print("Por favor, introduce un numero valido.")
        else:
            opcion = int(opcion)
            if not opcion in range(1, 5):
                print("Por favor, selecciona una opcion del menu.")
            else:
                if opcion == 1:
                    flag_01 = True
                    flag_00 = False
                if opcion == 2:
                    flag_02 = True
                    flag_00 = False
                if opcion == 3:
                    flag_03 = True
                    flag_00 = False
                if opcion == 4:
                    salir = False
                    print("Saliendo del programa...")
                
    
    while flag_01:
        new_jugador = input("Añade un nuevo jugador: ")
        if new_jugador in jugadores:
            print("El jugador ya existe.")
        
        velocidad = input("Introduce la velocidad del jugador: ")
        if not velocidad.isdigit():
            print("Por favor, introduce un numero valido para la velocidad.")
        
        precision = input("Introduce la precision del jugador: ")
        if not precision.isdigit():
            print("Por favor, introduce un numero valido para la precision.")
        
        altura = input("Introduce la altura del jugador: ")
        if not altura.isdigit():
            print("Por favor, introduce un numero valido para la altura.")
        
        peso = input("Introduce el peso del jugador: ")
        if not peso.isdigit():
            print("Por favor, introduce un numero valido para el peso.")
        
        jugadores += "-{},{},{},{};{}".format(new_jugador, velocidad, precision, altura, peso)
        print("Jugador añadido correctamente.")
        input("Presiona Enter para continuar...")
        flag_00 = True
        flag_01 = False

    while flag_02:
        print(menu02)
        opcion = input("Selecciona una opcion: ")
        if not opcion.isdigit():
            print("Por favor, introduce un numero valido.")
        else:
            opcion = int(opcion)
            if not opcion in range(1, 7):
                print("Por favor, selecciona una opcion del menu.")
            else:
                print("Jugadores".center(50, "*") + "\n" + "Nombre".ljust(20) + "Velocidad".ljust(10) + "Precision".ljust(10) + "Altura".ljust(10) + "Peso".rjust(10))
                total_jugadores = jugadores.count("-") + 1
                datos = []

                total_jugadores = jugadores.count("-") + 1
                for i in range(total_jugadores):
                    if i == 0:
                        inicio = 0
                        final = jugadores.find("-")
                        jugador_iesmo = jugadores[inicio:final]

                    else:
                        inicio = final + 1
                        final = jugadores.find("-", inicio)
                        jugador_iesmo = jugadores[inicio:final]
                    
                    # jugadores = "LeBron James,30:90,206;113-Stephen Curry,28:95,191;86-Kobe Bryant,29:85,198;96"

                    asterisco1 = jugador_iesmo.find(",")
                    asterisco2 = jugador_iesmo.find(":", asterisco1)
                    asterisco3 = jugador_iesmo.find(";", asterisco2)
                    
                    nombre = jugador_iesmo[:asterisco1]
                    velocidad = jugador_iesmo[asterisco1 + 1:asterisco2]
                    precision_altura = jugador_iesmo[asterisco2 + 1:asterisco3]
                    precision = precision_altura[:precision_altura.find(",")]
                    altura = precision_altura[precision_altura.find(",") + 1:]
                    peso = jugador_iesmo[asterisco3 + 1:]

                    
                    datos.append([nombre, velocidad, precision, altura, peso])
                #print(datos)
                if opcion == 1:
                    for i in range(len(datos)-1):
                        for j in range(len(datos)- 1 - i):
                            if datos[j][0] > datos[j+1][0]:
                                aux = datos[j]
                                datos[j] = datos[j+1]
                                datos[j+1] = aux
                    lista_jugadores = ""
                    for jugador in datos:
                        nombre = jugador[0]
                        velocidad = jugador[1]
                        precision = jugador[2]
                        altura = jugador[3]
                        peso = jugador[4]
                        lista_jugadores += nombre.ljust(20) + velocidad.ljust(10) + precision.ljust(10) + altura.ljust(10) + peso.rjust(10) + "\n"
                    print(lista_jugadores)

                if opcion == 2:
                    for i in range(len(datos)-1):
                        for j in range(len(datos)- 1 - i):
                            if datos[j][1] > datos[j+1][1]:
                                aux = datos[j]
                                datos[j] = datos[j+1]
                                datos[j+1] = aux
                    lista_jugadores = ""
                    for jugador in datos:
                        nombre = jugador[0]
                        velocidad = jugador[1]
                        precision = jugador[2]
                        altura = jugador[3]
                        peso = jugador[4]
                        lista_jugadores += nombre.ljust(20) + velocidad.ljust(10) + precision.ljust(10) + altura.ljust(10) + peso.rjust(10) + "\n"
                    print(lista_jugadores)
                
                if opcion == 3:
                    for i in range(len(datos)-1):
                        for j in range(len(datos)- 1 - i):
                            if datos[j][2] > datos[j+1][2]:
                                aux = datos[j]
                                datos[j] = datos[j+1]
                                datos[j+1] = aux
                    lista_jugadores = ""
                    for jugador in datos:
                        nombre = jugador[0]
                        velocidad = jugador[1]
                        precision = jugador[2]
                        altura = jugador[3]
                        peso = jugador[4]
                        lista_jugadores += nombre.ljust(20) + velocidad.ljust(10) + precision.ljust(10) + altura.ljust(10) + peso.rjust(10) + "\n"
                    print(lista_jugadores)

                if opcion == 4:
                    for i in range(len(datos)-1):
                        for j in range(len(datos)- 1 - i):
                            if datos[j][3] > datos[j+1][3]:
                                aux = datos[j]
                                datos[j] = datos[j+1]
                                datos[j+1] = aux
                    lista_jugadores = ""
                    for jugador in datos:
                        nombre = jugador[0]
                        velocidad = jugador[1]
                        precision = jugador[2]
                        altura = jugador[3]
                        peso = jugador[4]
                        lista_jugadores += nombre.ljust(20) + velocidad.ljust(10) + precision.ljust(10) + altura.ljust(10) + peso.rjust(10) + "\n"
                    print(lista_jugadores)

                if opcion == 5:
                    for i in range(len(datos)-1):
                        for j in range(len(datos)- 1 - i):
                            if datos[j][4] > datos[j+1][4]:
                                aux = datos[j]
                                datos[j] = datos[j+1]
                                datos[j+1] = aux
                    lista_jugadores = ""
                    for jugador in datos:
                        nombre = jugador[0]
                        velocidad = jugador[1]
                        precision = jugador[2]
                        altura = jugador[3]
                        peso = jugador[4]
                        lista_jugadores += nombre.ljust(20) + velocidad.ljust(10) + precision.ljust(10) + altura.ljust(10) + peso.rjust(10) + "\n"
                    print(lista_jugadores)

                if opcion == 6:
                    flag_00 = True
                    flag_02 = False

        input("Presiona Enter para continuar...")

    while flag_03:
        print(menu03)
        opcion = input("Selecciona una opcion: ")
        if not opcion.isdigit():
            print("Por favor, introduce un numero valido.")
        else:
            opcion = int(opcion)
            if not opcion in range(1, 5):
                print("Por favor, selecciona una opcion del menu.")
            else:
                if opcion == 1:
                    nombre_buscar = input("Introduce el nombre del jugador a buscar: ")
                    encontrado = False
                    total_jugadores = jugadores.count("-") + 1
                    for i in range(total_jugadores):
                        if i == 0:
                            inicio = 0
                            final = jugadores.find("-")
                            jugador_iesmo = jugadores[inicio:final]
                        else:
                            inicio = final + 1
                            final = jugadores.find("-", inicio)
                            jugador_iesmo = jugadores[inicio:final]
                        
                        asterisco1 = jugador_iesmo.find(",")
                        nombre = jugador_iesmo[:asterisco1]
                        
                        #Si quiero buscar el nombre identico es:
                        """
                        if nombre.lower() == nombre_buscar.lower():
                            encontrado = True
                            asterisco2 = jugador_iesmo.find(":", asterisco1)
                            asterisco3 = jugador_iesmo.find(";", asterisco2)
                            velocidad = jugador_iesmo[asterisco1 + 1:asterisco2]
                            precision_altura = jugador_iesmo[asterisco2 + 1:asterisco3]
                            precision = precision_altura[:precision_altura.find(",")]
                            altura = precision_altura[precision_altura.find(",") + 1:]
                            peso = jugador_iesmo[asterisco3 + 1:]
                            print("Nombre: {}, Velocidad: {}, Precision: {}, Altura: {}, Peso: {}".format(nombre, velocidad, precision, altura, peso))
                        """
                        #Si quiero buscar el nombre que contenga la palabra:
                        if nombre_buscar.lower() in nombre.lower():
                            encontrado = True
                            asterisco2 = jugador_iesmo.find(":", asterisco1)
                            asterisco3 = jugador_iesmo.find(";", asterisco2)
                            velocidad = jugador_iesmo[asterisco1 + 1:asterisco2]
                            precision_altura = jugador_iesmo[asterisco2 + 1:asterisco3]
                            precision = precision_altura[:precision_altura.find(",")]
                            altura = precision_altura[precision_altura.find(",") + 1:]
                            peso = jugador_iesmo[asterisco3 + 1:]
                            print("Nombre: {}, Velocidad: {}, Precision: {}, Altura: {}, Peso: {}".format(nombre, velocidad, precision, altura, peso))
                        

                    if not encontrado:
                        print("No se ha encontrado ningun jugador con ese nombre.")
               
                if opcion == 2:
                    precision_buscar = input("Introduce la precision del jugador a buscar: ")
                    encontrado = False
                    total_jugadores = jugadores.count("-") + 1
                    for i in range(total_jugadores):
                        if i == 0:
                            inicio = 0
                            final = jugadores.find("-")
                            jugador_iesmo = jugadores[inicio:final]
                        else:
                            inicio = final + 1
                            final = jugadores.find("-", inicio)
                            jugador_iesmo = jugadores[inicio:final]
                        
                        asterisco1 = jugador_iesmo.find(",")
                        asterisco2 = jugador_iesmo.find(":", asterisco1)
                        asterisco3 = jugador_iesmo.find(";", asterisco2)
                        precision_altura = jugador_iesmo[asterisco2 + 1:asterisco3]
                        precision = precision_altura[:precision_altura.find(",")]
                        
                        if precision == precision_buscar:
                            encontrado = True
                            nombre = jugador_iesmo[:asterisco1]
                            altura = precision_altura[precision_altura.find(",") + 1:]
                            peso = jugador_iesmo[asterisco3 + 1:]
                            print("Nombre: {}, Velocidad: {}, Precision: {}, Altura: {}, Peso: {}".format(nombre, velocidad, precision, altura, peso))
                    
                    if not encontrado:
                        print("No se ha encontrado ningun jugador con esa precision.")
                
                if opcion == 3:
                    altura_buscar = input("Introduce la altura del jugador a buscar: ")
                    encontrado = False
                    total_jugadores = jugadores.count("-") + 1
                    for i in range(total_jugadores):
                        if i == 0:
                            inicio = 0
                            final = jugadores.find("-")
                            jugador_iesmo = jugadores[inicio:final]
                        else:
                            inicio = final + 1
                            final = jugadores.find("-", inicio)
                            jugador_iesmo = jugadores[inicio:final]
                        
                        asterisco1 = jugador_iesmo.find(",")
                        asterisco2 = jugador_iesmo.find(":", asterisco1)
                        asterisco3 = jugador_iesmo.find(";", asterisco2)
                        precision_altura = jugador_iesmo[asterisco2 + 1:asterisco3]
                        altura = precision_altura[precision_altura.find(",") + 1:]
                        
                        if altura == altura_buscar:
                            encontrado = True
                            nombre = jugador_iesmo[:asterisco1]
                            velocidad = jugador_iesmo[asterisco1 + 1:asterisco2]
                            peso = jugador_iesmo[asterisco3 + 1:]
                            print("Nombre: {}, Velocidad: {}, Precision: {}, Altura: {}, Peso: {}".format(nombre, velocidad, precision, altura, peso))
                    
                    if not encontrado:
                        print("No se ha encontrado ningun jugador con esa altura.")
                    
                
                if opcion == 4:
                    flag_00 = True
                    flag_03 = False

        input("Presiona Enter para continuar...")