# dic = {"Clave1":"Valor1",
#        #2:True,
#        (1,2,3):[4,5,6],
#        False:25,
#        2:"Valor X",
#        34:{"a":1, "b":1}
#        }
# print(dic[2])
# print(dic[34]["a"])
# dic[34]=True
# print(dic[34])
# del(dic[34])
# print(dic)
# dic.clear()
# print(dic)
#
# dic = {"Clave1":"Valor1",
#        #2:True,
#        (1,2,3):[4,5,6],
#        False:25,
#        2:"Valor X",
#        34:{"a":1, "b":1}
#        }
#
# print(len(dic))
# print("Clave1" in dic)
#
# dic2 = dic
# print(dic2)
# dic2[2] = "ALgo"
# print(dic,"\n",dic2)
#
# dic2 = {"x":2}
# dic2.update(dic)
# print(dic2)
# print(dic.get("Valor10","Valor no esta en lista"))
# print(dic.get("Clave1","Valor no esta en lista"))
menu = "Jugadores".center(40,"*")+"\n"+"DNI".ljust(10) + "Nombre".ljust(20) + "Puntos".rjust(10) + "\n"+"*"*40
jugadores = {"11111111L":{"Nombre":"Pedro Martinez","dados":[],"puntos":0},
            "22222222K":{"Nombre":"Pedro Sanchez","dados":[],"puntos":1},
            "33333333S":{"Nombre":"Lola Indigo","dados":[],"puntos":5},
            "44444444L":{"Nombre":"Andres iniesta","dados":[],"puntos":3}}
jugadores2 = list(jugadores.copy())
print(jugadores2)
print(menu)
for players in jugadores:
    nombre =(jugadores[players]["Nombre"])
    puntos =(jugadores[players]["puntos"])
    print(players.ljust(10) + nombre.ljust(20) + str(puntos).rjust(10))


lista_ids_ordenada_puntos = []
for key in jugadores:
    if len(lista_ids_ordenada_puntos) == 0:
        lista_ids_ordenada_puntos.append(key)
    else:
        len_lista_ids_ordenada_puntos = len(lista_ids_ordenada_puntos)
        for i in range(len(lista_ids_ordenada_puntos)):
            if jugadores[key]["puntos"] > jugadores[lista_ids_ordenada_puntos[i]]["puntos"]:
                lista_ids_ordenada_puntos.insert(i,key)
                break
        if len_lista_ids_ordenada_puntos == len(lista_ids_ordenada_puntos):
            lista_ids_ordenada_puntos.append(key)
print(lista_ids_ordenada_puntos)

# for dni in lista_ids_ordenada_puntos:
#      nombre =(lista_ids_ordenada_puntos[dni]["Nombre"])
#      puntos =(lista_ids_ordenada_puntos[dni]["puntos"])
#      print(dni.ljust(10) + nombre.ljust(20) + str(puntos).rjust(10))




