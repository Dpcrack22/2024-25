# Datos iniciales
letrasDni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C',
             'K', 'E']
usuario1 = {"nombre": "Pedro Javier Morales", "direccion": "Flores 36 8º 2º", "tfn": ["+0034345345345"],
            "compras": [1234, 423, 23]}
usuario2 = {"nombre": "Maite Lopez Miravet", "direccion": "Balmes 31 1º 2º",
            "tfn": ["+0034234234235", "+0034239999235"], "compras": [12344]}
usuario3 = {"nombre": "Marta Garcia Suarez", "direccion": "Valencia 21 3º 1º", "tfn": ["+0075766576575"],
            "compras": [34, 423, 23, 6]}
usuarios = {"47474747X": usuario1, "24536425T": usuario2, "76767676H": usuario3}

# Menús y control
menu00 = "1) Create User\n2) Modify User\n3) Show Users\n4) Find Users\n5) List Users\n6) Exit"
menu01 = "\n1) Enter Dni\n2) Enter Name\n3) Enter Surname\n4) Enter Address\n5) Enter Tfn\n6) Save User\n7) Go Back"
menu02 = "\n" + "**************Menu 02 - Modify User***************" + "\n1) Add purchase\n2) Add tfn number\n3) Del tfn number\n4) Change address\n5) Go Back"
menu04 = "\n1) Find Users by DNI\n2) Find Users by Name\n3) Go back\nOption: "
menu05 = "1) List Users by DNI\n2) List Users by Name\n3) List Users by Address\n4) List Users by Total Purchase\n5) Go back"

salir = False

# Ciclo principal
while not salir:
    print(menu00)
    opcion = input("Seleccione una opción: ")

    # Opción 1: Crear Usuario
    if opcion == "1":
        nuevo_usuario = {"dni": "", "nombre": "", "apellido": "", "direccion": "", "tfn": []}

        creando_usuario = True
        while creando_usuario:
            # Mostrar el formulario de creación con los valores actuales
            print("\nDni:*           ", nuevo_usuario["dni"])
            print("Name:*          ", nuevo_usuario["nombre"])
            print("Surname:*       ", nuevo_usuario["apellido"])
            print("Address:*       ", nuevo_usuario["direccion"])
            print("tfn:            ", ", ".join(nuevo_usuario["tfn"]) if nuevo_usuario["tfn"] else "No phones added")

            # Mostrar el menú de opciones
            print(menu01)
            sub_opcion = input("Option: ")

            if sub_opcion == "1":  # Ingresar DNI
                dni = input("Enter DNI: ")
                if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
                    numero = int(dni[:-1])
                    letra_correcta = letrasDni[numero % 23]
                    if dni[-1].upper() == letra_correcta:
                        nuevo_usuario["dni"] = dni
                    else:
                        print("DNI inválido: letra incorrecta.")
                else:
                    print("DNI inválido: debe tener 8 dígitos y una letra.")

            elif sub_opcion == "2":  # Ingresar Nombre
                nuevo_usuario["nombre"] = input("Enter Name: ")

            elif sub_opcion == "3":  # Ingresar Apellido
                nuevo_usuario["apellido"] = input("Enter Surname: ")

            elif sub_opcion == "4":  # Ingresar Dirección
                nuevo_usuario["direccion"] = input("Enter Address: ")

            elif sub_opcion == "5":  # Ingresar Teléfono
                telefono = input("Enter Tfn (Formato: +0034 xxxxxxxxx): ")
                if telefono.startswith("+0034") and len(telefono) == 14 and telefono[5:].isdigit():
                    nuevo_usuario["tfn"].append(telefono)
                else:
                    print("Número de teléfono inválido. Debe tener el formato +0034 seguido de 9 dígitos.")

            elif sub_opcion == "6":  # Guardar Usuario
                if nuevo_usuario["dni"] in usuarios:
                    print("Error: Este DNI ya está registrado.")
                elif all(nuevo_usuario.values()):  # Verificar que todos los campos requeridos estén completos
                    # Crear el usuario completo uniendo nombre y apellido
                    usuarios[nuevo_usuario["dni"]] = {
                        "nombre": f"{nuevo_usuario['nombre']} {nuevo_usuario['apellido']}",
                        "direccion": nuevo_usuario["direccion"],
                        "tfn": nuevo_usuario["tfn"],
                        "compras": []
                    }
                    print(f"Usuario {nuevo_usuario['nombre']} {nuevo_usuario['apellido']} creado con éxito.\n")
                    creando_usuario = False
                else:
                    print("Error: Debe completar todos los campos obligatorios (*) antes de guardar.\n")

            elif sub_opcion == "7":  # Volver sin guardar
                creando_usuario = False

            else:
                print("Opción inválida. Intente de nuevo.\n")

    # Opción 2: Modificar Usuario
    if opcion == "2":
        dni = input("Enter DNI of user to modify: ")

        if dni in usuarios:
            modificando_usuario = True
            usuario_actual = usuarios[dni]

            while modificando_usuario:
                print(menu02)
                opcion_modificar = input("Option: ")

                # Sub-opción 1: Añadir compra
                if opcion_modificar == "1":
                    compra = input("Enter purchase amount: ")
                    if compra.isdigit():
                        usuario_actual["compras"].append(int(compra))
                        print("Purchase added.")
                    else:
                        print("Invalid amount. Please enter a valid number.")

                # Sub-opción 2: Añadir número de teléfono
                elif opcion_modificar == "2":
                    nuevo_tfn = input("Enter new phone number (+0034 XXXXXXXXX): ")
                    if nuevo_tfn.startswith("+0034") and len(nuevo_tfn) == 13 and nuevo_tfn[5:].isdigit():
                        usuario_actual["tfn"].append(nuevo_tfn)
                        print("Phone number added.")
                    else:
                        print("Invalid phone number format. Please use +0034 followed by 9 digits.")

                # Sub-opción 3: Eliminar número de teléfono
                elif opcion_modificar == "3":
                    print("Current phone numbers:", usuario_actual["tfn"])
                    del_tfn = input("Enter phone number to delete: ")
                    if del_tfn in usuario_actual["tfn"]:
                        usuario_actual["tfn"].remove(del_tfn)
                        print("Phone number removed.")
                    else:
                        print("Phone number not found in user data.")

                # Sub-opción 4: Cambiar dirección
                elif opcion_modificar == "4":
                    nueva_direccion = input("Enter new address: ")
                    usuario_actual["direccion"] = nueva_direccion
                    print("Address updated.")

                # Sub-opción 5: Volver
                elif opcion_modificar == "5":
                    modificando_usuario = False

                else:
                    print("Invalid option. Please try again.\n")

        else:
            print("No user found with the specified DNI.\n")

    # Opción 3: Mostrar Usuarios
    if opcion == "3":
        if opcion == "3":
            for dni, usuario_actual in usuarios.items():
                # Formatear y mostrar la información del usuario
                print("\nDNI:         ", dni)
                print("Nombre:      ", usuario_actual["nombre"])
                print("TFN:         ", ", ".join(usuario_actual["tfn"]))

                input("\nPress Enter to see next user")
        else:
            print("User not found with the specified DNI.\n")

    #Opcion 4: Buscar Usuario
    if opcion == "4":
        buscando_usuario = True
        while buscando_usuario:
            print(menu04)
            opcion_busqueda = input("Option: ")

            # Sub-opción 1: Buscar por DNI
            if opcion_busqueda == "1":
                dni = input("Enter DNI to search: ")
                if dni in usuarios:
                    usuario_actual = usuarios[dni]
                    print("\nUser found:")
                    print("DNI:         ", dni)
                    print("Nombre:      ", usuario_actual["nombre"])
                    print("TFN:         ", ", ".join(usuario_actual["tfn"]))
                else:
                    print("No user found with the specified DNI.")
                input("\nPress Enter to continue")

            # Sub-opción 2: Buscar por Nombre
            elif opcion_busqueda == "2":
                nombre = input("Enter Name to search: ").lower()
                encontrado = False
                for dni, usuario_actual in usuarios.items():
                    if nombre in usuario_actual["nombre"].lower():
                        print("\nUser found:")
                        print("DNI:         ", dni)
                        print("Nombre:      ", usuario_actual["nombre"])
                        print("TFN:         ", ", ".join(usuario_actual["tfn"]))
                        encontrado = True
                if not encontrado:
                    print("No user found with the specified name.")
                input("\nPress Enter to continue")

            # Sub-opción 3: Volver
            elif opcion_busqueda == "3":
                buscando_usuario = False

            else:
                print("Invalid option. Please try again.\n")

    # Opción 5: Listar Usuarios
    elif opcion == "5":
        print(menu05)
        sub_opcion = input("Seleccione una opción de listado: ")

        # Listar por DNI (usando método burbuja)
        if sub_opcion == "1":
            lista_dni = list(usuarios.keys())
            for i in range(len(lista_dni) - 1):
                for j in range(len(lista_dni) - i - 1):
                    if lista_dni[j] > lista_dni[j + 1]:
                        lista_dni[j], lista_dni[j + 1] = lista_dni[j + 1], lista_dni[j]
            print("Usuarios ordenados por DNI:")
            for dni in lista_dni:
                print(dni, usuarios[dni]["nombre"])

        # Listar por Nombre (usando método burbuja)
        elif sub_opcion == "2":
            lista_usuarios = list(usuarios.items())
            for i in range(len(lista_usuarios) - 1):
                for j in range(len(lista_usuarios) - i - 1):
                    if lista_usuarios[j][1]["nombre"] > lista_usuarios[j + 1][1]["nombre"]:
                        lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]
            print("Usuarios ordenados por Nombre:")
            for dni, datos in lista_usuarios:
                print(datos["nombre"], "-", dni)

        # Listar por total de compras (usando método burbuja)
        elif sub_opcion == "4":
            lista_usuarios = list(usuarios.items())
            for i in range(len(lista_usuarios) - 1):
                for j in range(len(lista_usuarios) - i - 1):
                    total_compras_j = sum(lista_usuarios[j][1]["compras"])
                    total_compras_next = sum(lista_usuarios[j + 1][1]["compras"])
                    if total_compras_j < total_compras_next:
                        lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]
            print("Usuarios ordenados por Total de Compras:")
            for dni, datos in lista_usuarios:
                print(datos["nombre"], "-", f"Total Compras: {sum(datos['compras'])}")

    # Opción 6: Salir
    elif opcion == "6":
        salir = True
        print("Saliendo del programa...")

    else:
        print("Opción inválida. Intente de nuevo.\n")
