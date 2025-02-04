#Cabecera
import random
menu="The Best Game In The World".center(40,"=") + "\n" + "1)New Game" + "\n" + "2)New Player" + "\n" + "3)Show Ranking" + "\n" + "4)Sortir" + "\n" + "Selecciona una opcion: "
llista = "Ranking".center(40,"=") + "\n" + "Nombre".ljust(30) + "Puntos".rjust(10) + "\n" +"*"*40 + "\n"

name_check = False
flag000 = True
flag001 = True
flag002 = False
flag003 = False
flag004 = False
NombresJugador = ""
PuntosDados = 0
PuntosDados2 = 0
PuntosDadosBot = 0
PuntosDadosBot2 = 0
TotalJugador1 = 0
TotalBot = 0
while flag000:
    while flag001:
        opc = input(menu)
        if not opc.isdigit():
            print("Esto no es un numero")
        elif not 0< int(opc) <5:
            print("Opcion fuera de rango")
        else:
            opc = int(opc)
            if opc == 1 and name_check==True:
                 flag001 = False
                 flag002 = True
            elif opc == 2:
                flag001 = False
                flag003 = True
            elif opc == 3:
                flag001 = False
                flag004 = True
            elif opc == 4:
                flag000 = False
                flag001 = False
            else:
                print("Pon un nombre")


    while flag002:
        for i in range(3):
            print("Turno {}".format(i+1).center(40,"*"))
            turno = random.randrange(2)
            if turno == 0:
                PuntosDados = random.randrange(7)
                PuntosDados2 = random.randrange(7)
                PuntosDadosBot = random.randrange(7)
                PuntosDadosBot2 = random.randrange(7)
                if (PuntosDados + PuntosDados2) % 2 == 0:
                    TotalJugador1 = PuntosDados + PuntosDados2 + TotalJugador1
                elif not (PuntosDados + PuntosDados2) % 2 == 0:
                    TotalJugador1 = (PuntosDados - PuntosDados2) + TotalJugador1
                elif (PuntosDadosBot + PuntosDadosBot2) % 2 == 0:
                    TotalBot = PuntosDadosBot + PuntosDadosBot2 + TotalBot
                elif not (PuntosDadosBot + PuntosDadosBot2) % 2 == 0:
                    TotalBot = (PuntosDadosBot - PuntosDadosBot2) + TotalBot
                print("Puntos Totales Bot = {}, Puntos de {} = {}".format(TotalBot, NombresJugador, TotalJugador1))


                # TotalJugador1 = PuntosDados +  TotalJugador1
                # TotalBot = PuntosDados1 +  TotalBot



    while flag003:
        NombresJugador = input("Dame un nombre: ")
        name_check = True
        flag003 = False
        flag001 = True

    while flag004:
        print(llista + "\n")
        input("Presiona enter para continuar: ")