#Cada dia: un predator mata 5 aliens y un humano
#Cada dos dias Cada grupo de 10 aliens mata un humano y generan un nuevo alien
#Cada tres dias cada 10 humanos consigen matar a un alien y cada 1000 aliens matan a un predator
#Cada cuatro dias llega una nave con 500 humanos como refuerzo

import time
Aliens = 10000
Humanos = 10000
Predators = 100
contador = 0

print(Aliens//10)

while True:
    contador += 1
    #Cada dia: un predator mata 5 aliens y un humano
    if contador%1==0:
        Aliens = Aliens - (Predators*5)
    
    #Cada dos dias Cada grupo de 10 aliens mata un humano y generan un nuevo alien
    if contador%2==0:
        Humanos = Humanos - (Aliens//10)
        Aliens = Aliens + (Aliens//10)

    #Cada tres dias cada 10 humanos consigen matar a un alien y cada 1000 aliens matan a un predator
    if contador%3==0:
        Aliens = Aliens - (Humanos//10)
        Predators = Predators - (Aliens//1000)

    #Cada cuatro dias llega una nave con 500 humanos como refuerzo
    if contador%4==0:
        Humanos += 500

    if Aliens < 0:
        Aliens = 0
        Predators = 0
        print("Dia {} --> Humanos = {}, Predators = {}, Aliens = {}".format(contador,Humanos,Predators,Aliens))
        print("Dias Totales = {}".format(contador))
        break
        


    print("Dia {} --> Humanos = {}, Predators = {}, Aliens = {}".format(contador,Humanos,Predators,Aliens))
    input("Enter to continue: ")
    

