def recuperar_contactos_1(nombre_fichero):
    ficherito = open(nombre_fichero, "r", encoding="utf-8")
    agenda = {}  # Diccionario que almacenará todos los contactos
    
    for linea in ficherito:
        linea = linea.replace("\n", "").replace(" ", "")
        campos = linea.split("*")

        dni = ""
        nombre = ""
        apellidos = ""
        tfn = []
        direccion = ""

        for elementos in campos:
            if "nombre:" in elementos:
                nombre = elementos.split(":")[1]
            if "dni:" in elementos:
                dni = elementos.split(":")[1]
            if "apellido:" in elementos:
                apellidos = elementos.split(":")[1]
            if "direccion:" in elementos:
                direccion = elementos.split(":")[1]
            if "tfn:" in elementos:
                telefonos = elementos.split(":")[1]
                tfn = [int(tf) for tf in telefonos.split(",")]

        agenda[dni] = {"nombre": nombre, "apellidos": apellidos, "tfn": tfn, "direccion": direccion}

    ficherito.close()
    
    print("\n📌 **AGENDA FORMATO 1:**")
    print(agenda)

# Prueba con un archivo llamado "Contactos1.txt"
recuperar_contactos_1("Contactos1.txt")



def recuperar_contactos_2(nombre_fichero):
    ficherito = open(nombre_fichero, "r", encoding="utf-8")
    agenda = {}

    for linea in ficherito:
        linea = linea.replace("\n", "").replace(" ", "")
        campos = linea.split("*")

        dni = campos[0]
        nombre = ""
        apellidos = ""
        tfn = []
        direccion = ""

        for campo in campos[1:]:
            if "," in campo and campo.replace(",", "").isdigit():
                # Si contiene comas y solo números → es la lista de teléfonos
                tfn = [int(tf) for tf in campo.split(",")]
            elif any(char.isdigit() for char in campo):
                # Si tiene números → es la dirección
                direccion = campo
            elif nombre == "":
                # Si el nombre está vacío → es el nombre
                nombre = campo
            else:
                # Si no es nombre, ni dirección, ni teléfonos → es el apellido
                apellidos = campo

        agenda[dni] = {"nombre": nombre, "apellidos": apellidos, "tfn": tfn, "direccion": direccion}

    ficherito.close()
    
    # 🔥 Imprimimos la agenda completa
    print("\n📌 **AGENDA FORMATO 2:**")
    print(agenda)

# Prueba con un archivo llamado "Contactos2.txt"
recuperar_contactos_2("Contactos2.txt")



def recuperar_contactos_3(nombre_fichero):
    ficherito = open(nombre_fichero, "r", encoding="utf-8")
    agenda = {}

    for linea in ficherito:
        linea = linea.replace("\n", "").replace(" ", "")
        campos = linea.split("-")
        print(campos)

        dni = ""
        nombre = ""
        apellidos = ""
        tfn = []
        direccion = ""

        for i in range(len(campos)):
            if i == 0:
                dni = campos[i]
                
            elif ";" in campos[i]:  # Nombre y apellido separados por ";"
                partes = campos[i].split(";")
                print(partes)
                nombre = partes[0]
                #print(nombre)
                apellidos = partes[1].split(".")
                #print(apellidos)  # Quitamos el punto del apellido
            elif "-" in campos[i]:  # Teléfonos y dirección separados por "-"
                partes = campos[i].split("-")
                telefonos = partes[0]
                direccion = partes[1]
                tfn.append(telefonos)
            else:
                direccion = campos[i]  # Si no tiene "-", es la dirección

        agenda[dni] = {"nombre": nombre, "apellidos": apellidos, "tfn": tfn, "direccion": direccion}

    ficherito.close()
    
    # 🔥 Imprimimos la agenda completa
    print("\n📌 **AGENDA FORMATO 3:**")
    print(agenda)

# Prueba con un archivo llamado "Contactos3.txt"
recuperar_contactos_3("Contactos3.txt")

