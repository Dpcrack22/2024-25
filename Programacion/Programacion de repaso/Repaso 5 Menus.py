menu0 = False
menu01 = False
menu02 = False


while menu0:
    opcion = input("Selecciona Una Opcion: ")
    if not opcion.isdigit():
        print("Only numerical option")
        input("Press Enter to continue")
    elif not int(opcion) in range(1, 3):
        print("Not in range option")
        input("Press Enter to continue")
    else:
        if int(opcion) == 1:
            menu01 = True
            menu0 = False
        elif int(opcion) == 2:
            menu02 = True
            menu0 = False

while menu01:
    opcion = input("Selecciona Una Opcion: ")
    if not opcion.isdigit():
        print("Only numerical option")
        input("Press Enter to continue")
    elif not int(opcion) in range(1, 3):
        print("Not in range option")
        input("Press Enter to continue")
    else:
        if int(opcion) == 1:
            print("menu011")
            menu0 = True
            menu01 = False

        elif int(opcion) == 2:
            print("menu012")
            menu0 = True
            menu01 = False

while menu02:
    opcion = input("Selecciona Una Opcion: ")
    if not opcion.isdigit():
        print("Only numerical option")
        input("Press Enter to continue")
    elif not int(opcion) in range(1, 3):
        print("Not in range option")
        input("Press Enter to continue")
    else:
        if int(opcion) == 1:
            print("menu021")
            menu0 = True
            menu02 = False

        elif int(opcion) == 2:
            print("menu022")
            menu0 = True
            menu02 = False


menu00 = "Menu00".center(20,"*") + "\n" + "1: Opcion1" + "\n" + "2: Opcion2" + "\n" + "3: Salir"

menu001 = "Menu001".center(20,"*") + "\n" + "1: Opcion1" + "\n" + "2: Opcion2" + "\n" + "3: Back"
menu002 = "Menu002".center(20,"*") + "\n" + "1: Opcion1" + "\n" + "2: Opcion2" + "\n" + "3: Back"

flg_salir = False
flg_00 = True
flg_01 = False
flg_02 = False
flg_011 = False
flg_012 = False
flg_021 = False
flg_022 = False

while not flg_salir:
    while flg_00:
        print(menu00)
        opc = input("Selecciona una opcion: ")
        if not opc.isdigit():
            print("Opcion no numerica")
            input("Enter to continue: ")
        elif not int(opc) in range(1,4):
            print("Opcion Fuera de rango")
            input("Enter to continue: ")
        else:
            opc = int(opc)
            if opc == 1:
                flg_01 = True
                flg_00 = False
            elif opc ==2:
                flg_02 = True
                flg_00 = False
            elif opc ==3:
                flg_salir = True
                flg_00 = False
            


    while flg_01:
        print(menu001)
        opc = input("Selecciona una opcion: ")
        if not opc.isdigit():
            print("Opcion no numerica")
            input("Enter to continue: ")
        elif not int(opc) in range(1,4):
            print("Opcion Fuera de rango")
            input("Enter to continue: ")
        else:
            opc = int(opc)
            if opc == 1:
                flg_011 = True
                flg_01 = False
            elif opc ==2:
                flg_012 = True
                flg_01 = False
            elif opc ==3:
                flg_00 = True
                flg_01 = False


    while flg_02:
        print(menu002)
        opc = input("Selecciona una opcion: ")
        if not opc.isdigit():
            print("Opcion no numerica")
            input("Enter to continue: ")
        elif not int(opc) in range(1,4):
            print("Opcion Fuera de rango")
            input("Enter to continue: ")
        else:
            opc = int(opc)
            if opc == 1:
                flg_021 = True
                flg_02 = False
            elif opc ==2:
                flg_022 = True
                flg_02 = False
            elif opc ==3:
                flg_00 = True
                flg_02 = False
