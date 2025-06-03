discografia = "Abbey Road*1969*The Beatles-The Dark Side of the Moon*1973*Pink Floyd-Born to Run*1975*Bruce Springsteen-Hotel California*1976*Eagles-Rumours*1977*Fleetwood Mac-Back in Black*1980*AC/DC-Thriller*1982*Michael Jackson-The Joshua Tree*1987*U2-Nevermind*1991*Nirvana-OK Computer*1997*Radiohead-"

total_discos = discografia.count("-")
#print(total_discos)
inicio = 0
final = 0

menu0 = "1. Mostrar discografía\n2. Añadir disco (Ordenado por año)\n3. Buscar disco\n5. Salir\n"
menu03 = "1. Buscar por disco\n2. Buscar por año\n3. Buscar por grupo\n4. Volver al menú principal\n"

titulo1 = "Discografía".center(60, "*") + "\nDiscos".ljust(30) + "Año".rjust(10) + "Grupo".rjust(20) + "\n" + "*" * 60 + "\n"

#insertar disco ordenado por año
nuevo_disco ="Nuevo Disco"
nuevo_año = "2000"
nuevo_grupo = "Nuevo Grupo"

for i in range(total_discos):
    disco_iesmo = discografia
    if i == 0:
        inicio = 0
        final = discografia.find("-")
        disco_iesmo = discografia[inicio:final]
    else:
        inicio = final + 1
        final = discografia.find("-",inicio)

    asterisco1 = discografia.find("*")
    asterisco2 = discografia.find("*",asterisco1)
    nombre_disco = disco_iesmo[:asterisco1]
    año = disco_iesmo[asterisco1+1:asterisco2]
    grupo = disco_iesmo[asterisco2:]
    if nuevo_año < año:
        cadena_delante = discografia[:inicio]
        cadena_detras = discografia[inicio:]
        print("delante = ", cadena_delante)
        print("atras = ", cadena_detras)