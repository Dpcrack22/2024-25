"""
Cada tres dias:
Cada 10 humanos consiguen matar a un alien
Cada 1000 aliens consiguen matar un predators
Cada 4 dias:
Llega una nave con 500 humanos como refuerzo
"""

import time

aliens = 10000
humanos = 10000
predators = 100
segundos = 1

while (aliens > 0 and predators > 0 and humanos > 0):
    print("Dia = {}".format(segundos).center(50,"*"))
    print("Humanos = {} ,Predators = {}, Aliens = {} ".format(humanos,predators,aliens))
    matar_alien1 = predators * 5
    aliens = aliens - matar_alien1
    humanos = humanos - predators

    if segundos % 2 == 0:
        matar_humano1 = aliens // 10
        humanos = humanos - matar_humano1
        aliens = aliens + matar_humano1

    if segundos % 3 == 0:
        matar_alien2 = humanos // 10
        aliens = aliens - matar_alien2
        matar_predator1 = aliens // 1000
        predators = predators -matar_predator1

    if segundos % 4 == 0:
        humanos = humanos + 500














    time.sleep(1)
    segundos += 1