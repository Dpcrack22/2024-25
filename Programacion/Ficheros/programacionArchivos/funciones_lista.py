import os.path
letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']


def recuperar_contactos(nombre_fichero):
    ficherito = open(nombre_fichero)
    for linea in ficherito:
        agenda = {}
        #print(linea)
        #print("*")
        linea = linea.replace("\n","")
        linea = linea.replace(" ","")
        Campos = linea.split("*")
        #print(Campos)
        #print("**")
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
    while True:
        dni = input("Dame tu dni:\n")
        if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
            numero = int(dni[:-1])
            letra_Correcta = letrasDni[numero % 23]
            if dni[-1].upper() == letra_Correcta:
                print("DNI Correcto")
                break
            else:
                print("DNI invalido: letra incorrecta")
        else:
            print("DNI invalido debe contener 8 digitos")
    nombre = input("Dame tu nombre:\n")
    apellido = input("Dame tu apellido:\n")
    direccion = input("Dame tu direccion:\n")
    tfn = (input("Dame tu numero:\n"))
    opc = input("Quieres aÃ±adir otro numero?\n (S/N): ").upper()
    if opc == "s".upper():
        tfn2 = input("Añade otro numero")
        tfn = tfn + "," + tfn2
    elif opc == "n".upper():
        print("De acuerdo...")
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
        ficherito.write(linea)
    ficherito.close()





def buscar_contacto(nombre_fichero, criterio, valor):
    ficherito = open(nombre_fichero, "r")
    encontrados = []

    for linea in ficherito:
        linea = linea.replace("\n", "").replace(" ", "")
        campos = linea.split("*")

        contacto = {}
        for campo in campos:
            if "dni" in campo:
                contacto["dni"] = campo.split(":")[1]
            elif "nombre" in campo:
                contacto["nombre"] = campo.split(":")[1]
            elif "apellido" in campo:
                contacto["apellido"] = campo.split(":")[1]
            elif "direccion" in campo:
                contacto["direccion"] = campo.split(":")[1]
            elif "tfn" in campo:
                contacto["tfn"] = campo.split(":")[1].split(",")

        try:
            if criterio == "nombre" and valor.lower() in contacto["nombre"].lower():
                encontrados.append(contacto)
            elif criterio == "dni" and valor.lower() == contacto["dni"].lower():
                encontrados.append(contacto)
            elif criterio == "tfn":
                for tfn in contacto["tfn"]:
                    if valor in tfn:
                        encontrados.append(contacto)
                        break
        except KeyError:
            pass

    ficherito.close()

    if encontrados:
        for contacto in encontrados:
            telefono_str = ""
            for tfn in contacto["tfn"]:
                telefono_str += tfn + " "

            print(f"Contacto encontrado: DNI: {contacto['dni']} | Nombre: {contacto['nombre']} | Apellido: {contacto['apellido']} | Teléfonos: {telefono_str}Dirección: {contacto['direccion']}")
    else:
        print("No se encontraron contactos con ese criterio.")



def listar_contactos(nombre_fichero, criterio):
    ficherito = open(nombre_fichero)
    agenda = {}

    for linea in ficherito:
        linea = linea.replace("\n", "")
        linea = linea.replace(" ", "")
        Campos = linea.split("*")

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

        nuevo_contacto = {"nombre": nombre, "apellidos": apellidos, "tfn": tfn, "direccion": direccion}
        agenda[dni] = nuevo_contacto

    dnis = list(agenda.keys())
    for i in range(len(dnis) - 1):
        cambio = False
        for j in range(len(dnis) - (i + 1)):
            if agenda[dnis[j + 1]]["nombre"] > agenda[dnis[j]]["nombre"]:
                cambio = True
                aux = dnis[j + 1]
                dnis[j + 1] = dnis[j]
                dnis[j] = aux
        if not cambio:
            break

    # Mostrar ranking ordenado por puntos
    print("Ordenado por puntos")
    datos = ""
    for dni in range(len(dnis)):
        datos += dnis[dni].ljust(10) + str(dnis[dni]).ljust(20)
        #datos += agenda[dnis][dni]["nombre"].rjust(10)
        #datos += str(dnis[dni]["apellidos"]).rjust(10) + "\n"

        print(datos)
    ficherito.close()
listar_contactos("Contactos", "nombre")