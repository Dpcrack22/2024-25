# Lista con todos los correos en una sola variable
correos = [
    "a@b.com", "a.b@c.com", "a.b@c.d.es",
    ".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com",
    "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com", "awer@wer.com",
    "awer@wer.commmm", "..@wer.commmm"
]

print("Resultado de la validacion de correos: ")
for correo in correos:
    ini = correo.find("@")

    if ini == -1 or ini == 0:
        print("{} Este es incorrecto / no valido".format(correo))
        continue

    usuario = correo[:ini]
    dominio = correo[ini + 1:]

    Valido = True
    for i in range(len(usuario)):
        if not (usuario[i].isalnum() or usuario[i] == "."):
            Valido = False
            break
        if i > 0 and usuario[i] == "." and usuario[i - 1] == ".":
            Valido = False
            break

    puntos = 0
    for i in range (len(dominio)):
        if not (dominio[i].isalnum() or dominio[i] == "."):
            Valido = False
            break
        if dominio[i] == ".":
            if i == 0 or i == len(dominio) - 1 or dominio[i-1] == ".":
                Valido = False
                break
            puntos += 1
        elif i == dominio.count(".") -1 and (len(dominio[ini:]) < 2 or len(dominio[ini:]) >3):
            Valido = False


    if puntos < 1:
        Valido = False

    print(f"{correo}: {'Válido' if Valido else 'No válido'}")
