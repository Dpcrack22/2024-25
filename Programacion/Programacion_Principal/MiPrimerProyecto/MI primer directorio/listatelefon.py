# Cadena inicial de la agenda
agenda = "Garcia Gutierrez-Laia:666666666;Ruiz Almansa-Esther:656343536;Casado Ruiz-Manolo:674343536;Lopez Manrique-Esteban:655676869;"
agenda_dict = {}

# Convertir la cadena en un diccionario
for contacto in agenda.split(';'):
    if contacto:  # Evitar última cadena vacía
        nombre_completo, telefono = contacto.split(':')
        apellido, nombre = nombre_completo.split('-')
        agenda_dict[(nombre, apellido)] = telefono

menu00 = "The Best Agenda In The World".center(50, "=")+"\n"+"Menu00".center(50, "=")+"\n"+"1) New Contact\n2) Show Contacts\n3) Find Contact\n4) Exit\n"
menu02 = "The Best Agenda In The World".center(50, "=")+"\n"+"Menu01".center(50, "=")+"\n"+"1) Show By Name\n2) Show By Surname\n3) Show By Phone Number\n4) Go Back\n"
menu03 = "The Best Agenda In The World".center(50, "=")+"\n"+"Menu02".center(50, "=")+"\n"+"1) Find By Name\n2) Find By Surname\n3) Find By Phone Number\n4) Go Back\n"

flg_00 = True
flg_01 = False
flg_02 = False
flg_03 = False
salir = False

while not salir:
    while flg_00:
        print(menu00)
        opc = input("\nOption:\n")
        if not opc.isdigit():
            print("No numeric option, try again")
            input("Enter to continue")
        elif int(opc) not in range(1, 5):
            print("Option out of range, try again")
            input("Enter to continue")
        else:
            opc = int(opc)

        if opc == 4:
            salir = True
            break
        if opc == 3:
            flg_03 = True
            flg_00 = False
        if opc == 2:
            flg_02 = True
            flg_00 = False
        if opc == 1:
            # Agregar nuevo contacto
            nombre = input("Enter the name:\n")
            apellido = input("Enter the surname:\n")
            telefono = input("Enter the phone number:\n")
            nombre_completo = (nombre, apellido)
            
            if nombre_completo in agenda_dict:
                print("Contact already exists!")
            else:
                agenda_dict[nombre_completo] = telefono
                print("Contact added successfully!")
            input("Enter to continue")

    while flg_02:
        print(menu02)
        opc = input("\nOption:\n")
        if not opc.isdigit():
            print("No numeric option, try again")
            input("Enter to continue")
        elif int(opc) not in range(1, 5):
            print("Option out of range, try again")
            input("Enter to continue")
        else:
            opc = int(opc)

        if opc == 4:
            flg_02 = False
            flg_00 = True

        # Mostrar contactos ordenados
        contactos_ordenados = []
        if opc == 1:
            # Ordenar por nombre
            contactos_ordenados = sorted(agenda_dict.items(), key=lambda x: x[0][0])
        elif opc == 2:
            # Ordenar por apellido
            contactos_ordenados = sorted(agenda_dict.items(), key=lambda x: x[0][1])
        elif opc == 3:
            # Ordenar por teléfono
            contactos_ordenados = sorted(agenda_dict.items(), key=lambda x: x[1])

        # Mostrar la agenda
        for (nombre, apellido), telefono in contactos_ordenados:
            print(f"{nombre} {apellido}: {telefono}")
        input("Enter to continue")

    while flg_03:
        print(menu03)
        opc = input("\nOption:\n")
        if not opc.isdigit():
            print("No numeric option, try again")
            input("Enter to continue")
        elif int(opc) not in range(1, 5):
            print("Option out of range, try again")
            input("Enter to continue")
        else:
            opc = int(opc)

        if opc == 4:
            flg_03 = False
            flg_00 = True

        # Búsqueda por nombre, apellido o teléfono usando .find()
        busqueda = input("Enter your search term:\n").lower()
        encontrados = []

        for (nombre, apellido), telefono in agenda_dict.items():
            if opc == 1:
                # Buscar por nombre usando .find()
                if nombre.lower().find(busqueda) != -1:
                    encontrados.append(f"{nombre} {apellido}: {telefono}")
            elif opc == 2:
                # Buscar por apellido usando .find()
                if apellido.lower().find(busqueda) != -1:
                    encontrados.append(f"{nombre} {apellido}: {telefono}")
            elif opc == 3:
                # Buscar por teléfono usando .find()
                if telefono.find(busqueda) != -1:
                    encontrados.append(f"{nombre} {apellido}: {telefono}")

        # Mostrar resultados de búsqueda
        if encontrados:
            print("\n".join(encontrados))
        else:
            print("No contacts found.")
        input("Enter to continue")
