ranking_risk={"12111111L":{"games":0,"points":20},
              "11222222K":{"games":0,"points":20},
              "44444444L":{"games":0,"points":20},
              "22222222K":{"games":0,"points":20}
              }
base_jugadores = {"11111111L": "Pedro Martinez", "22222222K": "Pedro Sanchez", "33333333S": "Lola Indigo",
                  "44444444L": "Andres iniesta"}

dnis = list(ranking_risk.keys())

# print(dnis)
# for pasadas in range(len(dnis)-1):
#     for i in range(len(dnis) - 1 - pasadas):
#         #comparaciones += 1
#         if dnis[i] > dnis[i + 1]:
#             aux = dnis[i]
#             dnis[i] = dnis[i + 1]
#             dnis[i + 1] = aux
# print(dnis)

for pasadas in range(len(lista_dnis)-1):
