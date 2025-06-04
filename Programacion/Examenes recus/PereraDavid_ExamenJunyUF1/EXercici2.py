players = {"47474747R":{"name":"Pedro Javier Morales", "tfn":["+0034345345345"], "points":12},"24536425T":{"name":"Maite Lopez Miravet", "tfn":["+0034234234235","+0034239999235"],"points":15},"76767676H":{"name":"Marta Garcia Suarez", "tfn": ["+0075766576575"], "points":21},"84848484I":{"name":"Aitana Sanchez Castillejos", "tfn": ["+0088823303445"], "points":16},"12345623I":{"name":"Sergio Alarcon Navas", "tfn": ["+0066688221122"], "points":12}}


salir = True
flag_00 = True
flag_01 = False
flag_02 = False
flag_03 = False

menu00 = "1) Search Player\n2) List Players\n3) Exit\n"
menu01 = "1) By name\n2) By DNI\n3) By tfn\n4) Go back"
menu02 = "1) List by name\n2) List by DNI\n3) List by tfn\n4) Go back"

while salir:
    while flag_00:
        print(menu00)
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
            print("Por favor, ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion not in range(1, 4):
                print("Opción no válida, por favor intente de nuevo.")
            else:
                if opcion == 1:
                    flag_01 = True
                    flag_00 = False
                elif opcion == 2:
                    flag_02 = True
                    flag_00 = False
                elif opcion == 3:
                    
                    salir = False
                    flag_00 = False
                    print("Saliendo del programa...")

    while flag_01:
        print(menu01)
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
            print("Por favor, ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion not in range(1, 5):
                print("Opción no válida, por favor intente de nuevo.")
            else:
                encontrado = False
                datos = ""
                if opcion == 1:
                    lista_nombres = list(players.keys())
                    nombre = input("Ingrese el nombre del jugador a buscar: ")
                    for dni in players:
                        if nombre in players[dni]["name"]:
                            encontrado = True
                            datos += str(players[dni]["name"]).ljust(35) + dni.ljust(10) + str(players[dni]["points"]).rjust(10)
                            for i in range(len(players[dni]["tfn"])):
                                if i == 0:
                                    datos += str(players[dni]["tfn"][i]).rjust(20) +"\n"
                                else:
                                    datos += " "*55 + str(players[dni]["tfn"][i]).rjust(20) +"\n"
                                
                    if encontrado:
                        print("Players".center(60, "*") + "\n" + "Name".ljust(35) + "DNI".ljust(10) + "Points".rjust(10) + "tfn".rjust(20))
                        print(datos)
                        input("Presione Enter para continuar...")
                    else:
                        print("Jugador no encontrado.")
                        input("Presione Enter para continuar")
                if opcion == 2:
                    
                    lista_nombres = list(players.keys())
                    nif = input("Ingrese el dni del jugador a buscar: ")
                    for dni in players:
                        if nif in dni:
                            encontrado = True
                            datos += str(players[dni]["name"]).ljust(35) + dni.ljust(10) + str(players[dni]["points"]).rjust(10)
                            for i in range(len(players[dni]["tfn"])):
                                if i == 0:
                                    datos += str(players[dni]["tfn"][i]).rjust(20) +"\n"
                                else:
                                    datos += " "*55 + str(players[dni]["tfn"][i]).rjust(20) +"\n"
                                
                    if encontrado:
                        print("Players".center(60, "*") + "\n" + "Name".ljust(35) + "DNI".ljust(10) + "Points".rjust(10) + "tfn".rjust(20))
                        print(datos)
                        input("Presione Enter para continuar...")
                    else:
                        print("Jugador no encontrado.")
                        input("Presione Enter para continuar")

                if opcion == 3:
                    lista_nombres = list(players.keys())
                    telefono = input("Ingrese el nombre del jugador a buscar: ")
                    for dni in players:
                        if telefono in str(players[dni]["tfn"]):
                            encontrado = True
                            datos += str(players[dni]["name"]).ljust(35) + dni.ljust(10) + str(players[dni]["points"]).rjust(10)
                            for i in range(len(players[dni]["tfn"])):
                                if i == 0:
                                    datos += str(players[dni]["tfn"][i]).rjust(20) +"\n"
                                else:
                                    datos += " "*55 + str(players[dni]["tfn"][i]).rjust(20) +"\n"
                                
                    if encontrado:
                        print("Players".center(60, "*") + "\n" + "Name".ljust(35) + "DNI".ljust(10) + "Points".rjust(10) + "tfn".rjust(20))
                        print(datos)
                        input("Presione Enter para continuar...")
                    else:
                        print("Jugador no encontrado.")
                        input("Presione Enter para continuar")
                
                if opcion == 4:
                    flag_00 = True
                    flag_01 = False

    while flag_02:
        print(menu02)
        opcion = input("Opcion: ")
        if not opcion.isdigit():
            input("Numero invalido. Vuelva a intentarlo: ")
        else:
            opcion = int(opcion)
            if opcion not in range(1, 5):
                input("Numero no en el rango. Vuelva a intentarlo: ")
            else:
                #"47474747R":{"name":"Pedro Javier Morales", "tfn":["+0034345345345"], "points":12}
                if opcion == 1:
                    datos = ""
                    telefonos = ""
                    lista_nombres = list(players.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if players[lista_nombres[i]]["name"] < players[lista_nombres[i+1]]["name"]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                    
                    

                    for dni in lista_nombres:
                        datos += str(players[dni]["name"]).ljust(35) + dni.ljust(10) + str(players[dni]["points"]).rjust(10)
                        for i in range(len(players[dni]["tfn"])):
                            if i == 0:
                                datos += str(players[dni]["tfn"][i]).rjust(20) +"\n"
                            else:
                                datos += " "*55 + str(players[dni]["tfn"][i]).rjust(20) +"\n"
                        
                    
                    print("Players".center(60, "*") + "\n" + "Name".ljust(35) + "DNI".ljust(10) + "Points".rjust(10) + "tfn".rjust(20))
                    print(datos)
                    input("Presione Enter para continuar...")

                if opcion == 2:
                    datos = ""
                    telefonos = ""
                    lista_nombres = list(players.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if lista_nombres[i] < lista_nombres[i+1]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                    
                    

                    for dni in lista_nombres:
                        datos += str(players[dni]["name"]).ljust(35) + dni.ljust(10) + str(players[dni]["points"]).rjust(10)
                        for i in range(len(players[dni]["tfn"])):
                            if i == 0:
                                datos += str(players[dni]["tfn"][i]).rjust(20) +"\n"
                            else:
                                datos += " "*55 + str(players[dni]["tfn"][i]).rjust(20) +"\n"
                        
                    
                    print("Players".center(60, "*") + "\n" + "Name".ljust(35) + "DNI".ljust(10) + "Points".rjust(10) + "tfn".rjust(20))
                    print(datos)
                    input("Presione Enter para continuar...")
            
                if opcion == 3:
                    datos = ""
                    telefonos = ""
                    lista_nombres = list(players.keys())
                    for pasada in range(len(lista_nombres)):
                        for i in range(len(lista_nombres)-1-pasada):
                            if players[lista_nombres[i]]["tfn"] < players[lista_nombres[i+1]]["tfn"]:
                                aux = lista_nombres[i+1]
                                lista_nombres[i+1] = lista_nombres[i]
                                lista_nombres[i] = aux
                    
                    

                    for dni in lista_nombres:
                        datos += str(players[dni]["name"]).ljust(35) + dni.ljust(10) + str(players[dni]["points"]).rjust(10)
                        for i in range(len(players[dni]["tfn"])):
                            if i == 0:
                                datos += str(players[dni]["tfn"][i]).rjust(20) +"\n"
                            else:
                                datos += " "*55 + str(players[dni]["tfn"][i]).rjust(20) +"\n"
                        
                    
                    print("Players".center(60, "*") + "\n" + "Name".ljust(35) + "DNI".ljust(10) + "Points".rjust(10) + "tfn".rjust(20))
                    print(datos)
                    input("Presione Enter para continuar...")

                if opcion == 4:
                    flag_00 = True
                    flag_02 = False