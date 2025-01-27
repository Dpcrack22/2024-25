items = "TR027-USB Memory 64 MB-15*UM302-INLET KIT 120SQM-27*GA204-4 POSITION BACKSHELL-35*CO056-SIZE 16 KEYING PIN, SOCKET-39"

menu00 = "menu Gestion De Productos".center(50, "*") + "\n1) Insertar nuevo producto \n2)Mostrar productos \n3)Exit"

salir = True
flag00 = True
flag01 = False
flag02 = False


while salir:
    while flag00:
        print(menu00)
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Only numerical option")
            input("Retry: ")

        else:
            choice = int(choice)
            if choice not in range(1, 4):
                print("Not in range option")
                input("Press Enter to ")
            else:
                if choice == 1:
                    flag01 = True
                    flag00 = False
                elif choice == 2:
                    flag02 = True
                    flag00 = False
                elif choice == 3:
                    salir = False
                    flag00 = False

    while flag01:
        new_code = input("Put an new code for the product: ")
        new_desc = input("Introduce the product description: ")
        new_price = input("Introduce the new price: ")
        new_product = "{}-{}-{}".format(new_code, new_desc, new_price)
        items_sep = items.split("*")
        flag00 = True
        flag01 = False

    while flag02:
        print("*"*50 + "\nCode".ljust(10) + "Description".rjust(10) + "Price".rjust(30) + "\n" + "*"*50)
        items_sep = items.split("*")
        for i in items_sep:
            todo = i.split("-")
            codigo = str(todo[0])
            desc = str(todo[1])
            price = str(todo[2])
            print(str(codigo).ljust(7), str(desc).ljust(30), str(price).rjust(10))
            flag02 = False
