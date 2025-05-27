#Tenemos un juego con un a cadena de bots = bot25,bot38,bot27,bot10 luego escojer uno aleatorio
#Usuario
#Empieza tirando aleatoriamente cada ronda
#Cada uno tira un dados
#En cada ronda quiere que salga un mensajito que es Dado botx /n dado usuario y /n y mensaje de quien gana puntos
import random

#Generar cadena de bots

Bots = ""

for i in range(5):
    numero = random.randrange(1,50)
    while str(numero) in Bots:
        numero = random.randrange(1,50)

    Bots += "Bot{};".format(str(numero))
Bots = Bots[:-1]
print(Bots)


#Escojer bot alearotio


total_bors = Bots.count(";")
inicio = 0
final = 0

num_boot_aleatorio = random.randrange(1,total_bors+2)
bot_aleatorio = ""

for i in range(num_boot_aleatorio):
    bot_iesmo = Bots
    if i == 0:
        inicio = 0
        final = Bots.find(";")
        bot_iesmo = Bots[inicio:final]
    else:
        if i == total_bors + 1:
            inicio = final + 1
            final = len(Bots)
        else:
            inicio = final + 1
            final = Bots.find("-",inicio)
        bot_iesmo = Bots[inicio:final]
    boot_aleatorio = bot_iesmo
print("Bot_iesimo = ",bot_iesmo)


tirada = 1
usuario = input("Inserte usuario: ")
puntos_bot = 0
puntos_usuario = 0
dado_usuario = 0
dado_bot = 0

while puntos_bot < 50 and puntos_usuario < 50:
    cadena = "Tirada " + str(tirada).center(30,"*")

    print(("Tirada " + str(tirada)).center(30,"*"))

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    orden_tirada = random.randrange(1,3)


    if orden_tirada == 0:
        cadena += "Dado usuario = " + str(dado1) + "Puntos Usuario =" +str(puntos_usuario) + "\n"
        cadena += "Dado boot = " + str(dado2) + "Puntos Usuario =" +str(puntos_bot) + "\n"
    else:
        cadena += "Dado boot = " + str(dado1) + "Puntos Usuario =" +str(puntos_bot) + "\n"
        cadena += "Dado usuario = " + str(dado2) + "Puntos Usuario =" +str(puntos_usuario) + "\n"

    if dado2 == dado1:
        #alguien gana puntos
        cadena += "Coincide SI"
        if orden_tirada == 1:
            #usuario ha tirado primero
            puntos_usuario += (dado2+dado1)
            cadena += "Usuario Gana = "+str(dado1 + dado2)
        else:
            puntos_bot += (dado1+dado2)
            cadena += "Bot Gana = "+str(dado2 + dado1)

    else:
        cadena += "Coincide NO" +"\n"

print(cadena)




