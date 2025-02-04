# Bucle per demanar la grandària del segment
while True:
    m = int(input("Escriu la grandària del segment: "))
    
    while True:
        n = int(input("Escriu el número de segments: "))
        if n > 0:
            break
        else:
            print("¡No ha escrit un número enter positiu!")

    segment = "* " * m
    espai = " " * m
    resultat = ""

    for i in range(n):
        resultat += segment
        if i < n - 1:  # Afegir espai només entre els segments
            resultat += espai

    print(resultat)

