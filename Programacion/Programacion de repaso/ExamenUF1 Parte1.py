import random
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
add_anothertfn = False


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
                    #print(menu02)
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
            if not name.replace(" ","").isalpha():
                print("Invalid Name")
            elif name == "":
                print("Put a correct name")
            else:
                add_tfn = True
                new_name = False

        while add_tfn:
            telefonos = []
            seleccion = input("Do you want to add a telephone number? Y/N  ").upper()
            if seleccion == "Y":
                telefono = input("Enter Tfn (Formato: +0034 xxxxxxxxx o 9 digitos nada mas): ")
                if telefono.startswith("+0034") and len(telefono) == 14 and telefono[5:].isdigit() or len(telefono) == 9 and telefono.isdigit():
                    telefonos.append(telefono)
                    seleccion2 = input("Do you want to add another telephone number? Y/N  ").upper()
                    if seleccion2 == "Y":
                        add_tfn = False
                        add_anothertfn = True
                    else:
                        save_customer = True
                        add_tfn = False
                else:
                    print("Número de teléfono inválido. Debe tener el formato +0034 seguido de 9 dígitos o 9 digitos nada mas")
            elif seleccion == "N":
                save_customer = True
                add_tfn = False
            else:
                print("Invalid Option")

        while add_anothertfn:
            telefono = input("Enter Tfn (Formato: +0034 xxxxxxxxx o 9 digitos nada mas): ")
            if telefono.startswith("+0034") and len(telefono) == 14 and telefono[5:].isdigit() or len(telefono) == 9 and telefono.isdigit():
                telefonos.append(telefono)
                save_customer = True
                add_anothertfn = False
            else:
                print("Número de teléfono inválido. Debe tener el formato +0034 seguido de 9 dígitos o 9 digitos nada mas")

        while save_customer:
            copdigoaleatorio = ""
            lista_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
            for i in range(3):
                longitud_letras = len(lista_letras)
                numero_aleatorio = random.randrange(0, longitud_letras)
                copdigoaleatorio += lista_letras[numero_aleatorio]
            for i in range(4):
                numero_aleatorio = random.randrange(0, 10)
                copdigoaleatorio += str(numero_aleatorio)

            for i in clientes:
                if clientes[i]["codigo"] == copdigoaleatorio:
                    print("Codigo repetido, generando otro codigo")
                    confirmacion = False
                else:
                    confirmacion = True
            
            
            if confirmacion == True:
                print("Codigo generado correctamente")
                clientes[newDNI] = {"nombre": name, "codigo": copdigoaleatorio, "tfn": telefonos, "compras": []}
                print("Cliente añadido correctamente")
                print("DNI: " + newDNI)
                print("Nombre: " + name)
                print("Codigo: " + copdigoaleatorio)
                print("Telefonos: " + ", " , telefonos)
                input("Press Enter to continue...")
                flag0 = True
                flag01 = False
                dni = False
                save_customer = False
                    

    #Listar#
    while flag02:
        print(menu02)
        datos = "Clientes".center(80,"=") + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Codigo".ljust(10) + "Tfn".rjust(15) + "Total Comparas".rjust(20) + "\n" + "=" * 80 + "\n"
        #print(datos)
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Only numerical option")
            input("Retry: ")

        else:
            
            choice = int(choice)
            if choice not in range(1, 4):
                print("Not in range option")
                input("Retry: ")

            else:


                if choice == 1:
                    lista_dnis = list(clientes.keys())
                    for pasada in range(len(lista_dnis)):
                        for i in range(len(lista_dnis)-1-pasada):
                            if lista_dnis[i] > lista_dnis[i+1]:
                                aux = lista_dnis[i+1]
                                lista_dnis[i+1] = lista_dnis[i]
                                lista_dnis[i] = aux
                    for dni in lista_dnis:
                        datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) + str(clientes[dni]["codigo"]).ljust(10)
                        telefonos = clientes[dni]["tfn"]
                        total_compras = 0
                        for i in range(len(clientes[dni]["compras"])):
                            total_compras += clientes[dni]["compras"][i]
                        
                        
                        if len(telefonos) == 0:
                            datos += "".rjust(15) + str(total_compras).rjust(20) + "\n"
                        else:
                            for i in range(len(telefonos)):
                                if i == 0:
                                    datos += str(telefonos[i]).rjust(15) + str(total_compras).rjust(20) +"\n"
                                else:
                                    datos += " ".ljust(45) + str(telefonos[i]).rjust(15) +"\n"

                    print(datos)
                    input("Press Enter to continue...")
                
                if choice == 2:
                    lista_dnis = list(clientes.keys())
                    for pasada in range(len(lista_dnis)):
                        for i in range(len(lista_dnis)-1-pasada):
                            if clientes[lista_dnis[i]]["codigo"] > clientes[lista_dnis[i+1]]["codigo"]:
                                aux = lista_dnis[i+1]
                                lista_dnis[i+1] = lista_dnis[i]
                                lista_dnis[i] = aux
                    
                    for dni in lista_dnis:
                        datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) + str(clientes[dni]["codigo"]).ljust(10)
                        telefonos = clientes[dni]["tfn"]
                        total_compras = 0
                        for i in range(len(clientes[dni]["compras"])):
                            total_compras += clientes[dni]["compras"][i]
                        
                        
                        if len(telefonos) == 0:
                            datos += "".rjust(15) + str(total_compras).rjust(20) + "\n"
                        else:
                            for i in range(len(telefonos)):
                                if i == 0:
                                    datos += str(telefonos[i]).rjust(15) + str(total_compras).rjust(20) +"\n"
                                else:
                                    datos += " ".ljust(45) + str(telefonos[i]).rjust(15) +"\n"
                     
                    print(datos)
                    input("Press Enter to continue...")

                if choice == 3:                    
                    lista_dnis = list(clientes.keys())
                    for pasada in range(len(lista_dnis)):
                        for i in range(len(lista_dnis)-1-pasada):

                            total_compras = 0
                            total_comprasI = 0
                            for compra in clientes[lista_dnis[i]]["compras"]:
                                total_compras += compra

                            for compra in clientes[lista_dnis[i+1]]["compras"]:
                                total_comprasI += compra

                            if total_compras > total_comprasI:
                                aux = lista_dnis[i+1]
                                lista_dnis[i+1] = lista_dnis[i]
                                lista_dnis[i] = aux
                    
                    for dni in lista_dnis:
                        datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) + str(clientes[dni]["codigo"]).ljust(10)
                        telefonos = clientes[dni]["tfn"]
                        
                        total_compras = 0
                        for i in range(len(clientes[dni]["compras"])):
                            total_compras += clientes[dni]["compras"][i]
                        
                        if len(telefonos) == 0:
                            datos += "".rjust(15) + str(total_compras).rjust(20) + "\n"
                        else:
                            for i in range(len(telefonos)):
                                if i == 0:
                                    datos += str(telefonos[i]).rjust(15) + str(total_compras).rjust(20) +"\n"
                                else:
                                    datos += " ".ljust(45) + str(telefonos[i]).rjust(15) +"\n"
                     
                    print(datos)
                    input("Press Enter to continue...")

                if choice == 4:
                    flag02 = False
                    flag0 = True
                    datos = ""
                    print("Exiting to main menu...")
                    input("Press Enter to continue...")

    #Buscar#
    while flag03:
        
        print("Buscar por:\n1) Nombre\n2) Teléfono\n3) Volver al menú principal")
        opcion_busqueda = input("Introduce una opción: ")

        if not opcion_busqueda.isdigit():
            print("Solo números válidos")
            input("Presiona Enter para continuar...")
        else:
            opcion_busqueda = int(opcion_busqueda)
            if opcion_busqueda not in range(1, 4):
                print("Opción fuera de rango")
                input("Presiona Enter para continuar...")
            else:
                if opcion_busqueda == 1:
                    nombre_a_buscar = input("Introduce el nombre (o parte): ").lower()
                    encontrados = []
                    for dni in clientes:
                        nombre_cliente = clientes[dni]["nombre"].lower()
                        indice = 0
                        encontrado = False
                        while indice <= len(nombre_cliente) - len(nombre_a_buscar) and not encontrado:
                            pedazo = ""
                            for j in range(len(nombre_a_buscar)):
                                pedazo += nombre_cliente[indice + j]
                            if pedazo == nombre_a_buscar:
                                encontrados.append(dni)
                                encontrado = True
                            indice += 1

                    if len(encontrados) == 0:
                        print("No se encontraron coincidencias.")
                    else:
                        print("Clientes encontrados:\n")
                        for dni in encontrados:
                            print("DNI:", dni)
                            print("Nombre:", clientes[dni]["nombre"])
                            print("Código:", clientes[dni]["codigo"])
                            print("Teléfonos:")
                            for telefono in clientes[dni]["tfn"]:
                                print("   -", telefono)
                            print("Compras:", clientes[dni]["compras"])
                            print("-" * 40)
                    input("Presiona Enter para continuar...")

                elif opcion_busqueda == 2:
                    telefono_a_buscar = input("Introduce el número de teléfono exacto: ")
                    encontrado = False
                    for dni in clientes:
                        telefonos = clientes[dni]["tfn"]
                        for telefono in telefonos:
                            if telefono == telefono_a_buscar:
                                print("Cliente encontrado:\n")
                                print("DNI:", dni)
                                print("Nombre:", clientes[dni]["nombre"])
                                print("Código:", clientes[dni]["codigo"])
                                print("Teléfonos:")
                                for t in telefonos:
                                    print("   -", t)
                                print("Compras:", clientes[dni]["compras"])
                                print("-" * 40)
                                encontrado = True
                    if not encontrado:
                        print("No se encontró ningún cliente con ese número.")
                    input("Presiona Enter para continuar...")

                elif opcion_busqueda == 3:
                    flag03 = False
                    flag0 = True
                    print("Volviendo al menú principal...")
                    input("Presiona Enter para continuar...")