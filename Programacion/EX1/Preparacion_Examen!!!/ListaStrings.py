# Cadena inicial que contiene los contactos, separados por "*"
agenda = "David:Perera Gonzalez;44444444K*605760064*Laura:Alonso Perez;12345678L*612345678*Carlos:Ramirez Diaz;87654321M*678123456"

# Menú principal del programa
menu = """
========================================
         GESTIÓN DE CONTACTOS
========================================
1) Añadir nuevo contacto
2) Mostrar contactos ordenados por DNI
3) Mostrar contactos ordenados por Nombre
4) Mostrar contactos ordenados por Apellido
5) Mostrar contactos ordenados por Teléfono
6) Salir
========================================
"""

# Banderas de control
salir = False

# Bucle principal del programa
while not salir:
    print(menu)  # Muestra el menú de opciones
    opcion = input("Elige una opción: ")  # Solicita una opción al usuario

    if opcion == "1":  # Opción para añadir un nuevo contacto
        # Pedimos al usuario que introduzca los datos del nuevo contacto
        nombre = input("Introduce el nombre: ")
        apellido = input("Introduce el apellido: ")
        dni = input("Introduce el DNI: ")
        telefono = input("Introduce el teléfono: ")

        # Añadimos el nuevo contacto a la cadena 'agenda'
        nuevo_contacto = "{}:{};{}*{}".format(nombre, apellido, dni, telefono)
        agenda += "*" + nuevo_contacto  # Agregamos el nuevo contacto a la cadena existente

    elif opcion == "2":  # Ordenar contactos por DNI
        # Procesamos los contactos de la cadena 'agenda'
        contactos = agenda.split('*')  # Los contactos están separados por "*"
        contactos_procesados = []

        # Procesamos los contactos para separarlos en partes (nombre, apellido, dni, teléfono)
        for i in range(0, len(contactos), 2):
            contacto_info = contactos[i:i+2]
            if len(contacto_info) == 2:
                nombre_apellido, telefono = contacto_info
                nombre, apellido_dni = nombre_apellido.split(':')
                apellido, dni = apellido_dni.split(';')
                contactos_procesados.append((nombre, apellido, dni, telefono))

        # Ordenamos los contactos por DNI (tercer elemento de cada tupla)
        contactos_ordenados = sorted(contactos_procesados, key=lambda x: x[2])

        # Mostramos los contactos ordenados por DNI
        print("\nContactos ordenados por DNI:")
        print("{:<10} {:<20} {:<10} {:<10}".format("Nombre", "Apellido", "DNI", "Teléfono"))
        for contacto in contactos_ordenados:
            print("{:<10} {:<20} {:<10} {:<10}".format(contacto[0], contacto[1], contacto[2], contacto[3]))
        print("\n")

    elif opcion == "3":  # Ordenar contactos por Nombre
        # Procesamos los contactos de la cadena 'agenda'
        contactos = agenda.split('*')
        contactos_procesados = []

        # Procesamos los contactos para separarlos en partes (nombre, apellido, dni, teléfono)
        for i in range(0, len(contactos), 2):
            contacto_info = contactos[i:i+2]
            if len(contacto_info) == 2:
                nombre_apellido, telefono = contacto_info
                nombre, apellido_dni = nombre_apellido.split(':')
                apellido, dni = apellido_dni.split(';')
                contactos_procesados.append((nombre, apellido, dni, telefono))

        # Ordenamos los contactos por Nombre (primer elemento de cada tupla)
        contactos_ordenados = sorted(contactos_procesados, key=lambda x: x[0])

        # Mostramos los contactos ordenados por Nombre
        print("\nContactos ordenados por Nombre:")
        print("{:<10} {:<20} {:<10} {:<10}".format("Nombre", "Apellido", "DNI", "Teléfono"))
        for contacto in contactos_ordenados:
            print("{:<10} {:<20} {:<10} {:<10}".format(contacto[0], contacto[1], contacto[2], contacto[3]))
        print("\n")

    elif opcion == "4":  # Ordenar contactos por Apellido
        # Procesamos los contactos de la cadena 'agenda'
        contactos = agenda.split('*')
        contactos_procesados = []

        # Procesamos los contactos para separarlos en partes (nombre, apellido, dni, teléfono)
        for i in range(0, len(contactos), 2):
            contacto_info = contactos[i:i+2]
            if len(contacto_info) == 2:
                nombre_apellido, telefono = contacto_info
                nombre, apellido_dni = nombre_apellido.split(':')
                apellido, dni = apellido_dni.split(';')
                contactos_procesados.append((nombre, apellido, dni, telefono))

        # Ordenamos los contactos por Apellido (segundo elemento de cada tupla)
        contactos_ordenados = sorted(contactos_procesados, key=lambda x: x[1])

        # Mostramos los contactos ordenados por Apellido
        print("\nContactos ordenados por Apellido:")
        print("{:<10} {:<20} {:<10} {:<10}".format("Nombre", "Apellido", "DNI", "Teléfono"))
        for contacto in contactos_ordenados:
            print("{:<10} {:<20} {:<10} {:<10}".format(contacto[0], contacto[1], contacto[2], contacto[3]))
        print("\n")

    elif opcion == "5":  # Ordenar contactos por Teléfono
        # Procesamos los contactos de la cadena 'agenda'
        contactos = agenda.split('*')
        contactos_procesados = []

        # Procesamos los contactos para separarlos en partes (nombre, apellido, dni, teléfono)
        for i in range(0, len(contactos), 2):
            contacto_info = contactos[i:i+2]
            if len(contacto_info) == 2:
                nombre_apellido, telefono = contacto_info
                nombre, apellido_dni = nombre_apellido.split(':')
                apellido, dni = apellido_dni.split(';')
                contactos_procesados.append((nombre, apellido, dni, telefono))

        # Ordenamos los contactos por Teléfono (cuarto elemento de cada tupla)
        contactos_ordenados = sorted(contactos_procesados, key=lambda x: x[3])

        # Mostramos los contactos ordenados por Teléfono
        print("\nContactos ordenados por Teléfono:")
        print("{:<10} {:<20} {:<10} {:<10}".format("Nombre", "Apellido", "DNI", "Teléfono"))
        for contacto in contactos_ordenados:
            print("{:<10} {:<20} {:<10} {:<10}".format(contacto[0], contacto[1], contacto[2], contacto[3]))
        print("\n")

    elif opcion == "6":  # Opción para salir del programa
        print("Saliendo del programa...")
        salir = True  # Cambiamos la bandera 'salir' a True para terminar el bucle
    else:
        print("Opción no válida. Inténtalo de nuevo.")
