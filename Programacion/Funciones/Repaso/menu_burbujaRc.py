customers = {
"34343434A":{"name":"Samuel","id":"AF245T","tfn":444444444,"shoppings":[234,43,567]},
"54545454T":{"name":"Samantha","id":"TS846G","tfn":555555555,"shoppings":[1001,34]},
"12344123G":{"name":"Esteban","id":"NT412B","tfn":666666666,"shoppings":[2300,340,34,123]},
"62323455B":{"name":"Ines","id":"UT487A","tfn":123412344,"shoppings":[485,568,682,456,12]},
"81238478S":{"name":"Soraya","id":"TS824V","tfn":939393933,"shoppings":[854]},
"96345245J":{"name":"Cristobal","id":"VN643I","tfn":542342342,"shoppings":[34,645,680]},
"44234423U":{"name":"Amador","id":"KS934W","tfn":636328284,"shoppings":[939,34,145]}
}

def newMenu(titulo,opciones):
    if not len(opciones)>=2:
        raise AssertionError("At least one option is required")
    print(titulo)
    for i in range(len(opciones)):
        print(i+1,")",opciones[i])
    opc_menu=input("Option:")
    if not opc_menu.isdigit():
        raise TypeError("Only numeric option are allowed")
    elif not 1 <= int(opc_menu) <= len(opciones):
        raise ValueError("option out of range")
    else:
        return int(opc_menu)


def keyDictOrdered(aordenar,order="name"):
    lista_aux=[]
    for clave in aordenar.keys():
        lista_aux.append(clave)

    datos = ""
    for i in range(len(lista_aux)-1):
        for j in range(len(lista_aux)-1-i):
            if aordenar[lista_aux[j]][order]>aordenar[lista_aux[j+1]][order]:
                aux=lista_aux[j]
                lista_aux[j]=lista_aux[j+1]
                lista_aux[j+1]=aux

    for i in range(len(lista_aux)):
        suma_ventas = 0
        for total_ventas in range(len(aordenar[lista_aux[i]]["shoppings"])):
            suma_ventas += aordenar[lista_aux[i]]["shoppings"][total_ventas]
        datos += lista_aux[i].ljust(18) + aordenar[lista_aux[i]]["name"].ljust(30) + str(aordenar[lista_aux[i]]["id"]).rjust(5) + str(
            aordenar[lista_aux[i]]["tfn"]).rjust(10) + str(suma_ventas).rjust(15) + "\n"

    return datos



def printClients(listOfKeys):
    datos_ordenado="Customers".center(70,"=")+"\n"+"Nif".ljust(10)+"Name".ljust(15)+"id".ljust(10)+\
    "Tfn".ljust(10)+"Total shoppings".rjust(20)+"\n"+"*"*70+"\n"
    if len(listOfKeys)==0:
        return ValueError("A list of keys is required to print the customers")
    else:
        for clave, items in listOfKeys.items():
            suma_ventas = 0
            for total_ventas in range(len(items["shoppings"])):
                suma_ventas += items["shoppings"][total_ventas]

            datos_ordenado += clave.ljust(10) + items["name"].ljust(15) + str(items["id"]).ljust(10) + str(
                items["tfn"]).ljust(10) + str(suma_ventas).rjust(20) + "\n"
        return datos_ordenado