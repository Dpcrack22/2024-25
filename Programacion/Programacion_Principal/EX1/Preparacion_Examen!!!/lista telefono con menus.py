# Cadena inicial que contiene la agenda con contactos separados por ';'
agenda = "Garcia Gutierrez-Laia:666666666;Ruiz Almansa-Esther:656343536;Casado Ruiz-Manolo:674343536;Lopez Manrique-Esteban:655676869;"

# Diccionario donde se almacenarán los contactos
agenda_dict = {}

# Convertir la cadena en un diccionario
for contacto in agenda.split(';'):  # Divide la cadena por cada ';'
    if contacto:  # Evita el último elemento vacío después del último ';'
        nombre_completo, telefono = contacto.split(':')  # Separa el nombre completo del teléfono
        apellido, nombre = nombre_completo.split('-')  # Separa el apellido del nombre
        agenda_dict[(nombre, apellido)] = telefono  # Añade al diccionario, con clave (nombre, apellido)

# Menús que se muestran al usuario en diferentes momentos
menu00 = "The Best Agenda In The World".center(50, "=") + "\n" + "Menu00".center(50, "=") + "\n" + "1) New Contact\n2) Show Contacts\n3) Find Contact\n4) Exit\n"
menu02 = "The Best Agenda In The World".center(50, "=") + "\n" + "Menu01".center(50, "=") + "\n" + "1) Show By Name\n2) Show By Surname\n3) Show By Phone Number\n4) Go Back\n"
menu03 = "The Best Agenda In The World".center(50, "=") + "\n" + "Menu02".center(50, "=") + "\n" + "1) Find By Name\n2) Find By Surname\n3) Find By Phone Number\n4) Go Back\n"

# Banderas de control para manejar los menús
flg_00 = True  # Control del menú principal
flg_01 = False  # No se utiliza, puede ser eliminado
flg_02 = False  # Control del menú de mostrar contactos
flg_03 = False  # Control del menú de búsqueda
salir = False  # Variable que controla si el programa debe terminar

# Bucle principal del programa
while not salir:
    while flg_00:  # Menú principal
        print(menu00)
        opc = input("\nOption:\n")  # Solicita una opción al usuario
        if not opc.isdigit():
            print("No numeric option, try again")  # Verifica que la opción sea un número
            input("Enter to continue")
        elif int(opc) not in range(1, 5):  # Verifica que la opción esté dentro del rango válido
            print("Option out of range, try again")
            input("Enter to continue")
        else:
            opc = int(opc)

        if opc == 4:
            salir = True  # Finaliza el programa si elige "Exit"
            break
        if opc == 3:
            flg_03 = True  # Activa la búsqueda de contactos
            flg_00 = False  # Desactiva el menú principal
        if opc == 2:
            flg_02 = True  # Activa la opción de mostrar contactos
            flg_00 = False
        if opc == 1:
            # Opción de agregar un nuevo contacto
            nombre = input("Enter the name:\n")
            apellido = input("Enter the surname:\n")
            telefono = input("Enter the phone number:\n")
            nombre_completo = (nombre, apellido)
            
            if nombre_completo in agenda_dict:  # Verifica si el contacto ya existe
                print("Contact already exists!")
            else:
                agenda_dict[nombre_completo] = telefono  # Añade el contacto al diccionario
                print("Contact added successfully!")
            input("Enter to continue")

    while flg_02:  # Menú para mostrar contactos
        print(menu02)
        opc = input("\nOption:\n")
        if not opc.isdigit():  # Verifica que la opción sea numérica
            print("No numeric option, try again")
            input("Enter to continue")
        elif int(opc) not in range(1, 5):
            print("Option out of range, try again")
            input("Enter to continue")
        else:
            opc = int(opc)

        if opc == 4:
            flg_02 = False  # Regresa al menú principal
            flg_00 = True

        # Mostrar contactos ordenados
        contactos_ordenados = []  # Lista donde se guardarán los contactos ordenados
        if opc == 1:
            # Opción de ordenar por nombre
            contactos_ordenados = sorted(agenda_dict.items(), key=lambda x: x[0][0])  # Ordena por el primer valor de la tupla (nombre)
        elif opc == 2:
            # Opción de ordenar por apellido
            contactos_ordenados = sorted(agenda_dict.items(), key=lambda x: x[0][1])  # Ordena por el segundo valor de la tupla (apellido)
        elif opc == 3:
            # Opción de ordenar por teléfono
            contactos_ordenados = sorted(agenda_dict.items(), key=lambda x: x[1])  # Ordena por teléfono

        # Muestra los contactos ordenados
        for (nombre, apellido), telefono in contactos_ordenados:
            print(f"{nombre} {apellido}: {telefono}")  # Imprime cada contacto formateado
        input("Enter to continue")

    while flg_03:  # Menú de búsqueda de contactos
        print(menu03)
        opc = input("\nOption:\n")
        if not opc.isdigit():  # Verifica que la opción sea numérica
            print("No numeric option, try again")
            input("Enter to continue")
        elif int(opc) not in range(1, 5):
            print("Option out of range, try again")
            input("Enter to continue")
        else:
            opc = int(opc)

        if opc == 4:
            flg_03 = False  # Regresa al menú principal
            flg_00 = True

        # Solicita el término de búsqueda al usuario
        busqueda = input("Enter your search term:\n").lower()
        encontrados = []  # Lista donde se guardarán los contactos encontrados

        # Búsqueda por nombre, apellido o teléfono
        for (nombre, apellido), telefono in agenda_dict.items():
            if opc == 1:
                # Buscar por nombre
                if nombre.lower().find(busqueda) != -1:
                    encontrados.append(f"{nombre} {apellido}: {telefono}")
            elif opc == 2:
                # Buscar por apellido
                if apellido.lower().find(busqueda) != -1:
                    encontrados.append(f"{nombre} {apellido}: {telefono}")
            elif opc == 3:
                # Buscar por teléfono
                if telefono.find(busqueda) != -1:
                    encontrados.append(f"{nombre} {apellido}: {telefono}")

        # Mostrar los contactos encontrados
        if encontrados:
            print("\n".join(encontrados))  # Imprime todos los contactos encontrados
        else:
            print("No contacts found.")  # Mensaje si no se encuentran contactos
        input("Enter to continue")
