jugadores = {"TS1":{"nombre":"Pedro", "apellidos":"Gutierrez Salnmeron","dados":[10,10,10],"puntos":150},
            "SU2":{"nombre":"Pablo", "apellidos":"Almansa Pacheco","dados":[8,8,8],"puntos":50},
            "VT3":{"nombre":"Sofia", "apellidos":"Lopez Ruiz","dados":[0,0,0],"puntos":80},
            "FU2":{"nombre":"Ester", "apellidos":"Rovira Cabrera","dados":[3,3,3],"puntos":20},
            "GR4":{"nombre":"Manuela", "apellidos":"Gonzalez Renato","dados":[3,3,2],"puntos":30},
            "PG5":{"nombre":"Roberto", "apellidos":"Rovira Prieto","dados":[7,7,7],"puntos":10} }

# def ordenarDic(Diccionario,Parametro1,Parametro2,Parametro3,Parametro4,ParametroOrdenaccion):
#     auxiliar = []
#     for key_id, valor_info in Diccionario.items():
#         auxiliar.append([key_id, valor_info])
#     if ParametroOrdenaccion == "codigo":
#         for pasadas in range(len(auxiliar) - 1):
#             for i in range(len(auxiliar) - pasadas - 1):
#                 if auxiliar[i][0] > auxiliar[i + 1][0]:
#                     aux = auxiliar[i]
#                     auxiliar[i] = auxiliar[i + 1]
#                     auxiliar[i + 1] = aux
#
#         for i in range(len(auxiliar)):
#             print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1][Parametro1].ljust(20) + str(auxiliar[i][1][Parametro2]).rjust(
#                 10) + str(auxiliar[i][1][Parametro3]).rjust(10) + str(auxiliar[i][1][Parametro4]).rjust(20))
#     elif ParametroOrdenaccion == "nombre":
#         for pasadas in range(len(auxiliar) - 1):
#             for i in range(len(auxiliar) - pasadas - 1):
#                 if auxiliar[i][1][Parametro1] > auxiliar[i + 1][1][Parametro1]:
#                     aux = auxiliar[i]
#                     auxiliar[i] = auxiliar[i + 1]
#                     auxiliar[i + 1] = aux
#
#         for i in range(len(auxiliar)):
#             print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1][Parametro1].ljust(20) + str(auxiliar[i][1][Parametro2]).rjust(
#                 10) + str(auxiliar[i][1][Parametro3]).rjust(10) + str(auxiliar[i][1][Parametro4]).rjust(20))
#     elif ParametroOrdenaccion == "apellidos":
#         for pasadas in range(len(auxiliar) - 1):
#             for i in range(len(auxiliar) - pasadas - 1):
#                 if auxiliar[i][1][Parametro2] > auxiliar[i + 1][1][Parametro2]:
#                     aux = auxiliar[i]
#                     auxiliar[i] = auxiliar[i + 1]
#                     auxiliar[i + 1] = aux
#
#         for i in range(len(auxiliar)):
#             print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1][Parametro1].ljust(20) + str(auxiliar[i][1][Parametro2]).rjust(
#                 10) + str(auxiliar[i][1][Parametro3]).rjust(10) + str(auxiliar[i][1][Parametro4]).rjust(20))
#
#     elif ParametroOrdenaccion == "dados":
#         for pasadas in range(len(auxiliar) - 1):
#             for i in range(len(auxiliar) - pasadas - 1):
#                 if auxiliar[i][1][Parametro3] > auxiliar[i + 1][1][Parametro3]:
#                     aux = auxiliar[i]
#                     auxiliar[i] = auxiliar[i + 1]
#                     auxiliar[i + 1] = aux
#
#         for i in range(len(auxiliar)):
#             print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1][Parametro1].ljust(20) + str(auxiliar[i][1][Parametro2]).rjust(
#                 10) + str(auxiliar[i][1][Parametro3]).rjust(10) + str(auxiliar[i][1][Parametro4]).rjust(20))
#
#     elif ParametroOrdenaccion == "puntos":
#         for pasadas in range(len(auxiliar) - 1):
#             for i in range(len(auxiliar) - pasadas - 1):
#                 if auxiliar[i][1][Parametro4] > auxiliar[i + 1][1][Parametro4]:
#                     aux = auxiliar[i]
#                     auxiliar[i] = auxiliar[i + 1]
#                     auxiliar[i + 1] = aux
#
#         for i in range(len(auxiliar)):
#             print(str(auxiliar[i][0]).ljust(10) + auxiliar[i][1][Parametro1].ljust(20) + str(auxiliar[i][1][Parametro2]).rjust(
#                 10) + str(auxiliar[i][1][Parametro3]).rjust(10) + str(auxiliar[i][1][Parametro4]).rjust(20))
#
# OrdenarPor = str(input("Por que quieres ordenar: ")).lower()
# ordenarDic(jugadores,"nombre","apellidos","dados", "puntos", OrdenarPor)

def ordenadiccionario(diccionario,criterio="",orden="asc"):
    claves = list(diccionario.keys())
    if criterio == "":
        for pasadas in range(len(claves)-1):
            cambios = False
            for i in range(len(claves)-1-pasadas):
                if orden == "asc":
                    if claves[i] > claves[i+1]:
                        cambios = True
                        aux = claves[i]
                        claves[i] = claves[i+1]
                        claves[i+1] = aux

                    else:
                        if claves[i] < claves[i + 1]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
            if not cambios:
                return claves

    else:
        #if type(diccionario[claves[0]][criterio]) == int or type(diccionario[claves[0]][criterio]) == float or type(diccionario[claves[0]][criterio]) == str:
        if type(diccionario[claves[0]][criterio]) in ( int, float, str):
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    if orden == "asc":
                        if diccionario[claves[i]][criterio] > diccionario[claves[i+1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux

                        else:
                            if claves[i] < claves[i + 1]:
                                cambios = True
                                aux = claves[i]
                                claves[i] = claves[i + 1]
                                claves[i + 1] = aux
                if not cambios:
                    return claves
        else:
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    sumai = 0
                    sumai1 = 0
                    for num in diccionario[claves[i]][criterio]:
                        sumai += num
                    for num in diccionario[claves[i+1]][criterio]:
                        sumai1 += num
                    if orden == "asc":
                        if sumai > sumai1:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux

                    else:
                        if sumai < sumai1:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                if not cambios:
                    return claves
    return claves

print(ordenadiccionario(jugadores,criterio="dados"))





def ordenadiccionario(diccionario, criterio="", orden="asc"):
    claves = list(diccionario.keys())
    if criterio == "":
        for pasadas in range(len(claves)-1):
            cambios = False
            for i in range(len(claves)-1-pasadas):
                if orden == "asc":
                    if claves[i] > claves[i+1]:
                        cambios = True
                        aux = claves[i]
                        claves[i] = claves[i+1]
                        claves[i+1] = aux
                else:
                    if claves[i] < claves[i + 1]:  # Esto es correcto para orden descendente por clave
                        cambios = True
                        aux = claves[i]
                        claves[i] = claves[i + 1]
                        claves[i + 1] = aux
            if not cambios:
                return claves
    else:
        if type(diccionario[claves[0]][criterio]) in (int, float, str):
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    if orden == "asc":
                        if diccionario[claves[i]][criterio] > diccionario[claves[i+1]][criterio]:
                            cambios = True
                            aux = claves[i]  # Intercambiar claves, no valores
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                    else:
                        if diccionario[claves[i]][criterio] < diccionario[claves[i + 1]][criterio]:  # Comparar por criterio
                            cambios = True
                            aux = claves[i]  # Intercambiar claves, no valores
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                if not cambios:
                    return claves
        else:
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    sumai = 0
                    sumai1 = 0
                    for num in diccionario[claves[i]][criterio]:  # Acceso correcto a los valores
                        sumai += num
                    for num in diccionario[claves[i+1]][criterio]:  # Acceso correcto a los valores
                        sumai1 += num
                    if orden == "asc":
                        if sumai > sumai1:
                            cambios = True
                            aux = claves[i]  # Intercambiar claves, no valores
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                    else:
                        if sumai < sumai1:
                            cambios = True
                            aux = claves[i]  # Intercambiar claves, no valores
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                if not cambios:
                    return claves
    return claves