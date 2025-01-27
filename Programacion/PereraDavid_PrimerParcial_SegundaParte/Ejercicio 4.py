Nombre = "David"
Apellido = "Perera Gonzalez"
horas_semanales = 15

while True:
    if horas_semanales > 9:
        print("Hola soy {} {} he dedicado {} horas y creo que no son suficientes".format(Nombre,Apellido,horas_semanales))
        break
    elif horas_semanales > 15 and horas_semanales < 25:
        print("Hola soy {} {} he dedicado {} horas y creo que son suficientes".format(Nombre,Apellido,horas_semanales))
        break