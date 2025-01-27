# Demanar el primer número
numero = int(input("Escriu un número enter: "))

# Demanar quants números es van a escriure
while True:
    quantitat = int(input("Quants números va a inscriure? "))
    if quantitat > 0:
        break

# Inicialitzar comptadors
comptador_numero = 0
comptador_diferents = 0

# Demanar la quantitat de números
for i in range(quantitat):
    num = int(input("Escriu un número enter: "))
    if num == numero:
        comptador_numero += 1
    else:
        comptador_diferents += 1

# Comparar i mostrar el resultat
if comptador_numero > comptador_diferents:
    print("Ha escrit més vegades el número {} que els altres números.".format(numero))
elif comptador_numero < comptador_diferents:
    print("Ha escrit menys vegades el número {} que la resta de números.".format(numero))
else:
    print("Ha escrit tantes vegades el número {} com la resta de números.".format(numero))

print("Programa terminat")
