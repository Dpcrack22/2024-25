# Inicializa una variable 'llista' que contiene la cabecera de la agenda formateada.
# 'center(30, "*")' centra el texto 'Agenda' y lo rodea con asteriscos para formar un título.
# 'ljust(15)' y 'rjust(15)' aseguran que los nombres y los teléfonos se alineen en columnas.
llista = "Agenda".center(30, "*") + "\n" + "Nombre".ljust(15) + "Telefono".rjust(15) + "\n" + "*"*30 + "\n"

# Menú principal del programa que ofrece tres opciones: Añadir un contacto, Mostrar la agenda o Salir.
menu = "1) Nuevo Contacto\n2) Mostrar Agenda\n3) Salir"

# Bucle que controla si el usuario ha decidido salir del programa o no. Inicialmente, 'salir' es False.
salir = FalsepythonProject1

# El programa se ejecuta hasta que el usuario decide salir (cuando 'salir' se pone en True).
while not salir:
    # Muestra el menú de opciones al usuario
    print(menu)
    # Solicita al usuario que seleccione una opción, que debe ser un número entero.
    opcion = int(input("Opcion: "))
    
    # Si el usuario elige la opción 1, se solicita agregar un nuevo contacto.
    if opcion == 1:
        # Se pide el nombre del nuevo contacto.
        Nombre = input("\n Introduce el Nombre del Contacto: ")
        # Se pide el teléfono del nuevo contacto.
        Telefono = input("\n Introduce el Telefono del Contacto: ")

        # Actualiza la variable 'llista' añadiendo el nuevo contacto al final.
        # 'format()' asegura que el nombre ocupe un ancho de 15 caracteres alineado a la izquierda
        # y el teléfono se alinee a la derecha con otros 15 caracteres.
        llista = llista + "{0:15}{1:15}\n".format(Nombre, Telefono.rjust(15))
        
        # Pausa el programa para que el usuario presione Enter antes de continuar.
        input("\nEnter para Continuar: ")

    # Si el usuario elige la opción 2, se muestra la agenda actual con todos los contactos.
    elif opcion == 2:
        # Muestra la lista completa de contactos con la cabecera.
        print("\n" + llista)
        # Pausa el programa para que el usuario presione Enter antes de continuar.
        input("\nEnter para Continuar: ")

    # Si el usuario elige la opción 3, se termina el programa poniendo 'salir' en True.
    elif opcion == 3:
        salir = True

    # Si el usuario introduce una opción que no está en el menú (no 1, 2 o 3), se muestra un mensaje de error.
    else:
        print("Opcion invalida (Marca un numero de las opciones)")
