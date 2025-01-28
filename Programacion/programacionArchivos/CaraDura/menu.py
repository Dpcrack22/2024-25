# import os.path
#
# def read_file(nombre_fichero):
#     fichero = nombre_fichero
#     resultado =[]
#     linea = open(fichero, "r")
#     for lineas in fichero:
#         id = lineas[0:7]
#         nombre = lineas[7:39]
#         direccion = lineas[39:69]
#         pais = lineas[69:]
#         diccionario = {}
#         diccionario["id"] = id
#         diccionario["nombre"] = nombre
#         diccionario["direccion"] = direccion
#         diccionario["pais"] = pais
#         resultado.append(diccionario)
#     fichero.close()
#     return resultado
#
# lista_contactos = read_file("Cara") + read_file("Dura")
# print(lista_contactos)
#
# def ordenar_contactos(lista_contactos):
#     print()
#     for passadas in range(len(lista_contactos)-1):
#         for i in range(len(lista_contactos)-1-passadas):
#             if lista_contactos[i]["nombre"] > lista_contactos[i+1]["nombre"]:
#                 aux = lista_contactos[i]
#                 lista_contactos[i] = lista_contactos[i+1]
#                 lista_contactos[i+1] = aux
#                 #lista_contactos[i]["nombre"] > lista_contactos[i+1]["nombre"]
#
# ordenar_contactos(lista_contactos)
# for diccionario in lista_contactos:
#     print(diccionario["nombre"])
#
#
# def guardar_contacto(nombre_fichero, lista):
#     fichero = open(nombre_fichero, "a")
#     for contacto in lista:
#         linea = contacto["id"] + contacto["nombre"] + contacto["direccion"] + contacto["pais"] + "\n"
#         fichero.write(linea)
#     fichero.close()
# guardar_contacto("Clientes", )

contactos = {}
def read_file(nombre_fichero):
    ficherito = open(nombre_fichero, "r")
    for linea in ficherito:
        contactos[linea[0:7]] = {"nombre":linea[7:39],"direccion":linea[39:69], "pais":linea[69:]}
    ficherito.close()

read_file("Cara")
read_file("Dura")

def devuelebe_ids_ordenado():
    lista_ids = list(contactos.keys())
    for passadas in range(len(lista_ids)-1):
        for i in range(len(lista_ids)-1-passadas):
            if contactos[lista_ids][i]["nombre"].lower() > contactos[lista_ids][i+1]["nombre"].lower():
                aux = lista_ids[i]
                lista_ids[i] = lista_ids[i+1]
                lista_ids[i+1] = aux
    return lista_ids
lista_ids_ordenados = devuelebe_ids_ordenado()
print(devuelebe_ids_ordenado())

def guardar_contacto(nombre_fichero, lista):
    fichero = open(nombre_fichero, "a")
    for id in lista:
        linea = id + contactos[id]["nombre"] + contactos[id]["direccion"] + contactos[id]["pais"] + "\n"
        fichero.write(linea)
    fichero.close()
guardar_contacto("Clientes", lista_ids_ordenados)