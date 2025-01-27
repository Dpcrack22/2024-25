# Cadena de texto con contactos en el formato especificado, todo en una sola línea
agenda = "Pedro:Morales Fernandez-47474747R_+0034345345345*12;Maite:Lopez Miravet-24536425T_+0034234234235*15;" \
         "Marta:Garcia Suarez-76767676H_+0075766576575*21;Aitana:Sanchez Castillejos-84848484I_+0088823303445*16;" \
         "Sergio:Alarcon Navas-12345623I_+0066688221122*12;"

# Imprimir la cabecera de la tabla con alineación
print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
print("=" * 100)  # Línea divisoria para mejorar la presentación

# Separar los contactos en una lista utilizando el delimitador ';'
contactos = agenda.split(';')  # Divide la cadena por el delimitador ';'

# Procesar y mostrar cada contacto en la tabla
for registro in contactos:
    if registro:  # Comprobar que el registro no esté vacío
        # Separar el nombre del resto del registro usando ':'
        partes = registro.split(':')  # Obtener partes del registro
        if len(partes) < 2:  # Verificar que se haya separado correctamente
            print(f"Registro no válido: {registro}")  # Mensaje de error si el formato es incorrecto
            continue  # Saltar a la siguiente iteración

        nombre = partes[0]  # Primer parte es el nombre
        apellido_datos = partes[1]  # Segunda parte es el resto de la información

        # Comprobar que el formato del apellido_datos sea correcto
        if '-' not in apellido_datos:
            print(f"Registro no válido: {registro}")  # Mensaje de error
            continue  # Saltar a la siguiente iteración

        # Obtener los apellidos y el resto utilizando '-'
        apellidos, dni_telefono = apellido_datos.split('-')  # Obtener "Apellidos_DNI_Teléfono*Puntos"
        # Separar el DNI y el teléfono utilizando '_'
        dni, telefono_puntos = dni_telefono.split('_')  # Separar DNI de "Teléfono*Puntos"
        # Separar el teléfono y los puntos utilizando '*'
        telefono, puntos = telefono_puntos.split('*')  # Separar teléfono de puntos
        # Imprimir la fila de datos en formato alineado
        print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))

# Bandera de control para salir
salir = False

# Bucle principal del menú
while not salir:
    print("\n========================================")
    print("         GESTIÓN DE CONTACTOS")
    print("========================================")
    print("1) Añadir nuevo contacto")  # Opción para añadir nuevo contacto
    print("2) Ordenar por Nombre")  # Opción para ordenar por Nombre
    print("3) Ordenar por Apellido")  # Opción para ordenar por Apellido
    print("4) Ordenar por DNI")  # Opción para ordenar por DNI
    print("5) Ordenar por Teléfono")  # Opción para ordenar por Teléfono
    print("6) Ordenar por Puntos")  # Opción para ordenar por Puntos
    print("7) Buscar")  # Opción para buscar contactos
    print("8) Salir")  # Opción para salir
    print("========================================")

    opcion = input("Elige una opción: ")  # Solicita una opción al usuario

    # Validar si la entrada es numérica
    if not opcion.isdigit():
        print("Opción no válida. Solo se permiten números.")
        input("Presiona Enter para continuar...")
        continue  # Vuelve a mostrar el menú

    # Convertir la opción a entero
    opcion = int(opcion)

    # Validar si la opción está en el rango permitido
    if opcion < 1 or opcion > 8:
        print("Opción fuera de rango. Introduce un número del 1 al 8.")
        input("Presiona Enter para continuar...")
        continue  # Vuelve a mostrar el menú

    # Aquí puedes añadir el código correspondiente para cada opción
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        dni = input("Introduce el DNI: ")
        telefono = input("Introduce el teléfono: ")
        puntos = input("Introduce los puntos: ")
        nuevo_contacto = f"{nombre}:{apellidos}-{dni}_{telefono}*{puntos}"
        agenda += nuevo_contacto + ";"
        input("Presiona Enter para continuar...")

        """
        sorted
        La función sorted() se utiliza para ordenar una lista. Puede tomar una lista de cualquier tipo de elementos y ordenarlos según un criterio específico. Devuelve una nueva lista ordenada, sin modificar la lista original.

        contactos
        contactos es la lista que contiene los datos de todos los contactos. Se ha creado dividiendo la cadena de agenda por el delimitador ;.

        key=lambda x: x.split(':')[0]
        Aquí es donde especificamos el criterio de ordenación. La clave (key) que estamos usando es una función lambda. Una lambda es una función pequeña y anónima que se puede definir rápidamente. En este caso, lambda x: x.split(':')[0] hace lo siguiente:

        x representa cada elemento individual de la lista contactos.

        x.split(':') divide ese elemento en una lista de partes utilizando : como delimitador.

        x.split(':')[0] selecciona la primera parte (el nombre) del contacto.

        Resumen
        Así que sorted(contactos, key=lambda x: x.split(':')[0]):

        Toma la lista contactos.

        Utiliza la función lambda para especificar que los contactos deben ser ordenados por el nombre (que es la primera parte de cada contacto).

        Devuelve una nueva lista contactos_ordenados, donde los contactos están ordenados alfabéticamente por nombre.
        """
    elif opcion == 2:
        contactos = agenda.split(';')  # Divide la cadena por el delimitador ';'
        contactos_ordenados = sorted(contactos, key=lambda x: x.split(':')[0])  # Ordenar contactos por nombre

        # Imprimir la cabecera de la tabla con alineación
        print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
        print("=" * 100)  # Línea divisoria para mejorar la presentación

        # Procesar y mostrar cada contacto en la tabla
        for registro in contactos_ordenados:
            if registro:  # Comprobar que el registro no esté vacío
                # Separar el nombre del resto del registro usando ':'
                partes = registro.split(':')  # Obtener partes del registro
                if len(partes) < 2:  # Verificar que se haya separado correctamente
                    print(f"Registro no válido: {registro}")  # Mensaje de error si el formato es incorrecto
                    continue  # Saltar a la siguiente iteración

                nombre = partes[0]  # Primer parte es el nombre
                apellido_datos = partes[1]  # Segunda parte es el resto de la información

                # Comprobar que el formato del apellido_datos sea correcto
                if '-' not in apellido_datos:
                    print(f"Registro no válido: {registro}")  # Mensaje de error
                    continue  # Saltar a la siguiente iteración

                # Obtener los apellidos y el resto utilizando '-'
                apellidos, dni_telefono = apellido_datos.split('-')  # Obtener "Apellidos_DNI_Teléfono*Puntos"
                # Separar el DNI y el teléfono utilizando '_'
                dni, telefono_puntos = dni_telefono.split('_')  # Separar DNI de "Teléfono*Puntos"
                # Separar el teléfono y los puntos utilizando '*'
                telefono, puntos = telefono_puntos.split('*')  # Separar teléfono de puntos
                # Imprimir la fila de datos en formato alineado
                print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))
        input("Presiona Enter para continuar...")


    elif opcion == 3:
        contactos = agenda.split(';')  # Divide la cadena por el delimitador ';'
        contactos_ordenados = sorted(contactos, key=lambda x: x.split(':')[1].split('-')[0] if len(x.split(':')) > 1 and '-' in x else '')  # Ordenar contactos por apellido

        # Imprimir la cabecera de la tabla con alineación
        print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
        print("=" * 100)  # Línea divisoria para mejorar la presentación

        # Procesar y mostrar cada contacto en la tabla
        for registro in contactos_ordenados:
            if registro:  # Comprobar que el registro no esté vacío
                # Separar el nombre del resto del registro usando ':'
                partes = registro.split(':')  # Obtener partes del registro
                if len(partes) < 2:  # Verificar que se haya separado correctamente
                    print(f"Registro no válido: {registro}")  # Mensaje de error si el formato es incorrecto
                    continue  # Saltar a la siguiente iteración

                nombre = partes[0]  # Primer parte es el nombre
                apellido_datos = partes[1]  # Segunda parte es el resto de la información

                # Comprobar que el formato del apellido_datos sea correcto
                if '-' not in apellido_datos:
                    print(f"Registro no válido: {registro}")  # Mensaje de error
                    continue  # Saltar a la siguiente iteración

                # Obtener los apellidos y el resto utilizando '-'
                apellidos, dni_telefono = apellido_datos.split('-')  # Obtener "Apellidos_DNI_Teléfono*Puntos"
                # Separar el DNI y el teléfono utilizando '_'
                dni, telefono_puntos = dni_telefono.split('_')  # Separar DNI de "Teléfono*Puntos"
                # Separar el teléfono y los puntos utilizando '*'
                telefono, puntos = telefono_puntos.split('*')  # Separar teléfono de puntos
                # Imprimir la fila de datos en formato alineado
                print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))

        input("Presiona Enter para continuar...")

    elif opcion == 4:
        contactos = agenda.split(';')  # Divide la cadena por el delimitador ';'
        contactos_ordenados = sorted(contactos, key=lambda x: x.split('-')[1].split('_')[0] if '-' in x else '')  # Ordenar contactos por DNI

        # Imprimir la cabecera de la tabla con alineación
        print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
        print("=" * 100)  # Línea divisoria para mejorar la presentación

        # Procesar y mostrar cada contacto en la tabla
        for registro in contactos_ordenados:
            if registro:  # Comprobar que el registro no esté vacío
                # Separar el nombre del resto del registro usando ':'
                partes = registro.split(':')  # Obtener partes del registro
                if len(partes) < 2:  # Verificar que se haya separado correctamente
                    print(f"Registro no válido: {registro}")  # Mensaje de error si el formato es incorrecto
                    continue  # Saltar a la siguiente iteración

                nombre = partes[0]  # Primer parte es el nombre
                apellido_datos = partes[1]  # Segunda parte es el resto de la información

                # Comprobar que el formato del apellido_datos sea correcto
                if '-' not in apellido_datos:
                    print(f"Registro no válido: {registro}")  # Mensaje de error
                    continue  # Saltar a la siguiente iteración

                # Obtener los apellidos y el resto utilizando '-'
                apellidos, dni_telefono = apellido_datos.split('-')  # Obtener "Apellidos_DNI_Teléfono*Puntos"
                # Separar el DNI y el teléfono utilizando '_'
                dni, telefono_puntos = dni_telefono.split('_')  # Separar DNI de "Teléfono*Puntos"
                # Separar el teléfono y los puntos utilizando '*'
                telefono, puntos = telefono_puntos.split('*')  # Separar teléfono de puntos
                # Imprimir la fila de datos en formato alineado
                print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))

        input("Presiona Enter para continuar...")
    elif opcion == 5:
        contactos = agenda.split(';')  # Divide la cadena por el delimitador ';'
        contactos_ordenados = sorted(contactos, key=lambda x: x.split('_')[1].split('*')[0] if '_' in x else '')  # Ordenar contactos por teléfono

        # Imprimir la cabecera de la tabla con alineación
        print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
        print("=" * 100)  # Línea divisoria para mejorar la presentación

        # Procesar y mostrar cada contacto en la tabla
        for registro in contactos_ordenados:
            if registro:  # Comprobar que el registro no esté vacío
                # Separar el nombre del resto del registro usando ':'
                partes = registro.split(':')  # Obtener partes del registro
                if len(partes) < 2:  # Verificar que se haya separado correctamente
                    print(f"Registro no válido: {registro}")  # Mensaje de error si el formato es incorrecto
                    continue  # Saltar a la siguiente iteración

                nombre = partes[0]  # Primer parte es el nombre
                apellido_datos = partes[1]  # Segunda parte es el resto de la información

                # Comprobar que el formato del apellido_datos sea correcto
                if '-' not in apellido_datos:
                    print(f"Registro no válido: {registro}")  # Mensaje de error
                    continue  # Saltar a la siguiente iteración

                # Obtener los apellidos y el resto utilizando '-'
                apellidos, dni_telefono = apellido_datos.split('-')  # Obtener "Apellidos_DNI_Teléfono*Puntos"
                # Separar el DNI y el teléfono utilizando '_'
                dni, telefono_puntos = dni_telefono.split('_')  # Separar DNI de "Teléfono*Puntos"
                # Separar el teléfono y los puntos utilizando '*'
                telefono, puntos = telefono_puntos.split('*')  # Separar teléfono de puntos
                # Imprimir la fila de datos en formato alineado
                print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))

        input("Presiona Enter para continuar...")


    elif opcion == 6:
        contactos = agenda.split(';')  # Divide la cadena por el delimitador ';'
        contactos_ordenados = sorted(contactos, key=lambda x: x.split('*')[1] if '*' in x else '')  # Ordenar contactos por puntos

        # Imprimir la cabecera de la tabla con alineación
        print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
        print("=" * 100)  # Línea divisoria para mejorar la presentación

        # Procesar y mostrar cada contacto en la tabla
        for registro in contactos_ordenados:
            if registro:  # Comprobar que el registro no esté vacío
                # Separar el nombre del resto del registro usando ':'
                partes = registro.split(':')  # Obtener partes del registro
                if len(partes) < 2:  # Verificar que se haya separado correctamente
                    print(f"Registro no válido: {registro}")  # Mensaje de error si el formato es incorrecto
                    continue  # Saltar a la siguiente iteración

                nombre = partes[0]  # Primer parte es el nombre
                apellido_datos = partes[1]  # Segunda parte es el resto de la información

                # Comprobar que el formato del apellido_datos sea correcto
                if '-' not in apellido_datos:
                    print(f"Registro no válido: {registro}")  # Mensaje de error
                    continue  # Saltar a la siguiente iteración

                # Obtener los apellidos y el resto utilizando '-'
                apellidos, dni_telefono = apellido_datos.split('-')  # Obtener "Apellidos_DNI_Teléfono*Puntos"
                # Separar el DNI y el teléfono utilizando '_'
                dni, telefono_puntos = dni_telefono.split('_')  # Separar DNI de "Teléfono*Puntos"
                # Separar el teléfono y los puntos utilizando '*'
                telefono, puntos = telefono_puntos.split('*')  # Separar teléfono de puntos
                # Imprimir la fila de datos en formato alineado
                print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))

        input("Presiona Enter para continuar...")


    elif opcion == 7:
        print("\n========================================")
        print("         BÚSQUEDA DE CONTACTOS")
        print("========================================")
        print("1) Buscar por Nombre")  # Opción para buscar por Nombre
        print("2) Buscar por Apellido")  # Opción para buscar por Apellido
        print("3) Buscar por DNI")  # Opción para buscar por DNI
        print("4) Buscar por Teléfono")  # Opción para buscar por Teléfono
        print("5) Buscar por Puntos")  # Opción para buscar por Puntos
        print("6) Volver al menú principal")  # Opción para volver al menú principal
        print("========================================")

        opcion_buscar = input("Elige una opción de búsqueda: ")  # Solicita una opción al usuario

        if not opcion_buscar.isdigit() or int(opcion_buscar) < 1 or int(opcion_buscar) > 6:
            print("Opción no válida. Solo se permiten números del 1 al 6.")
            input("Presiona Enter para continuar...")
            continue  # Vuelve a mostrar el submenú de búsqueda

        opcion_buscar = int(opcion_buscar)

        if opcion_buscar == 1:
            criterio = input("Introduce el Nombre a buscar: ")
            resultados = [c for c in contactos if len(c.split(':')) > 1 and criterio.lower() in c.split(':')[0].lower()]
        elif opcion_buscar == 2:
            criterio = input("Introduce el Apellido a buscar: ")
            resultados = [c for c in contactos if len(c.split(':')) > 1 and '-' in c.split(':')[1] and criterio.lower() in c.split(':')[1].split('-')[0].lower()]
        elif opcion_buscar == 3:
            criterio = input("Introduce el DNI a buscar: ")
            resultados = [c for c in contactos if len(c.split('-')) > 1 and '_' in c.split('-')[1] and criterio.lower() in c.split('-')[1].split('_')[0].lower()]
        elif opcion_buscar == 4:
            criterio = input("Introduce el Teléfono a buscar: ")
            resultados = [c for c in contactos if len(c.split('_')) > 1 and '*' in c.split('_')[1] and criterio in c.split('_')[1].split('*')[0]]
        elif opcion_buscar == 5:
            criterio = input("Introduce los Puntos a buscar: ")
            resultados = [c for c in contactos if len(c.split('*')) > 1 and criterio in c.split('*')[1]]
        elif opcion_buscar == 6:
            continue  # Volver al menú principal

        if opcion_buscar != 6:
            # Imprimir los resultados de la búsqueda
            print("{:<10} {:<30} {:<10} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI", "Teléfono", "Puntos"))
            print("=" * 100)  # Línea divisoria para mejorar la presentación

            for registro in resultados:
                if registro:  # Comprobar que el registro no esté vacío
                    partes = registro.split(':')
                    if len(partes) < 2:
                        continue
                    nombre = partes[0]
                    apellido_datos = partes[1]
                    if '-' not in apellido_datos:
                        continue
                    apellidos, dni_telefono = apellido_datos.split('-')
                    dni, telefono_puntos = dni_telefono.split('_')
                    telefono, puntos = telefono_puntos.split('*')
                    print("{:<10} {:<30} {:<10} {:<20} {:<10}".format(nombre, apellidos, dni, telefono, puntos))

            input("Presiona Enter para continuar...")

    elif opcion == 8:
        print("Saliendo del programa...")
        salir = True  # Cambiamos la bandera 'salir' a True para terminar el bucle
