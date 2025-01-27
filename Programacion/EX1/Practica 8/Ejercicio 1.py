# Preguntar quants nombres es van a introduir
while True:
    quants_nombres = int(input("Quants valors va a introduir? "))
    if quants_nombres > 0:
        break
    else:
        print("¡Impossible!")

# Inicialitzar el primer nombre
anterior_nombre = int(input("Escriu un nombre: "))

# Bucle per demanar la resta de nombres
for i in range(1, quants_nombres):
    while True:
        nou_nombre = int(input(f"Escriu un nombre diferent de {anterior_nombre} : "))
        if nou_nombre != anterior_nombre:
            anterior_nombre = nou_nombre
            break
        else:
            print(f"¡ {nou_nombre} no és diferent de {anterior_nombre} !")

print("Gràcies per la seva col·laboració")
