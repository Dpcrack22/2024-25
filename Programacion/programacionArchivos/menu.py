import funciones_lista as FL

menu00 = " 1. Nuevo Contacto \n 2. Buscar Contacto \n 3. Listar Contactos \n 4. Salir"
menu01 = " 1) Por Nombre \n 2) Por Tfn \n 3) Por DNI \n 4) Ir Atras"
menu02 = " 1) Ordenar por DNI \n 2) Ordenar por Nombre \n 3) Ordenar por Telefono \n 4) Ordenar por Apellido \n 5) Ir atras"
salir = True
menu1 = False
menu2 = False

while salir:
    print(menu00)
    opc = input("Selecciona una opcion: ")
    if not opc.isdigit():
        print("Solo numeros")
        input("Press Enter to continue")
    elif not int(opc) in range(1, 5):
        print("No en rango")
        input("Press Enter to continue")
    else:
        if int(opc) == 1:
            FL.guardar_contacto("Contactos")
        if int(opc) == 2:
            menu1 = True
            salir = False
        if int(opc) == 3:
            menu2 = True
            salir = False
        if int(opc) == 4:
            print("Saliendo de Contactos...")
            salir = False


while menu1:
    print(menu01)
    opc1 = input("Selecciona una opcion: ")
    if not opc1.isdigit():
        print("Solo numeros")
        input("Press Enter to continue")
    elif not int(opc1) in range(1, 5):
        print("No en rango")
        input("Press Enter to continue")
    else:
        if int(opc1) == 1:
            valor = "nombre"
            criterio = input("Dame el nombre del contacto: ")
            FL.buscar_contacto("Contactos",valor,criterio)
            input("Enter to continue: ")
        if int(opc1) == 2:
            valor = "tfn"
            criterio = input("Dame el telefono del contacto: ")
            FL.buscar_contacto("Contactos",valor,criterio)
            input("Enter to continue: ")
        if int(opc1) == 3:
            valor = "dni"
            criterio = input("Dame el DNI del contacto: ")
            FL.buscar_contacto("Contactos",valor,criterio)
            input("Enter to continue: ")
        if int(opc1) == 4:
            salir = True
            menu1 = False


while menu2:
    print(menu01)
    opc1 = input("Selecciona una opcion: ")
    if not opc1.isdigit():
        print("Solo numeros")
        input("Press Enter to continue")
    elif not int(opc1) in range(1, 6):
        print("No en rango")
        input("Press Enter to continue")
    else:
        if int(opc1) == 1:
            criterio = "dni"
            FL.listar_contactos("Contactos",criterio)

        if int(opc1) == 2:
            criterio = "nombre"
            FL.listar_contactos("Contactos",criterio)

        if int(opc1) == 3:  
            criterio = "apellido"
            FL.listar_contactos("Contactos",criterio)

        if int(opc1) == 4:  
            criterio = "tfn"
            FL.listar_contactos("Contactos",criterio)

        if int(opc1) == 5:
            salir = True
            menu2 = False