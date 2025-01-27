amplada = int(input("Introdueix l'amplada del rectangle: "))
alcada = int(input("Introdueix l'alçada del rectangle: "))

for i in range(alcada):
    if i == 0 or i == alcada - 1:
        print("*" * amplada)
    else:
        print("*" + " " * (amplada - 2) + "*")
