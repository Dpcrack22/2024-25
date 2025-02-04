import random  # Importa el módulo random, que se usa para generar números aleatorios.

# Definición de los personajes, armas, tripulaciones, rangos y categorías en diccionarios.

# Diccionario de personajes. Cada personaje tiene atributos como nombre, categoría, armas, fuerza, velocidad y experiencia.
dict_characters = {
    1: {"name": "Luffy", "category": 1, "weapons": [1, 1], "strength": 6, "speed": 7, "experience": 0},
    2: {"name": "Zoro", "category": 1, "weapons": [], "strength": 5, "speed": 6, "experience": 0},
    3: {"name": "Sanji", "category": 1, "weapons": [1, 3], "strength": 4, "speed": 6, "experience": 0},
    4: {"name": "Buggy", "category": 2, "weapons": [3], "strength": 2, "speed": 4, "experience": 0},
    5: {"name": "Mr3", "category": 2, "weapons": [5], "strength": 3, "speed": 2, "experience": 0},
    6: {"name": "Xebec", "category": 3, "weapons": [1, 3], "strength": 6, "speed": 5, "experience": 0},
    7: {"name": "Kaido", "category": 3, "weapons": [4], "strength": 8, "speed": 3, "experience": 0},
    8: {"name": "Mama grande", "category": 3, "weapons": [5], "strength": 7, "speed": 1, "experience": 0},
    9: {"name": "Akainu", "category": 4, "weapons": [2], "strength": 6, "speed": 4, "experience": 0},
    10: {"name": "Kizaru", "category": 4, "weapons": [1, 3], "strength": 5, "speed": 8, "experience": 0},
    11: {"name": "Fujitora", "category": 4, "weapons": [5], "strength": 5, "speed": 4, "experience": 0},
    12: {"name": "Garp", "category": 5, "weapons": [2], "strength": 6, "speed": 3, "experience": 0},
    13: {"name": "Smoker", "category": 5, "weapons": [5], "strength": 5, "speed": 5, "experience": 0},
    14: {"name": "Koby", "category": 6, "weapons": [4], "strength": 3, "speed": 4, "experience": 0},
    15: {"name": "Tashigi", "category": 6, "weapons": [3], "strength": 4, "speed": 4, "experience": 0},
}

# Diccionario de armas disponibles. Cada arma tiene atributos como fuerza, velocidad y si es de dos manos.
dict_weapons = {
    1: {"name": "Sword", "strength": 3, "speed": 5, "two_hand": False},
    2: {"name": "Greatsword", "strength": 5, "speed": 3, "two_hand": True},
    3: {"name": "Gun", "strength": 2, "speed": 6, "two_hand": False},
    4: {"name": "Rifle", "strength": 3, "speed": 4, "two_hand": True},
    5: {"name": "Chuchi", "strength": 4, "speed": 4, "two_hand": True},
}

# Diccionario de tripulaciones, que contiene una lista de miembros por ID.
dict_crews = {
    1: {"name": "Straw hat", "members": [8, 6]},
    2: {"name": "Pirates Buggy", "members": [1, 3, 5]},
    3: {"name": "Pirates Rocks", "members": [2, 4, 7]},
}

# Diccionario de rangos dentro de la marina, con sus respectivos miembros.
dict_ranks = {
    1: {"name": "Admiral", "members": [9, 10, 11]},
    2: {"name": "ViceAdmiral", "members": [12, 13]},
    3: {"name": "Lieutenant", "members": [14, 15]},
}

# Diccionario de categorías, que asocia números con los nombres de las categorías.
dict_categorys = {
    1: "Straw hat",
    2: "Pirates Buggy",
    3: "Pirates Rocks",
    4: "Admiral",
    5: "ViceAdmiral",
    6: "Lieutenant",
}

# Menú principal y otros submenús que permiten interactuar con el programa.

menu00 = "Menu 0 (One Piece)".center(40, "=") + "\n" + "\n" + "1) Play" + "\n" + "2) Create" + "\n" + "3) Edit" + "\n" + "4) List" + "\n" + "5) Exit"
menu02 = "Menu 02 (Create)".center(40, "=") + "\n" + "\n" + "1) Create Character" + "\n" + "2) Create Weapon" + "\n" + "3) Go Back"
menu03 = "Menu 03 (Edit Menu)".center(40, "=") + "\n" + "\n" + "1) Edit Character" + "\n" + "2) Edit Weapon" + "\n" + "3) Go Back"
menu04 = "Menu 04 (List)".center(40, "=") + "\n" + "\n" + "1) List Character" + "\n" + "2) List Weapons" + "\n" + "3) List Side" + "\n" + "4) List Range" + "\n" + "5) Go Back"
menu021 = "Menu 021 (New Character)".center(40, "=")
menu022 = "Menu 022 (New Weapon)".center(40, "=")
menu031 = "Menu 031 (Edit Character)".center(40, "=")
menu032 = "Menu 032 (Edit Weapon)".center(40, "=")
menu041 = "Menu 041 (List Character)".center(40, "=") + "\n" + "\n" + "1) List by ID" + "\n" + "2) List by Name" + "\n" + "3) List by Strength" + "\n" + "4) List by Speed" + "\n" + "5) Go Back"
menu042 = "Menu 042 (List Weapons)".center(40, "=") + "\n" + "\n" + "1) List by ID" + "\n" + "2) List by Name" + "\n" + "3) List by Strength" + "\n" + "4) List by Speed" + "\n" + "5) Go Back"

# Variables de control de flujo, como flags que determinan qué menú o acción se está ejecutando.
runing = True  # Bandera principal que controla el bucle del programa.
flag0 = True    # Bandera para controlar si el menú principal está activo.
flag1 = False   # Flag para otras funcionalidades (no se usa en el código actual).
flag2 = False   # Flag para indicar que el menú de creación está activo.
flag3 = False   # Flag para indicar que el menú de edición está activo.
flag4 = False   # Flag para indicar que el menú de listado está activo.
flag21 = False  # Flag para crear un personaje.
flag22 = False  # Flag para crear un arma.
flag23 = False  # Flag para editar un personaje (no se usa actualmente).
flag24 = False  # Flag para editar un arma (no se usa actualmente).
flag31 = False  # Flag para editar un personaje (no se usa actualmente).
flag32 = False  # Flag para editar un arma (no se usa actualmente).
flag41 = False  # Flag para listar personajes (no se usa actualmente).
flag42 = False  # Flag para listar armas (no se usa actualmente).

# Menú principal, donde el jugador selecciona qué acción realizar.
while runing:
    while flag0:
        print(menu00)  # Muestra el menú principal.
        choice = input("Enter your choice: ")  # Solicita al usuario una opción.

        if not choice.isdigit():  # Si la opción no es un número, muestra un error.
            print("Only numerical option")
            input("Retry: ")

        else:    
            choice = int(choice)  # Convierte la entrada en un número entero.
            
            if choice == 1:
                print("Playing the game...")  # Aquí se podría implementar el juego.
                flag0 = False  # Salir del menú principal.
            elif choice == 2:
                print(menu02)  # Muestra el menú de creación de personajes y armas.
                flag2 = True
                flag0 = False
            elif choice == 3:
                print(menu03)  # Muestra el menú de edición de personajes y armas.
                flag3 = True
                flag0 = False
            elif choice == 4:
                print(menu04)  # Muestra el menú de listado de personajes y armas.
                flag4 = True
                flag0 = False
            elif choice == 5:
                runing = False  # Salir del programa.
                flag0 = False
    # Bucle principal para manejar la selección de opciones del menú
    while flag2:
        # Se muestra el menú para crear un personaje o un arma
        print(menu02)
        choice = input("Enter your choice: ")
        
        # Se verifica si la entrada es numérica
        if not choice.isdigit():
            print("Only numerical option")
            input("Press Enter to continue...")  # Pausa para que el usuario vea el mensaje
        choice = int(choice)
        
        # Se verifica que la opción seleccionada esté dentro del rango válido (1-3)
        if choice not in range(1, 4):
            print("Not in range option")
            input("Press Enter to ")
            
        # Si la opción es 1, se va a crear un personaje
        if choice == 1:
            flag2 = False  # Salimos del bucle principal de selección de menú
            flag21 = True   # Activamos el flag para crear un personaje
        # Si la opción es 2, se va a crear un arma
        elif choice == 2:
            flag2 = False
            flag22 = True   # Activamos el flag para crear un arma
        # Si la opción es 3, se vuelve al menú principal
        elif choice == 3:  
            flag2 = False  
            flag0 = True    # Activamos el flag que regresa al menú principal
        else:
            print("Invalid choice. Please try again.")  # Si la entrada no es válida, se muestra un mensaje de error


    # Bucle para la creación de un personaje
    while flag21:
        print(menu021)
        character_name = input("Name of the new character:\n-> ")  # Pedimos el nombre del personaje

        # Bucle para seleccionar el bando (Marina o Piratas)
        valid_side_choice = False
        while not valid_side_choice:
            print("\nSide of the new character: \n1) Marine\n2) Pirates")
            side_choice = input("-> Option: ")
            
            # Verificamos que la opción sea 1 o 2
            if side_choice.isdigit() and int(side_choice) in [1, 2]:
                side_choice = int(side_choice)
                valid_side_choice = True
            else:
                print("Invalid choice. Please enter 1 or 2.")  # Si la opción no es válida, se muestra un mensaje de error

        # Asignamos el bando y los rangos disponibles según la elección
        if side_choice == 1:
            side = "Marine"
            available_ranks = list(dict_ranks.values())  # Rangos de la Marina
        else:
            side = "Pirates"
            available_ranks = list(dict_crews.values())  # Rangos de los Piratas

        print("\nRank or crew of the new character:")
        rank_index = 1
        # Mostramos los rangos disponibles
        for rank in available_ranks:
            if 'name' in rank:
                print("{}: {}".format(rank_index, rank['name']))
                rank_index += 1

        # Bucle para seleccionar el rango o tripulación del personaje
        valid_rank_choice = False
        while not valid_rank_choice:
            if rank_index == 1:
                print("No valid ranks available. Please check the data.")  # Si no hay rangos, mostramos un mensaje de error
                break

            # Pedimos la opción de rango
            rank_choice = input("-> Option: ")
            if rank_choice.isdigit() and 1 <= int(rank_choice) < rank_index:
                rank_choice = int(rank_choice)
                character_rank = available_ranks[rank_choice - 1]["name"]  # Obtenemos el nombre del rango seleccionado
                valid_rank_choice = True
            else:
                print("Invalid choice. Please select a valid rank.")  # Si la opción no es válida, mostramos un mensaje de error

        if not valid_rank_choice:
            break  # Si no se ha validado correctamente, salimos del bucle de creación del personaje

        # Creamos el diccionario del personaje con sus atributos
        new_character = {
            "name": character_name,
            "category": character_rank,
            "weapons": [],  # Inicialmente, el personaje no tiene armas
            "strength": random.randint(1, 10),  # Fuerza aleatoria entre 1 y 10
            "speed": random.randint(1, 10),  # Velocidad aleatoria entre 1 y 10
            "experience": 0  # La experiencia inicia en 0
        }

        available_weapons = dict_weapons.copy()  # Copiamos el diccionario de armas disponibles
        selected_weapons = []  # Lista para almacenar las armas seleccionadas
        two_handed_selected = False  # Flag para verificar si se ha seleccionado un arma de dos manos

        # Mostramos las estadísticas iniciales del personaje
        print("Strength: {}".format(new_character['strength']))
        print("Speed: {}".format(new_character['speed']))

        # Bucle para seleccionar las armas del personaje
        while True:
            print("\n===========Available Weapons============")
            # Mostramos las armas disponibles
            for weapon_id, weapon in available_weapons.items():
                print("{}: {}, Two-handed: {}, Strength: {}, Speed: {}".format(
                    weapon_id, weapon['name'], weapon['two_hand'], weapon['strength'], weapon['speed']))

            print("\n===========Character weapons:===========")
            # Mostramos las armas que el personaje ya ha seleccionado
            if selected_weapons:
                for weapon_id in selected_weapons:
                    weapon = dict_weapons[weapon_id]
                    print("{}: {}, Two-handed: {}, Strength: {}, Speed: {}".format(
                        weapon_id, weapon['name'], weapon['two_hand'], weapon['strength'], weapon['speed']))
            else:
                print("------------------None------------------")  # Si no tiene armas, mostramos que no tiene

            # Pedimos al usuario que seleccione un arma
            weapon_choice = input("-> Option (0 to finish selecting weapons): ")

            if weapon_choice.isdigit():
                weapon_choice = int(weapon_choice)

                # Si elige 0, terminamos la selección de armas
                if weapon_choice == 0:
                    break

                elif weapon_choice in available_weapons:
                    selected_weapon = available_weapons[weapon_choice]

                    # Si el arma es de dos manos, solo puede elegir una
                    if selected_weapon['two_hand']:
                        print("You selected a Two-handed weapon. No more weapons can be selected.")
                        selected_weapons = [weapon_choice]  # Asignamos solo esa arma
                        two_handed_selected = True  # Marcamos que ya se seleccionó un arma de dos manos
                        break
                    else:
                        selected_weapons.append(weapon_choice)  # Si no es de dos manos, se agrega a la lista
                        new_character['strength'] += selected_weapon['strength']  # Aumentamos la fuerza
                        new_character['speed'] += selected_weapon['speed']  # Aumentamos la velocidad
                        del available_weapons[weapon_choice]  # Eliminamos el arma seleccionada de las disponibles
                else:
                    print("Invalid weapon choice. Please try again.")  # Si la opción de arma no es válida

            else:
                print("Invalid input. Please enter a number.")  # Si la entrada no es numérica, mostramos un error

        # Asignamos las armas seleccionadas al personaje
        new_character["weapons"] = selected_weapons

        # Mostramos un resumen del nuevo personaje
        print("\nThe new player will be:")
        print("Name: {}".format(new_character['name']))
        print("Category: {}".format(character_rank))

        # Mostramos las armas seleccionadas
        if selected_weapons:
            weapon_names = ""
            for weapon_id in selected_weapons:
                weapon = dict_weapons[weapon_id]
                weapon_names += weapon['name'] + ", "
            weapon_names = weapon_names[:-2]  # Eliminamos la última coma
            print("Weapons: {}".format(weapon_names))
        else:
            print("Weapons: None")  # Si no tiene armas, indicamos que no tiene

        # Mostramos las estadísticas finales del personaje
        print("Strength: {}".format(new_character['strength']))
        print("Speed: {}".format(new_character['speed']))
        print("Experience: {}".format(new_character['experience']))

        # Preguntamos al usuario si desea guardar el personaje
        save_choice = input("Save this player? (Y/N): ").lower()
        if save_choice == 'y':
            dict_characters[len(dict_characters) + 1] = new_character  # Guardamos el personaje en el diccionario
            print("Character saved successfully!")
        else:
            print("Character creation cancelled.")  # Si no lo guarda, cancelamos la creación del personaje

        flag21 = False  # Terminamos el proceso de creación de personajes
        flag0 = True  # Volvemos al menú principal


    # Bucle para la creación de un arma
    while flag22:
        print(menu022)
        weapon_name = input("Name of the new weapon:\n-> ")

        # Bucle para seleccionar el tipo de arma (una o dos manos)
        valid_weapon_type_choice = False
        while not valid_weapon_type_choice:
            print("Select the type of weapon:\n1) One-handed\n2) Two-handed")
            weapon_type = input("-> Option: ")
            if weapon_type.isdigit() and int(weapon_type) in [1, 2]:
                weapon_type = int(weapon_type)
                valid_weapon_type_choice = True
            else:
                print("Invalid choice. Please enter 1 or 2.")

        # Bucle para ingresar la fuerza del arma
        valid_weapon_strength = False
        while not valid_weapon_strength:
            weapon_strength = input("Enter weapon strength (1-10): ")
            if weapon_strength.isdigit() and 1 <= int(weapon_strength) <= 10:
                weapon_strength = int(weapon_strength)
                valid_weapon_strength = True
            else:
                print("Invalid value. Please enter a number between 1 and 10.")  # Validación de la fuerza del arma
        
        valid_weapon_speed = False
        while not valid_weapon_speed:
            weapon_speed = input("Enter weapon speed (1-10): ")
            if weapon_speed.isdigit() and 1 <= int(weapon_speed) <= 10:
                weapon_speed = int(weapon_speed)
                valid_weapon_speed = True
            else:
                print("Invalid value. Please enter a number between 1 and 10.")

        # Creación del diccionario del arma con sus atributos
        new_weapon = {
            "name": weapon_name,
            "two_hand": weapon_type == 2,  # Si es de dos manos, se marca como True
            "strength": weapon_strength,
            "speed": weapon_speed
        }
        print("\nThe new weapon will be:")
        print("Name: {}".format(new_weapon['name']))
        print("Two-handed: {}".format(new_weapon['two_hand']))
        print("Strength: {}".format(new_weapon['strength']))
        print("Speed: {}".format(new_weapon['speed']))
        # Preguntamos al usuario si desea guardar el arma
        save_choice = input("Save this weapon? (S/N): ").lower()
        if save_choice == 's':
            dict_weapons[len(dict_weapons) + 1] = new_weapon  # Guardamos el arma en el diccionario
            print("Weapon saved successfully!")
        else:
            print("Weapon creation cancelled.")  # Si no lo guarda, cancelamos la creación del arma

        flag22 = False  # Terminamos el proceso de creación del arma
        flag0 = True  # Volvemos al menú principal

    # Bucle principal que controla el menú de edición de personajes y armas
    while flag3:
        print(menu03)  # Imprime el menú de opciones
        choice = input("Enter your choice: ")  # Pide al usuario que ingrese una opción
        
        # Comprobamos que la opción ingresada sea un número
        if not choice.isdigit():
            print("Only numerical option")  # Si no es un número, mostramos un mensaje de error
            input("Retry: ")  # Pausa para que el usuario vea el mensaje de error

        else:
            choice = int(choice)  # Convertimos la opción a un número entero
            
            # Verificamos que la opción esté dentro del rango válido
            if choice not in range(1, 6):
                print("Not in range option")  # Si no está en el rango, mostramos un mensaje de error
                input("Retry: ")  # Pausa para que el usuario vea el mensaje de error
            else:
                # Si la opción es válida, se ejecutan las acciones correspondientes
                if choice == 1:
                    flag31 = True  # Activamos la flag para entrar en la edición de personajes
                    flag3 = False  # Salimos del bucle principal
                elif choice == 2:
                    flag32 = True  # Activamos la flag para entrar en la edición de armas
                    flag3 = False  # Salimos del bucle principal
                elif choice == 3:
                    flag3 = False  # Salimos del bucle principal
                    flag0 = True  # Activamos la flag para volver al menú anterior
                else:
                    print("Invalid choice. Please try again.")  # Si la opción es incorrecta, mostramos un mensaje

    # Bucle para la edición de personajes
    while flag31:
        print(menu031)  # Imprime el menú de edición de personajes
        auxiliar = []  # Lista auxiliar para almacenar la información de los personajes
        for key_id, valor_info in dict_characters.items():
            auxiliar.append([key_id, valor_info])  # Añadimos cada personaje al auxiliar
        for i in range(len(auxiliar)):  # Recorremos la lista auxiliar
            auxiliar_id = auxiliar[i][0]  # ID del personaje
            auxiliar_nombre = auxiliar[i][1]["name"]  # Nombre del personaje
            auxiliar_speed = auxiliar[i][1]["speed"]  # Velocidad del personaje
            auxiliar_strength = auxiliar[i][1]["strength"]  # Fuerza del personaje
            auxiliar_exp = auxiliar[i][1]["experience"]  # Experiencia del personaje
            print("ID: "+str(auxiliar_id),"Name:"+auxiliar_nombre, 
                "speed: "+str(auxiliar_speed), "strength: "+str(auxiliar_strength), 
                "experience: "+str(auxiliar_exp))  # Mostramos la información del personaje
        
        edit_character = True  # Flag para iniciar la edición de un personaje
        while edit_character:
            choice = input("Enter your choice: ")  # Pedimos al usuario que ingrese la ID del personaje
            
            # Comprobamos que la opción ingresada sea un número
            if not choice.isdigit():
                print("Only numerical option")  # Si no es un número, mostramos un mensaje de error
                input("Retry: ")  # Pausa para que el usuario vea el mensaje de error
            else:
                choice = int(choice)  # Convertimos la opción a un número entero
                
                # Verificamos si la ID del personaje es válida
                if choice not in dict_characters.keys():
                    print("Not in range option")  # Si no existe, mostramos un mensaje de error
                    input("Retry: ")  # Pausa para que el usuario vea el mensaje de error
                else:
                    # Si la ID es válida, mostramos el personaje seleccionado
                    print("Select feature to edit to character ID: {}, Name: {}".format(choice, dict_characters[choice]["name"]))
                    edit_character2 = True  # Flag para entrar en el submenú de edición de características
                    while edit_character2:
                        print("\n1)Name \n2)Weapon \n3)Go Back")  # Opciones para editar el personaje
                        choise2 = input("Seleccione una opcion: ")  # Pedimos al usuario que ingrese una opción
                        
                        # Comprobamos que la opción ingresada sea un número
                        if not choise2.isdigit():
                            print("Only numerical option")  # Si no es un número, mostramos un mensaje de error
                            input("Retry: ")  # Pausa para que el usuario vea el mensaje de error
                        else:
                            choise2 = int(choise2)  # Convertimos la opción a un número entero
                            
                            # Si la opción es 1, editamos el nombre del personaje
                            if choise2 == 1:
                                new_name = input("Enter new name: ")  # Pedimos el nuevo nombre
                                seleccion = input("Do you want to save the changes (Y/N): ").upper()  # Preguntamos si desea guardar los cambios
                                if seleccion == "Y":
                                    dict_characters[choice]["name"] = new_name  # Guardamos el nuevo nombre
                                    print("Select feature to edit to character ID: {}, Name: {}".format(choice, dict_characters[choice]["name"]))
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_character2 = False  # Salimos del bucle de edición de características
                                    edit_character = False  # Salimos del bucle de edición de personajes
                                    flag31 = False  # Desactivamos la flag de edición de personajes
                                elif seleccion == "N":
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_character2 = False  # Salimos del bucle de edición de características
                                    edit_character = False  # Salimos del bucle de edición de personajes
                                    flag31 = False  # Desactivamos la flag de edición de personajes
                                else:
                                    print("Invalid Option")  # Si la opción no es válida, mostramos un mensaje de error
                            
                            # Si la opción es 2, editamos las armas del personaje
                            elif choise2 == 2:
                                auxiliar2 = []  # Lista auxiliar para mostrar las armas disponibles
                                editar_arma_personaje = True  # Flag para editar las armas del personaje
                                while editar_arma_personaje:
                                    print("Available Weapons".center(40, "="))  # Mostramos las armas disponibles
                                    
                                    # Si el personaje no tiene armas, mostramos todas las armas disponibles
                                    if len(dict_characters[choice]["weapons"]) == 0:
                                        for key_id, valor_info in dict_weapons.items():
                                            auxiliar2.append([key_id, valor_info])  # Añadimos las armas al auxiliar
                                            print(key_id, ") ", valor_info["name"], ",", "Strength =", valor_info["strength"], ", Speed =", valor_info["speed"])  # Mostramos las armas
                                            auxiliar_armas = list(dict_weapons.keys())  # Lista de armas disponibles
                                    else:
                                        auxiliar_armas = []  # Lista de armas disponibles para el personaje
                                        # Si ya tiene armas, mostramos solo las armas que puede añadir
                                        for i in range(len(dict_characters[choice]["weapons"])):
                                            if dict_weapons[dict_characters[choice]["weapons"][i]]["two_hand"] == True or len(dict_characters[choice]["weapons"]) == 2:
                                                print("\n" + "No available weapons".center(40, "*") + "\n")  # Si no puede añadir más, mostramos un mensaje
                                                break
                                            else:
                                                for key_id, valor_info in dict_weapons.items():
                                                    if not valor_info["two_hand"]:  # Si el arma no es de dos manos
                                                        print(key_id, ") ", valor_info["name"], ",", "Strength =", valor_info["strength"], ", Speed =", valor_info["speed"])  # Mostramos la información del arma
                                                        auxiliar_armas.append(key_id)  # Añadimos el ID del arma a la lista de armas disponibles
                                    print("=" * 40)  # Separador para mejorar la presentación
                                    
                                    # Mostramos las armas que el personaje ya tiene
                                    for i in range(len(dict_characters[choice]["weapons"])):
                                        print(str(dict_characters[choice]["weapons"][i]) + 
                                            (") {}, strength :{}, speed: {}".format(
                                                dict_weapons[dict_characters[choice]["weapons"][i]]["name"],
                                                dict_weapons[dict_characters[choice]["weapons"][i]]["strength"],
                                                dict_weapons[dict_characters[choice]["weapons"][i]]["speed"])))
                                    print("_" * 40)  # Separador para mejorar la presentación
                                    
                                    # Pedimos al usuario que elija un arma
                                    opc = input("Introduce the id to add Weapon\n-ID to delete the weapon\n0) Go back\n->Option: ")

                                    # Si la opción es válida, se ejecuta el código correspondiente para añadir o eliminar armas
                                    if len(opc) >= 2:
                                        if opc[0] == "-":  # Si la opción empieza con un '-', significa que quiere eliminar un arma
                                            if opc[1].isdigit():
                                                if int(opc[1]) in dict_characters[choice]["weapons"]:  # Verificamos que el arma exista
                                                    dict_characters[choice]["speed"] -= dict_weapons[int(opc[1])]["speed"]  # Restamos la velocidad del arma eliminada
                                                    dict_characters[choice]["strength"] -= dict_weapons[int(opc[1])]["strength"]  # Restamos la fuerza del arma eliminada
                                                    dict_characters[choice]["weapons"].remove(int(opc[1]))  # Eliminamos el arma del personaje
                                        else:
                                            print("Incorrect Option".center(30, "="))  # Si la opción no es válida, mostramos un mensaje de error
                                    else:
                                        if not opc.isdigit():  # Verificamos que la opción sea un número
                                            input("Incorrect Option".center(30, "=") + "\nPress Enter to continue...")  # Mostramos un mensaje de error
                                        else:
                                            opc = int(opc)
                                            if opc == 0:  # Si la opción es 0, salimos del bucle
                                                editar_arma_personaje = False
                                            elif not int(opc) in auxiliar_armas:  # Verificamos que la opción sea válida
                                                print(auxiliar_armas)
                                                input("Incorrect Option".center(30, "=") + "\nPress Enter to continue...")  # Mostramos un mensaje de error
                                            else:
                                                dict_characters[choice]["speed"] += dict_weapons[opc]["speed"]  # Añadimos la velocidad del arma
                                                dict_characters[choice]["strength"] += dict_weapons[opc]["strength"]  # Añadimos la fuerza del arma
                                                dict_characters[choice]["weapons"].append(opc)  # Añadimos el arma al personaje
                                                print("Speed has increased from {} by {}".format(dict_characters[choice]["speed"], dict_weapons[opc]["speed"]))  # Mostramos un mensaje de éxito

                                # Si la opción es 3, volvemos al menú anterior
                            elif choise2 == 3:
                                flag3 = True  # Restauramos el flag para volver al menú principal
                                edit_character2 = False  # Salimos del bucle de edición de armas
                                edit_character = False  # Salimos del bucle de edición de personajes
                                flag31 = False  # Desactivamos la flag de edición de personajes

    # Bucle para la edición de armas
    while flag32:
        print(menu032)  # Imprime el menú de edición de armas
        auxiliar = []  # Lista auxiliar para almacenar la información de las armas
        for key_id, valor_info in dict_weapons.items():
            auxiliar.append([key_id, valor_info])  # Añadimos cada arma al auxiliar
        for i in range(len(auxiliar)):  # Recorremos la lista auxiliar
            auxiliar_id = auxiliar[i][0]  # ID del arma
            auxiliar_nombre = auxiliar[i][1]["name"]  # Nombre del arma
            auxiliar_speed = auxiliar[i][1]["speed"]  # Velocidad del arma
            auxiliar_strength = auxiliar[i][1]["strength"]  # Fuerza del arma
            auxiliar_hand = auxiliar[i][1]["two_hand"]  # Si el arma es de dos manos o no
            print("ID: "+str(auxiliar_id),"Name:"+auxiliar_nombre, 
                "speed: "+str(auxiliar_speed), "strength: "+str(auxiliar_strength), 
                "Two Hand: "+str(auxiliar_hand))  # Mostramos la información del arma
        
        edit_weapon = True  # Flag para iniciar la edición de un arma
        while edit_weapon:
            choice = input("Enter your choice: ")  # Pedimos al usuario que ingrese la ID del arma
            
            # Comprobamos que la opción ingresada sea un número
            if not choice.isdigit():
                print("Only numerical option")  # Si no es un número, mostramos un mensaje de error
                input("Retry: ")  # Pausa para que el usuario vea el mensaje de error

            else:
                choice = int(choice)  # Convertimos la opción a un número entero
                
                # Verificamos si la ID del arma es válida
                if not choice in dict_weapons.keys():
                    print("Not in range option")  # Si no existe, mostramos un mensaje de error
                    input("Retry: ")  # Pausa para que el usuario vea el mensaje de error
                else:
                    # Si la ID es válida, mostramos el arma seleccionada
                    print("Select feature to edit to weapon ID: {}, Name: {}".format(choice, dict_weapons[choice]["name"]))
                    edit_weapon2 = True  # Flag para entrar en el submenú de edición de características
                    while edit_weapon2:
                        print("\n1)Name \n2)Plus Strength \n3)Plus Speed \n4) Go Back")  # Opciones para editar el arma
                        choise2 = input("Seleccione una opcion: ")  # Pedimos al usuario que ingrese una opción
                        
                        # Comprobamos que la opción ingresada sea un número
                        if not choise2.isdigit():
                            print("Only numerical option")  # Si no es un número, mostramos un mensaje de error
                            input("Retry: ")  # Pausa para que el usuario vea el mensaje de error
                        else:
                            choise2 = int(choise2)  # Convertimos la opción a un número entero
                            
                            # Si la opción es 1, editamos el nombre del arma
                            if choise2 == 1:
                                new_name = input("Enter new name: ")  # Pedimos el nuevo nombre
                                seleccion = input("Do you want to save the changes (Y/N): ").upper()  # Preguntamos si desea guardar los cambios
                                if seleccion == "Y":
                                    dict_weapons[choice]["name"] = new_name  # Guardamos el nuevo nombre
                                    print("Select feature to edit to weapon ID: {}, Name: {}".format(choice, dict_weapons[choice]["name"]))
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_weapon2 = False  # Salimos del bucle de edición de características
                                    edit_weapon = False  # Salimos del bucle de edición de armas
                                    flag32 = False  # Desactivamos la flag de edición de armas
                                elif seleccion == "N":
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_weapon2 = False  # Salimos del bucle de edición de características
                                    edit_weapon = False  # Salimos del bucle de edición de armas
                                    flag32 = False  # Desactivamos la flag de edición de armas
                                else:
                                    print("Invalid Option")  # Si la opción no es válida, mostramos un mensaje de error

                            # Si la opción es 2, aumentamos la fuerza del arma
                            elif choise2 == 2:
                                plus_strength = input("Enter the new strength: ")  # Pedimos el aumento de fuerza
                                seleccion = input("Do you want to save the changes (Y/N): ").upper()  # Preguntamos si desea guardar los cambios
                                if seleccion == "Y":
                                    dict_weapons[choice]["strength"] = dict_weapons[choice]["strength"] + int(plus_strength)  # Sumamos la fuerza
                                    print("Select feature to edit to weapon ID: {}, Strength: {}".format(choice, dict_weapons[choice]["strength"]))
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_weapon2 = False  # Salimos del bucle de edición de características
                                    edit_weapon = False  # Salimos del bucle de edición de armas
                                    flag32 = False  # Desactivamos la flag de edición de armas
                                elif seleccion == "N":
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_weapon2 = False  # Salimos del bucle de edición de características
                                    edit_weapon = False  # Salimos del bucle de edición de armas
                                    flag32 = False  # Desactivamos la flag de edición de armas
                                else:
                                    print("Invalid Option only Y or N: ")  # Si la opción no es válida, mostramos un mensaje de error
                                    input("Enter to retry:")  # Pausa para que el usuario vea el mensaje de error
                            
                            # Si la opción es 3, aumentamos la velocidad del arma
                            elif choise2 == 3:
                                plus_speed = input("Enter the new speed: ")  # Pedimos el aumento de velocidad
                                seleccion = input("Do you want to save the changes (Y/N): ").upper()  # Preguntamos si desea guardar los cambios
                                if seleccion == "Y":
                                    dict_weapons[choice]["speed"] = dict_weapons[choice]["speed"] + int(plus_speed)  # Sumamos la velocidad
                                    print("Select feature to edit to weapon ID: {}, Speed: {}".format(choice, dict_weapons[choice]["speed"]))
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_weapon2 = False  # Salimos del bucle de edición de características
                                    edit_weapon = False  # Salimos del bucle de edición de armas
                                    flag32 = False  # Desactivamos la flag de edición de armas
                                elif seleccion == "N":
                                    flag3 = True  # Restauramos el flag para volver al menú principal
                                    edit_weapon2 = False  # Salimos del bucle de edición de características
                                    edit_weapon = False  # Salimos del bucle de edición de armas
                                    flag32 = False  # Desactivamos la flag de edición de armas
                                else:
                                    print("Invalid Option only Y or N: ")  # Si la opción no es válida, mostramos un mensaje de error
                                    input("Enter to retry:")  # Pausa para que el usuario vea el mensaje de error
                            
                            # Si la opción es 4, volvemos al menú anterior
                            elif choise2 == 4:
                                flag3 = True  # Restauramos el flag para volver al menú principal
                                edit_weapon2 = False  # Salimos del bucle de edición de características
                                edit_weapon = False  # Salimos del bucle de edición de armas
                                flag32 = False  # Desactivamos la flag de edición de armas

    # Bucle principal para la gestión de la opción "Listar"
    while flag4:
        print(menu04)  # Se muestra el menú de opciones (suponemos que `menu04` contiene las opciones de menú)
        choice = input("Enter your choice: ")  # Se recibe la entrada del usuario
                    
        # Verificación de que la opción sea un número
        if not choice.isdigit():
            print("Only numerical option")  # Si no es un número, muestra un mensaje de error
            input("Retry: ")  # Pide al usuario que intente de nuevo (pero no hace nada más)

        else:    
            choice = int(choice)  # Si la entrada es válida, la convierte en un número entero
                
            # Verifica que la opción esté en el rango válido
            if choice not in range(1, 6):
                print("Not in range option")  # Si la opción no está en el rango permitido, muestra mensaje de error
                input("Retry: ")  # Pide al usuario que intente de nuevo

            else:
                # Aquí se manejan las opciones seleccionadas por el usuario
                if choice == 1:  # Si elige la opción 1, se va a listar los personajes (por ID)
                    flag41 = True
                    flag4 = False  # Sale del bucle principal y entra al submenú de personajes

                elif choice == 2:  # Si elige la opción 2, se va a listar los personajes (por nombre)
                    flag42 = True
                    flag4 = False  # Sale del bucle principal y entra al submenú de armas

                elif choice == 3:  # Si elige la opción 3, es una opción en construcción
                    print("En Construccion")
                    input("Enter to continue: ")  # Muestra un mensaje de que está en construcción

                elif choice == 4:  # Si elige la opción 4, es otra opción en construcción
                    print("En Construccion")
                    input("Enter to continue: ")  # Muestra otro mensaje de que está en construcción

                elif choice == 5:  # Si elige la opción 5, vuelve al menú principal
                    flag4 = False
                    flag0 = True  # Se activa otro flag para ir al menú anterior

    # Bucle para gestionar el listado de personajes (ordenado por diferentes atributos)
    while flag41:
        print(menu041)  # Muestra el submenú de personajes (asumimos que `menu041` contiene las opciones de orden)
        choice = input("Enter your choice: ")  # Recibe la entrada del usuario
                    
        # Verifica que la opción ingresada sea un número
        if not choice.isdigit():
            print("Only numerical option")  # Si no es un número, muestra un mensaje de error
            input("Retry: ")  # Pide al usuario que intente de nuevo

        else:    
            auxiliar = []  # Se crea una lista auxiliar para ordenar los personajes
            for key_id, valor_info in dict_characters.items():  # Se itera sobre el diccionario de personajes
                auxiliar.append([key_id, valor_info])  # Se agrega cada personaje a la lista auxiliar
            
            choice = int(choice)  # Convierte la opción a un número entero
                
            # Verifica que la opción esté en el rango válido
            if choice not in range(1, 6):
                print("Not in range option")  # Si la opción no está en el rango permitido, muestra mensaje de error
                input("Retry: ")  # Pide al usuario que intente de nuevo
            else:
                # Aquí se gestionan las opciones de ordenamiento para los personajes
                if choice == 1:  # Si se elige ordenar por ID
                    print("Characters ordered by ID".center(70, "=") + "\n" + "ID" + "Name".rjust(15) + "Strength".rjust(15) + "Speed".rjust(15) + "Expirience".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por ID (orden ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][0] > auxiliar[i + 1][0]:  # Compara los ID y realiza un intercambio
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    
                    # Imprime los personajes ordenados por ID
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["experience"]).rjust(20))

                # Opción para ordenar por nombre
                if choice == 2:
                    print("Characters ordered by Name".center(70, "=") + "\n" + "ID".ljust(10) + "Name".ljust(20) + "Strength".rjust(10) + "Speed".rjust(10) + "Expirience".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por nombre (orden alfabético ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["name"] > auxiliar[i + 1][1]["name"]:  # Compara los nombres
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    
                    # Imprime los personajes ordenados por nombre
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["experience"]).rjust(20))

                # Opción para ordenar por fuerza
                if choice == 3:
                    print("Characters ordered by Strength".center(70, "=") + "\n" + "ID".ljust(10) + "Name".ljust(20) + "Strength".rjust(10) + "Speed".rjust(10) + "Expirience".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por fuerza (orden ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["strength"] > auxiliar[i + 1][1]["strength"]:  # Compara la fuerza
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    
                    # Imprime los personajes ordenados por fuerza
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["experience"]).rjust(20))

                # Opción para ordenar por velocidad
                if choice == 4:
                    print("Characters ordered by Speed".center(70, "=") + "\n" + "ID".ljust(10) + "Name".ljust(20) + "Strength".rjust(10) + "Speed".rjust(10) + "Expirience".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por velocidad (orden ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["speed"] > auxiliar[i + 1][1]["speed"]:  # Compara la velocidad
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux     
                        
                    # Imprime los personajes ordenados por velocidad
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["experience"]).rjust(20))

                # Opción para salir de la lista de personajes y volver al menú principal
                if choice == 5:
                    flag4 = True
                    flag41 = False  # Regresa al menú anterior

    # Bucle para gestionar el listado de armas, que sigue la misma estructura que los personajes
    while flag42:
        print(menu042)  # Muestra el submenú de armas
        choice = input("Enter your choice: ")  # Recibe la entrada del usuario
                    
        if not choice.isdigit():
            print("Only numerical option")  # Verifica que sea un número
            input("Retry: ")  # Pide al usuario que intente de nuevo

        else:    
            auxiliar = []  # Se crea una lista auxiliar para ordenar las armas
            for key_id, valor_info in dict_weapons.items():  # Se itera sobre el diccionario de armas
                auxiliar.append([key_id, valor_info])  # Se agrega cada arma a la lista auxiliar
            
            choice = int(choice)  # Convierte la opción a número entero
                
            # Verifica que la opción esté en el rango válido
            if choice not in range(1, 6):
                print("Not in range option")  # Si la opción no está en el rango permitido, muestra mensaje de error
                input("Retry: ")  # Pide al usuario que intente de nuevo
            else:
                # Aquí se gestionan las opciones de ordenamiento para las armas
                if choice == 1:  # Si se elige ordenar por ID
                    print("Weapons ordered by ID".center(70, "=") + "\n" + "ID" + "Name".rjust(15) + "Strength".rjust(15) + "Speed".rjust(15) + "Two Hands".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por ID (orden ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][0] > auxiliar[i + 1][0]:  # Compara los ID y realiza un intercambio
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                            
                    # Imprime las armas ordenadas por ID
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["two_hand"]).rjust(20))

                # Opción para ordenar por nombre
                if choice == 2:
                    print("Weapons ordered by Name".center(70, "=") + "\n" + "ID".ljust(10) + "Name".ljust(20) + "Strength".rjust(10) + "Speed".rjust(10) + "Two Hands".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por nombre (orden alfabético ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["name"] > auxiliar[i + 1][1]["name"]:  # Compara los nombres
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    
                    # Imprime las armas ordenadas por nombre
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["two_hand"]).rjust(20))

                # Opción para ordenar por fuerza
                if choice == 3:
                    print("Weapons ordered by Strength".center(70, "=") + "\n" + "ID".ljust(10) + "Name".ljust(20) + "Strength".rjust(10) + "Speed".rjust(10) + "Two Hands".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por fuerza (orden ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["strength"] > auxiliar[i + 1][1]["strength"]:  # Compara la fuerza
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    
                    # Imprime las armas ordenadas por fuerza
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["two_hand"]).rjust(20))

                # Opción para ordenar por velocidad
                if choice == 4:
                    print("Weapons ordered by Speed".center(70, "=") + "\n" + "ID".ljust(10) + "Name".ljust(20) + "Strength".rjust(10) + "Speed".rjust(10) + "Two Hands".rjust(20) + "\n" + ("="*70))

                    # Algoritmo de ordenación por velocidad (orden ascendente)
                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["speed"] > auxiliar[i + 1][1]["speed"]:  # Compara la velocidad
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                        
                    # Imprime las armas ordenadas por velocidad
                    for i in range(len(auxiliar)):
                        print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1]["name"].ljust(20) + str(auxiliar[i][1]["strength"]).rjust(10) + str(auxiliar[i][1]["speed"]).rjust(10) + str(auxiliar[i][1]["two_hand"]).rjust(20))
                
                # Opción para salir y volver al menú principal
                if choice == 5:
                    flag4 = True
                    flag42 = False  # Regresa al menú anterior
