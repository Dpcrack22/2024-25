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
dni_letters = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
abcd=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
menu00="Examen Final UF1".center(40,"*")+"\n1)New Customer\n2)List Customers\n3)Find Customer\n4)Exit"
menu01="Examen Final UF1".center(40,"*")+("\n1)Show clients ordered By NIF\n2)Show clients ordered NUMERIC CODE\n"
                                          "3)Show clients ordered By purchases\n4)Go back")
menu02="Examen Final UF1".center(40,"*")+"\n1)Find By name\n2)Find by Phone Number\n3)Go back"
cabecera="Clientes".center(90,"=")+"\n"+"Nif".ljust(10)+"Nombre".ljust(20)+"Codigo".ljust(15)+"Tfn".rjust(25)+"Total Compras".rjust(20)+"\n"+"*"*90+"\n"


flag00=True
flag01=True
flag011=False
flag012=False
flag013=False

while flag00:
    while flag01:
        opc=input(menu00)
        if not opc.isdigit():
            print("Only numerical option")
        elif not 0<int(opc)<5:
            print("Out of range")
        else:
            if int(opc)==1:
                new_customer={"nombre":"","codigo":"","tfn":[],"compras":[]}
                new_name=True
                new_tlf=True
                new_code=True
                new_dni=True
                flag011=True
                flag01=False
            elif int(opc)==2:
                flag012=True
                flag01=False
            elif int(opc)==3:
                flag01=False
                flag013=True
            else:
                flag01=False
                flag00=False

    while flag011:
        while new_name:
            name=input("Introduce the name: ")
            if len(name.replace(" ",""))==0:
                print("Incorrect length name")
            elif not name.replace(" ","").isalnum():
                print("Only alfanumerical name")
            else:
                new_customer["nombre"]=name
                new_name=False
        while new_dni:
            dni=input("Introduce the dni").upper()
            if not len(dni)==9:
                print("Incorrect length")

            elif not dni[:8].isdigit():
                print("Error de los numeros")
            elif not dni[8:].isalpha():
                print("Erro en la letra")
            else:
                letra_nie = int(dni[:8]) % 23
                letra_seleccionada=dni_letters[letra_nie]

                if not letra_seleccionada == dni[8:]:
                    print("iNCORRECT dni LETTER")
                else:

                    new_dni = False
        while new_tlf:
            opc=input("Do u want to introduce a new tlf? y/n").upper()
            if opc=="Y":
                introducir_tlf=True
                while introducir_tlf:
                    tlf=input("Introduce the tlf: ")
                    if tlf in new_customer["tfn"]:
                        print("PHone number alredy exist")
                    else:
                        if len(tlf)==9 and tlf.isdigit():
                            new_customer["tfn"].append(tlf)
                            introducir_tlf=False
                        elif len(tlf)==14 and tlf[0]=="+" and tlf[1:].isdigit():
                            new_customer["tfn"].append(tlf)
                            introducir_tlf = False
                        else:
                            print("Incoirrect number")
            elif opc=="N":
                new_tlf=False
            else:
                print("Incorrect option")
        while new_code:
            letras=""
            numeros=""
            codigo=""
            while len(letras)<3:
                letras+=abcd[random.randrange(len(abcd))]
            while len(numeros)<4:
                numeros+=str(random.randrange(0,10))
            codigo=letras+numeros
            codigo_duplicado = False
            for llave, cliente in clientes.items():
                if codigo == cliente["codigo"]:
                    codigo_duplicado = True
                    break
            if not codigo_duplicado:
                new_customer["codigo"] = codigo
                guardar=True
                new_code = False
        while guardar:
            datos = "Dni:".ljust(20) + dni.rjust(20) + "\n" + "Nombre".ljust(20) + name.rjust(
                20) + "\n" + "Codigo:".ljust(20) + \
                    codigo.rjust(20) + "\n" + "Telefonos:".ljust(20)
            for i in range(len(new_customer["tfn"])):
                if i == 0:
                    datos += str(new_customer["tfn"][i]).rjust(20)+"\n"
                else:
                    datos += str(new_customer["tfn"][i]).rjust(40)+"\n"
            print(datos)
            opc=input("QUIERES GUARDAR EL PERSONAJE? Y/N").upper()

            if opc=="Y":
                clientes[dni]=new_customer
                flag01=True
                flag011=False
                guardar=False
            elif opc=="N":
                flag01 = True
                flag011 = False
                guardar = False
            else:
                print("Incorrect option")

    while flag012:
        listado=[]
        for llaves in clientes.keys():
            listado.append(llaves)
        opc = input(menu01)
        if not opc.isdigit():
            print("Only numerical option")
        elif not 0 < int(opc) < 5:
            print("Out of range")
        else:
            if int(opc) == 1:
                for i in range(len(listado)-1):
                    for j in range(len(listado)-i-1):
                        if listado[j]>listado[j+1]:
                            aux=listado[j+1]
                            listado[j + 1]=listado[j]
                            listado[j]=aux
                printar = True
            elif int(opc) == 2:
                for i in range(len(listado) - 1):
                    for j in range(len(listado) - i - 1):
                        if clientes[listado[j]]["codigo"][3:] > clientes[listado[j + 1]]["codigo"][3:]:
                            aux = listado[j + 1]
                            listado[j + 1] = listado[j]
                            listado[j] = aux

                printar=True
            elif int(opc) == 3:
                for i in range(len(listado) - 1):
                    for j in range(len(listado) - i - 1):
                        comprasJ=0
                        comprasJ1=0
                        for k in range(len(clientes[listado[j]]["compras"])):
                            comprasJ+=clientes[listado[j]]["compras"][k]
                        for l in range(len(clientes[listado[j+1]]["compras"])):
                            comprasJ1 += clientes[listado[j+1]]["compras"][l]
                        if comprasJ > comprasJ1:
                            aux = listado[j + 1]
                            listado[j + 1] = listado[j]
                            listado[j] = aux
                printar=True
            else:
                flag012 = False
                flag01 = True
        while printar:
            cabecera = "Clientes".center(90, "=") + "\n" + "Nif".ljust(10) + "Nombre".ljust(20) + "Codigo".ljust(
                15) + "Tfn".rjust(25) + "Total Compras".rjust(20) + "\n" + "*" * 90 + "\n"
            for i in range(len(listado)):
                cabecera += listado[i].ljust(10) + clientes[listado[i]]["nombre"].ljust(20) + \
                            clientes[listado[i]]["codigo"].ljust(15)
                total_compras = 0
                for j in range(len(clientes[listado[i]]["compras"])):
                    total_compras += clientes[listado[i]]["compras"][j]
                for k in range(len(clientes[listado[i]]["tfn"])):
                    if k == 0:
                        cabecera += clientes[listado[i]]["tfn"][k].rjust(25) + str(total_compras).rjust(20)
                    else:
                        cabecera += "\n" + clientes[listado[i]]["tfn"][k].rjust(70)
                cabecera += "\n"
            print(cabecera)
            input("Press any key to go back")
            printar=False


    while flag013:
        listado = []
        mostrar=False
        opc=input(menu02)
        if not opc.isdigit():
            print("Only numerical option")
        elif not 0<int(opc)<5:
            print("Out of range")
        else:
            if int(opc)==1:
                searcher=input("Nombre a buscar: ").upper()
                for llave in clientes.keys():
                    if searcher in clientes[llave]["nombre"].upper():
                        listado.append(llave)
                mostrar=True

            elif int(opc)==2:
                searcher=input("Phone to search: ").upper()
                for llave in clientes.keys():
                    for i in range(len(clientes[llave]["tfn"])):
                        if searcher in clientes[llave]["tfn"][i]:
                            listado.append(llave)
                            break
                mostrar=True
            else:
                flag01=True
                flag013=False

        while mostrar:
            cabecera = "Clientes".center(90, "=") + "\n" + "Nif".ljust(10) + "Nombre".ljust(20) + "Codigo".ljust(
                15) + "Tfn".rjust(25) + "Total Compras".rjust(20) + "\n" + "*" * 90 + "\n"
            if len(listado)==0:
                cabecera+="There is not customers with {} in the game".format(searcher)
            else:
                for i in range(len(listado)):
                    cabecera += listado[i].ljust(10) + clientes[listado[i]]["nombre"].ljust(20) +\
                                clientes[listado[i]]["codigo"].ljust(15)
                    total_compras = 0
                    for j in range(len(clientes[listado[i]]["compras"])):
                        total_compras += clientes[listado[i]]["compras"][j]
                    for k in range(len(clientes[listado[i]]["tfn"])):
                        if k == 0:
                            cabecera += clientes[listado[i]]["tfn"][k].rjust(25) + str(total_compras).rjust(20)
                        else:
                            cabecera += "\n" + clientes[listado[i]]["tfn"][k].rjust(70)
                    cabecera += "\n"

            print(cabecera)
            input("Press any key to go back")
            mostrar = False