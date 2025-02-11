import os.path

agenda = {}
def recuperar_contactos(nombre_fichero):
    ficherito = open(nombre_fichero)
    for linea in ficherito:
        #print(linea)
        linea = linea.replace("\n","")
        Campos = linea.split("*")
        #print(Campos)
        dni = ""
        nombre = ""
        apellidos = ""
        tfn = []
        direccion = ""
        for elementos in Campos:
            if "nombre" in elementos:
                elementos = elementos.replace(" ", "")
                nombre = elementos.split(":")[1]
            if "dni" in elementos:
                elementos = elementos.replace(" ", "")
                dni = elementos.split(":")[1]
            if "apellido" in elementos:
                elementos = elementos.replace(" ", "")
                apellidos = elementos.split(":")[1]
            if "direccion" in elementos:

                direccion = elementos.split(":")[1]
            if "tfn" in elementos:
                elementos = elementos.replace(" ", "")
                telefonos = elementos.split(":")[1]
                for tf in telefonos.split(","):
                    tfn.append(int(tf))


        nuevo_contacto = {"nombre":nombre, "apellidos":apellidos, "tfn":tfn, "direccion":direccion}
        agenda[dni] = nuevo_contacto
        print(agenda)



    ficherito.close()

recuperar_contactos("Contactos")



def guardar_contacto(nombre_fichero):
    ficherito = open(nombre_fichero,"a+")
    dni = input("Dame tu dni:\n")
    nombre = input("Dame tu nombre:\n")
    apellido = input("Dame tu apellido:\n")
    direccion = input("Dame tu direccion:\n")
    tfn = list(input("Dame tu numero:\n"))
    opc = input("Quieres añadir otro numero?\n (S/N): ")
    if opc == "s".upper():
        print("")
    elif opc == "n".upper():
        print("De acuerdo:")
    else:
        print("Responda con S o N porfavor")

    agenda = {dni:{"nombre":nombre, "apellidos":apellido, "tfn":[tfn], "direccion":direccion}}
    for dni in agenda:
        linea = "\n"
        linea += "dni" + ":" + dni + "*"
        linea += "nombre" + ":" + agenda[dni]["nombre"] + "*"
        linea += "apellidos" + ":" + agenda[dni]["apellidos"] + "*"
        linea += "direccion" + ":" + agenda[dni]["direccion"] + "*"
        linea += "tfn:"
        for tfn in agenda[dni]["tfn"]:
            linea += str(tfn) + ","
        linea = linea[:-1]
        linea += "\n"
        ficherito.write(linea)
    ficherito.close()





