# Solicitar al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Inicializar contadores
contador_vocales = 0
contador_consonantes = 0

# Definir vocales
vocales = "aeiouAEIOU"

# Recorrer cada carácter de la frase
for caracter in frase:
    if caracter.isalpha():  # Comprobar si el carácter es una letra
        if caracter in vocales:  # Comprobar si es una vocal
            contador_vocales += 1
        else:  # Si no es vocal, es consonante
            contador_consonantes += 1

# Imprimir resultados
print("Vocales:", contador_vocales)
print("Consonantes:", contador_consonantes)
