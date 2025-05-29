agenda = {}
def recuperar_contactos(nombre_fichero):
    ficherito = open(nombre_fichero)
    for linea in ficherito:
        #print(linea)
        linea = linea.replace("\n","")
        Campos = linea.split(",")
        #print(Campos)
        dni = ""
        name = ""
        apellidos = ""
        shopping = []
        totalShp = 0
        for elementos in Campos:
            if "surname" in elementos:
                elementos = elementos.replace(" ", "")
                apellidos = elementos.split(":")[1]
            if " name" in elementos:
                name = elementos.split(":")[1]
            if "nif" in elementos:
                elementos = elementos.replace(" ", "")
                dni = elementos.split(":")[1]
            if "shoppings" in elementos:
                elementos = elementos.replace(" ", "")
                shoppings = elementos.split(":")[1]
                for shp in shoppings.split("-"):
                    shopping.append(int(shp))
                for i in shopping:
                    totalShp += i


        nuevo_contacto = {"nombre":name, "apellidos":apellidos, "shoppings":shopping, "TotalShoping":totalShp}
        agenda[dni] = nuevo_contacto

    ficherito.close()

recuperar_contactos("fichero.txt")
print(agenda)