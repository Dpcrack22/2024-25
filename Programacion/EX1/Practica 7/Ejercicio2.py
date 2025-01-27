# Bucle per assegurar-nos que els números introduïts són positius
while True:
    a = int(input("Introdueix la base (nombre positiu): "))
    b = int(input("Introdueix l'exponent (nombre positiu): "))
    
    if a > 0 and b > 0:
        break
    else:
        print("Tots dos números han de ser positius. Torna-ho a intentar.")

# Calcular a^b amb multiplicacions repetides
resultat = 1

for i in range(b):
    resultat *= a

# Mostrar el resultat
print("El resultat de {} elevat a {} és: {}".format(a, b, resultat))
