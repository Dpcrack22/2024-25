ranking_risk={"11111111L":{"games":0,"points":20},
              "22222222K":{"games":0,"points":20},
              "33333333S":{"games":0,"points":20},
              "44444444L":{"games":0,"points":20}
              }


base_jugadores = {"11111111L": "Pedro Martinez", "22222222K": "Pedro Sanchez", "33333333S": "Lola Indigo",
                  "44444444L": "Andres iniesta"}
cabecera="RRankingRisk".center(40,"*")+"\n"+"Nombre".ljust(20)+"Games".rjust(10)+"Puntos".rjust(10)+"\n"+"*"*40
puntos_ordenados=[]
games_ordenados=[]
flg_00 = True
flg_01 = False
flg_02 = False
flg_03 = False





for key in ranking_risk:
    if len(games_ordenados)==0:
        games_ordenados.append(key)
    else:
        len_lista=len(games_ordenados)
        for i in range(len(games_ordenados)):
            if ranking_risk[key][("games")]>ranking_risk[games_ordenados[i]]["games"]:
                games_ordenados.insert(i,key)
                break
        if len_lista==len(games_ordenados):
            games_ordenados.append(key)

for key in ranking_risk:
    if len(puntos_ordenados)==0:
        puntos_ordenados.append(key)
    else:
        len_lista=len(puntos_ordenados)
        for i in range(len(puntos_ordenados)):
            if ranking_risk[key][("points")]>ranking_risk[puntos_ordenados[i]]["points"]:
                puntos_ordenados.insert(i,key)
                break
        if len_lista==len(puntos_ordenados):
            puntos_ordenados.append(key)
print("Ordenaod por juegos")
print(cabecera)
for i in range(len(games_ordenados)):
    nombre=base_jugadores[games_ordenados[i]]
    games=ranking_risk[games_ordenados[i]]["games"]
    points=ranking_risk[games_ordenados[i]]["points"]
    print(nombre.ljust(20)+str(games).rjust(10)+str(points).rjust(10))
print("*****************************************")
print("Ordenaod por puntos")

print(cabecera)
for i in range(len(puntos_ordenados)):
    nombre=base_jugadores[puntos_ordenados[i]]
    games=ranking_risk[puntos_ordenados[i]]["games"]
    points=ranking_risk[puntos_ordenados[i]]["points"]
    print(nombre.ljust(20)+str(games).rjust(10)+str(points).rjust(10))