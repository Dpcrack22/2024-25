llista = "*"*50 + "\n" + "DNI".ljust(15) + "Nombre".ljust(15) + "Nota". ljust(5) + "Nota boletin". rjust(15) + "\n" + "*"*50 + "\n"


menu = "1) Nuevo alumno\n2) Mostrar alumnos\n3) Salir"
salir = False
while not salir:
    print(menu)
    opcion = int(input("Opcion: "))
    if opcion == 1:
        DNI1 = input("\n Introdueix el DNI del Alumne")
        Alumne1 = input("\n Inrodueix el Nom del alumne")
        Nota1 = float(input("\n Introdueix la nota del alumne"))
        if Nota1 < 5:
            Boletin = ("Suspes")
        elif 5 <= Nota1 < 6:
            Boletin = ("Aprobat")
        elif 6 <= Nota1 < 7:
            Boletin = ("Be")
        elif 7 <= Nota1 < 9:
            Boletin = ("Notable")
        else:
            Boletin = ("Excelent")
        llista = llista + "{0:15}{1:15}{2:5.2f}{3:15}\n".format(DNI1, Alumne1, Nota1, Boletin)
    elif opcion == 2:
        print("\n" + llista)
    elif opcion == 3:
        salir = True
    else:
        print("Opcion invalida (Marca un numero de las opciones)")

"""
En este ejercicio hemos hecho una lista en la cual se guarda la informacion mediante un bucle
"""