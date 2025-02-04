# Jugador 1 y jugador 2
# Tirar dos dados cada uno si la suma de ellos es el mayor esto se sumara
# EN caso de empate el que tire primero ganata
import random
# Numero_aleatorio1= random.randrange(0,11,2)
# Numero_aleatorio2= random.randrange(0,11,2)
# Numero_aleatorio3= random.randrange(0,11,2)
# Numero_aleatorio4= random.randrange(0,11,2)
#
# Jugador1 = Numero_aleatorio1 , Numero_aleatorio2
# Jugador2 = Numero_aleatorio3, Numero_aleatorio4
# print(Jugador1)
# print(Jugador2)
# Caezera = "Tirada 1".center(20,"*") + "\n Jugador 1:".ljust(10) + "{}".rjust(10).format(Jugador1)

for i in range(10):
    Numero_aleatorio1 = random.randrange(0, 11, 2)
    Numero_aleatorio2 = random.randrange(0, 11, 2)
    Numero_aleatorio3 = random.randrange(0, 11, 2)
    Numero_aleatorio4 = random.randrange(0, 11, 2)
    Tiradas = 0 + 1

    Jugador1 = Numero_aleatorio1, Numero_aleatorio2
    Jugador2 = Numero_aleatorio3, Numero_aleatorio4
    Caezera = ("Tirada{0}").center(20, "*").format(i) + "\n Jugador 1:".ljust(10) + "{}".rjust(10).format(Jugador1)

    # print("Puntos Jugador 1: {}".format(Jugador1))
    # print("Puntos Jugador 2: {}".format(Jugador2))
    print(Caezera)