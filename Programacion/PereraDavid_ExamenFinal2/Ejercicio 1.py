import random
dados_tiradas = [[0,0,0,0],[0,0,0]]
nombre = ""
jugadores = [{"name":nombre,"points":20},{"name":"boot","points":20}]

ranking_risk = {}



meter_usuario =True
juego_en_curso = False

while meter_usuario:
    nombre = input("Dame tu nombre")
    if len(nombre.replace(" ", "")) == 0:
        print("Incorrect length name")
    elif not nombre.replace(" ", "").isalnum():
        print("Only alfanumerical name")
    else:
        jugadores = [{"name": nombre, "points": 20}, {"name": "boot", "points": 20}]
        #print(nombre, jugadores)
        juego_en_curso = True
        meter_usuario = False
while juego_en_curso:
    for i in jugadores:
        jugadores_partida = i["name"]
        print(jugadores_partida)




    juego_en_curso = False