# Bucle per assegurar-nos que la data introduïda és correcta
while True:
    data_naixement = input("Introdueix la teva data de naixement en format ddmmaaaa: ")
    
    if len(data_naixement) == 8 and data_naixement.isdigit():
        break
    else:
        print("La data introduïda no és vàlida. Torna-ho a intentar.")

# Sumar els dígits de la data
suma = 0
for digit in data_naixement:
    suma += int(digit)

# Reduir la suma fins obtenir un sol dígit
while suma >= 10:
    nova_suma = 0
    for digit in str(suma):
        nova_suma += int(digit)
    suma = nova_suma

# Mostrar el número de la sort
print("El teu número de la sort és: {}".format(suma))
