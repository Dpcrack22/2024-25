from itertools import repeat

clientes = {
    "34343434A":{"nombre":"Teodoro","codigo":"AFT3245","tfn":["+0034234343434","917174556"],"compras":[234,43,567]},
    "54545454T":{"nombre":"Amaia","codigo":"TSR8462","tfn":["+0034876545454","914568392"],"compras":[1001,34]},
    "12344123G":{"nombre":"Isidoro","codigo":"NTZ4123","tfn":["+0034453464564"],"compras":[2300,340,34,123]},
    "62323455B":{"nombre":"Ines","codigo":"UTN4875","tfn":["+0034456411564"],"compras":[485,568,682,456,12]},
    "81238478S":{"nombre":"Soraya","codigo":"TSX8245","tfn":[],"compras":[854]},
    "96345245J":{"nombre":"Carlos","codigo":"VNP6438","tfn":["+0034848262626","938847575"],"compras":[34,645,680]},
    "44234423U":{"nombre":"Ernesto","codigo":"KSQ9345","tfn":["+0034777334455","918765445"],"compras":[939,34,145]}
}
dni_letters = "T;R;W;A;G;M;Y;F;P;D;X;B;N;J;Z;S;Q;V;H;L;C;K;E;"

menu00 = "Examen Final UF1".center(40, "*") + "\n" + "\n" + "1) New Costumer" + "\n" + "2) List Customer" + "\n" + "3) Find Costumers" + "\n" + "4) Exit"
menu01 = "New Costumer".center(40, "*")
menu02 = "List Costumers".center(40, "*") + "\n" + "\n" + "1) Show clients ordered By NIF" + "\n" + "2) Show clients ordered By numeric code" + "\n" + "3) Show clients ordered By purchases" + "\n" + "4) Exit"



salir = True
flag0 = True
flag01 = False
flag02 = False
flag03 = False
flag04 = False


while salir:
    while flag0:
        print(menu00)
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Only numerical option")
            input("Retry: ")

        else:
            choice = int(choice)
            if choice not in range(1, 5):
                print("Not in range option")
                input("Press Enter to ")
            else:
                if choice == 1:
                    flag01 = True
                    dni = True
                    flag0 = False
                elif choice == 2:
                    print(menu02)
                    flag02 = True
                    flag0 = False
                elif choice == 3:
                    print(menu01)
                    flag03 = True
                    flag0 = False
                elif choice == 4:
                    salir = False
                    flag0 = False

    while flag01:
        while dni:
            newDNI = input("Enter DNI: ")
            auxiliar = []
            for key_id, valor_info in clientes.items():
                auxiliar.append([key_id, valor_info])

            if len(newDNI) == 9:
                letra_nie = int(newDNI[:8]) % 23
                for i in range(letra_nie + 1):
                    if i == 0:
                        inicio = 0
                        final = dni_letters.index(";")
                    else:
                        inicio = final + 1
                        final = dni_letters.index(";", inicio)
                letra_seleccionada = dni_letters[inicio:final]
                if not newDNI[:8].isdigit():
                    input("DNI no válido, los primeros 8 números deben ser dígitos\nPresiona Enter para continuar...")
                elif not newDNI[8:].isalpha():
                    input("DNI no válido, la letra debe ser alfabética\nPresiona Enter para continuar...")
                elif letra_seleccionada.upper() != newDNI[8:].upper():
                    input("DNI no válido, letra incorrecta\nPresiona Enter para continuar...")
                elif newDNI in auxiliar[0]:
                    input("DNI ya existe Intentelo de nuevo\nPresiona Enter para continuar...")
                else:
                    newDNI = newDNI[:8] + newDNI[8:].upper()
                    print("NIE aceptado")
                    new_name = True
                    dni = False
            else:
                input("NIE no válido, debe tener 8 números y 1 letra al final\nPresiona Enter para continuar...")
        while new_name:
            name = input("Introduce el nombre y apellido: ")
            if not name.isalpha():
                print("Invalid Name")
            elif name == "":
                print("Put a correct name")
            else:
                add_tfn = True
                new_name = False

        while add_tfn:
            seleccion = input("Do you want to add a telephone number").upper()
            if seleccion == "Y":
                telefono = input("Enter Tfn (Formato: +0034 xxxxxxxxx o 9 digitos nada mas): ")
                if telefono.startswith("+0034") and len(telefono) == 14 and telefono[5:].isdigit() or len(telefono) == 9 and telefono.isdigit():
                    new_tfn = list(telefono)
                    seleccion2 = input("Do you want to add another telephone number").upper()
                    if seleccion2 == "Y":
                        add_tfn = False
                        add_anothertfn = True
                    else:
                        save_customer = True
                        add_tfn = False
            elif seleccion == "N":
                save_customer = True
                add_tfn = False
            else:
                print("Invalid Option")

        while add_anothertfn:
            telefono = input("Enter Tfn (Formato: +0034 xxxxxxxxx o 9 digitos nada mas): ")
            if telefono.startswith("+0034") and len(telefono) == 14 and telefono[5:].isdigit() or len(
                telefono) == 9 and telefono.isdigit():
                new_tfn = new_tfn + telefono
                save_customer = True
                add_anothertfn = False
            else:
                print("Número de teléfono inválido. Debe tener el formato +0034 seguido de 9 dígitos o 9 digitos nada mas")



    #Listar#
    while flag02:
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
                auxiliar = []
                for key_id, valor_info in clientes.items():
                    auxiliar.append([key_id, valor_info])


                choice = int(choice)

                if choice == 1:

                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][0] > auxiliar[i + 1][0]:
                                aux = auxiliar[i]
                                auxiliar[i] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    for i in range(len(auxiliar)):
                        auxiliar_id = auxiliar[i][0]
                        auxiliar_nombre = auxiliar[i][1]["nombre"]
                        auxiliar_codigo = auxiliar[i][1]["codigo"]
                        auxiliar_tfn = auxiliar[i][1]["tfn"]
                        auxiliar_compras = auxiliar[i][1]["compras"]
                        print("ID: " + str(auxiliar_id), "Name:" + auxiliar_nombre,
                              "Codigo: " + str(auxiliar_codigo), "Telefono: " + str(auxiliar_tfn),
                              "Compras: " + str(auxiliar_compras))
                if choice == 2:

                    for pasadas in range(len(auxiliar) - 1):
                        for i in range(len(auxiliar) - pasadas - 1):
                            if auxiliar[i][1]["nombre"] > auxiliar[i + 1][0]["nombre"]:
                                aux = auxiliar[i]["nombre"]
                                auxiliar[i]["nombre"] = auxiliar[i + 1]
                                auxiliar[i + 1] = aux
                    for i in range(len(auxiliar)):
                        auxiliar_id = auxiliar[i][0]
                        auxiliar_nombre = auxiliar[i][1]["nombre"]
                        auxiliar_codigo = auxiliar[i][1]["codigo"]
                        auxiliar_tfn = auxiliar[i][1]["tfn"]
                        auxiliar_compras = auxiliar[i][1]["compras"]
                        print("ID: " + str(auxiliar_id), "Name:" + auxiliar_nombre,
                              "Codigo: " + str(auxiliar_codigo), "Telefono: " + str(auxiliar_tfn),
                              "Compras: " + str(auxiliar_compras))
