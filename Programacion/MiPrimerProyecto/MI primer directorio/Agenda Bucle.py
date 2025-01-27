llista = "Agenda".center(30, "*") +  "\n" + "Nombre".ljust(15) + "Telefono".rjust(15) + "\n" + "*"*30 + "\n"

menu = "1) Nuevo Contacto\n2) Mostrar Agenda\n3) Salir"
salir = False
while not salir:
    print(menu)
    opcion = int(input("Opcion: "))
    if opcion == 1:
        Nombre = input("\n Introdueix el Nombre del Contacto: ")
        Telefono = input("\n Inrodueix el Telefono del contacto: ")

        llista = llista + "{0:15}{1:15}\n".format(Nombre, Telefono.rjust(15))
        input("\nEnter para Continuar: ")
    elif opcion == 2:
        print("\n" + llista)
        input("\nEnter para Continuar: ")
    elif opcion == 3:
        salir = True
    else:
        print("Opcion invalida (Marca un numero de las opciones)")

"""
En este ejercicio hemos hecho una lista en la cual se guarda la informacion mediante un bucle
"""