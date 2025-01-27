letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}

menu00 = "1)Create User\n2)Modify user\n3)Show Users\n4)Find Users\n5)List Users\n6)Exit"
menu01 = "1)Enter Dni\n2)Enter Name\n3)Enter Surname\n4)Enter Address\n5)Enter Tfn\n6)Save User\n7)Go Back"
menu02 = "\n"+"Menu 02 - Modify User".center(50,"*")+"\n"+"1)Add purchase\n2)Add tfn number\n3)Del tfn number\n4)Change address\n5)Go Back"
menu05 = "1)List Users by DNI\n2)List Users by Name\n3)List Users by Address\n4)List Users by Total Purchase\n5)Go back"
menu04 = "1)Find Users by DNI\n2)Find Users by Name\n3)Go back"

salir = False

while not salir:
    print(menu00)
    opcion = input("Selecciona Una Opcion: ")
    if not opcion.isdigit():
        print("Only numerical option")
        input("Press Enter to continue")
    elif not int(opcion) in range(1, 6):
        print("Not in range option")
        input("Press Enter to continue")
    if int(opcion) == 1:
        nuevo_usuario = {"dni": "", "nombre": "", "apellido": "", "direccion": "", "tfn": []}

        creando_usuario = True
        while creando_usuario:
            print("\nDni:*           ", nuevo_usuario["dni"] + "\nName:*          ", nuevo_usuario["nombre"] + "\nSurname:*       ", nuevo_usuario["apellido"] + "\nAddress:*       ", nuevo_usuario["direccion"] + "\ntfn:            ", ", ",nuevo_usuario["tfn"])

            print(menu01)
            subopc = input("Dame una Opcion: ")

            if not subopc.isdigit():
                print("Only numerical option")
                input("Press Enter to continue")
            elif not int(subopc) in range(1, 8):
                print("Not in range option")
                input("Press Enter to continue")
            if int(subopc) == 1:
                dni = input("Dame DNI: ")
                if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
                    numero = int(dni[:-1])

                    letra_Correcta = letrasDni[numero % 23]
                    if dni[-1].upper() == letra_Correcta:
                        nuevo_usuario["dni"] = dni
                    else:
                        print("DNI invalido: letra incorrecta")
                else:
                    print("DNI invalido debe contener 8 digitos")
            elif int(subopc) == 2:
                nuevo_usuario["nombre"] = input("Dime tu Nombre: ")

            elif int(subopc) == 3:
                nuevo_usuario["apellido"] = input("Dame tu Apellido: ")

            elif int(subopc) == 4:
                nuevo_usuario["direccion"] = input("Dame tu Direccion: ")

            elif int(subopc) == 5:
                telefono = input("Dame tu numero en formato +0034 acompañado de los 9 dijitos: ")
                if telefono.startswith("+0034") and len(telefono) == 14 and telefono[5:].isdigit():
                    nuevo_usuario["tfn"].append(telefono)
                else:
                    print("Numero incorrecto. Debe de tener formato +0034*********")

            elif int(subopc) == 6:
                if nuevo_usuario["dni"] == "" or nuevo_usuario["nombre"] == "" or nuevo_usuario["apellido"] == "" or nuevo_usuario["direccion"] == "":
                    print("Faltan Campos Obligatorios")
                else:
                    usuarios[nuevo_usuario["dni"]] = {"nombre": nuevo_usuario["nombre"] + " " + nuevo_usuario["apellido"], "direccion": nuevo_usuario["direccion"], "tfn": nuevo_usuario["tfn"] or [], "compras": []}

                    creando_usuario = False

            elif int(subopc) == 7:
                creando_usuario = False

            else:
                print("Opcion invalida. Intente de nuevo")

    if int(opcion) == 2:
        dni_corr = True
        while dni_corr:
            dni = input("Dame DNI para buscar al usuario: ")
            if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
                dni_corr = False
            else:
                print("Dni no valido")


        if dni in usuarios:
            modificando_usuario = True
            usuario_actual = usuarios[dni]

            while modificando_usuario:
                print(menu02)
                subopc = input("Dame una opcion: ")

                if not subopc.isdigit():
                    print("Only numerical option")
                    input("Press Enter to continue")
                elif not int(subopc) in range(1, 8):
                    print("Not in range option")
                    input("Press Enter to continue")

                elif int(subopc) == 1:
                    compras = input("Dime Tu Compra: ")
                    if not compras.isdigit():
                        print("Solo opciones Numericas")
                    else:
                        compras = int(compras)
                        usuario_actual["compras"].append(compras)
                        print()

                elif int(subopc) == 2:
                    nuevo_tfn = input("Dame el nuevo numero de telefono (+0034xxxxxxxxx): ")
                    if nuevo_tfn.startswith("+0034") and len(nuevo_tfn) == 13 and nuevo_tfn[5:].isdigit():
                        usuario_actual["tfn"].append(nuevo_tfn)
                        print("Numero de telefono añadido")
                    else:
                        print("Invalido el formato de telefono ")

                elif int(subopc) == 3:
                    if not usuario_actual["tfn"]:
                        print("Este usuario no tiene numero de telefono")
                    else:
                        print("Numeros de telefono actuales:", usuario_actual["tfn"])
                        del_tfn = input("Dame un numero para eliminar")
                        if del_tfn in usuarios["tfn"]:
                            usuario_actual["tfn"].remove(del_tfn)
                            print("Numero de telefono eliminado")
                        else:
                            print("Numero de telefono no encontrado")

