correo = input("Dame un correo para verificar si es correcto o no")

for i in range(len(correo)):
    ini = correo.find("@")

    if ini == -1 or ini ==0:
        print("Este correo {} es incorrecto / no valido ".format(correo))
        continue

    usuario = correo[:ini]
    dominio = correo[ini + 1:]

    Valido = True

    for j in range (len(usuario)):
        if not (usuario[j].isalnum() or usuario[j] == "."):
            Valido = False
            break
        if j > 0 and usuario[j] == "." and usuario[i-1] == ".":
            Valido = False
            break

    puntos = 0

    for j in range(len(dominio)):
        if not (dominio[j].isalnum() or dominio[j] == "."):
            Valido = False
            break
        if dominio[j] == ".":
            if j == 0 or j == len(dominio) - 1 or dominio[j - 1] == ".":
                Valido = False
                break
            puntos += 1

    if puntos < 1:
        Valido = False

    print(f"{correo}: {'Válido' if Valido else 'No válido'}")