quants_numeros = int(input("Quants números vols introduir? "))
comptador_negatius = 0

for i in range(quants_numeros):
    num = int(input("Introdueix el número {}: ".format(i + 1)))
    if num < 0:
        comptador_negatius += 1

print("Has introduït {} números negatius.".format(comptador_negatius))
