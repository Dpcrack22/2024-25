discografia = "Abbey Road*1969*The Beatles-The Dark Side of the Moon*1973*Pink Floyd-Born to Run*1975*Bruce Springsteen-Hotel California*1976*Eagles-Rumours*1977*Fleetwood Mac-Back in Black*1980*AC/DC-Thriller*1982*Michael Jackson-The Joshua Tree*1987*U2-Nevermind*1991*Nirvana-OK Computer*1997*Radiohead"

menu0 = "1. Mostrar discografía\n2. Añadir disco (Ordenado por año)\n3. Buscar disco\n5. Salir\n"
menu03 = "1. Buscar por disco\n2. Buscar por año\n3. Buscar por grupo\n4. Volver al menú principal\n"

titulo1 = "Discografía".center(60, "*") + "\nDiscos".ljust(30) + "Año".rjust(10) + "Grupo".rjust(20) + "\n" + "*" * 60 + "\n"


condicion = True

while condicion:

    print(menu0)

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print(titulo1)
        discosSeparados = discografia.split("-")
       #print(discos)
        for i in range(len(discosSeparados)):
            discos = discosSeparados[i].split("*")
            disco = discos[0]
            año = discos[1]
            grupo = discos[2]
            #print(discos)
            print(disco.ljust(30), año.rjust(10), grupo.rjust(20))

    elif opcion == "2":
        nuevoDisco = True
        while nuevoDisco:
            disco = input("Introduce el nombre del disco: ")
            año = input("Introduce el año de lanzamiento: ")
            grupo = input("Introduce el nombre del grupo: ")

            if len(disco) > 30:
                print("El nombre del disco no puede tener más de 30 caracteres")
                continue
            if len(grupo) > 20:
                print("El grupo no puede tener más de 20 caracteres")
                continue

            nuevoRegistro = "{}*{}*{}".format(disco, año, grupo)
            discosSeparados = discografia.split("-")
            insertado = False
            nuevaDiscografia = ""
            
            for i in range(len(discosSeparados)):
                actual = discosSeparados[i].split("*")
                año_actual = int(actual[1])
                disco_actual = actual[0]

                if not insertado and (int(año) < año_actual or (int(año) == año_actual and disco < disco_actual)):
                    nuevaDiscografia += nuevoRegistro + "-"
                    insertado = True

                nuevaDiscografia += discosSeparados[i]
                if i != len(discosSeparados) - 1:
                    nuevaDiscografia += "-"

            if not insertado:
                nuevaDiscografia += "-" + nuevoRegistro

            discografia = nuevaDiscografia
            print(discografia)
            print("Disco añadido correctamente.\n")
            nuevoDisco = False

    elif opcion == "3":
        print(menu03)
        opcionBusqueda = input("Seleccione una opción: ")
        if opcionBusqueda == "1":
            discoBuscado = input("Introduce el nombre del disco a buscar: ")
            encontrado = False
            for registro in discografia.split("-"):
                if discoBuscado.lower() in registro.lower():
                    encontrado = True
                    print(registro)
            if not encontrado:
                print("Disco no encontrado.")

        elif opcionBusqueda == "2":
            añoBuscado = input("Introduce el año a buscar: ")
            encontrado = False
            for registro in discografia.split("-"):
                if añoBuscado in registro:
                    encontrado = True
                    print(registro)
            if not encontrado:
                print("Año no encontrado.")

        elif opcionBusqueda == "3":
            grupoBuscado = input("Introduce el nombre del grupo a buscar: ")
            encontrado = False
            for registro in discografia.split("-"):
                if grupoBuscado.lower() in registro.lower():
                    encontrado = True
                    print(registro)
            if not encontrado:
                print("Grupo no encontrado.")

        elif opcionBusqueda == "4":
            continue


