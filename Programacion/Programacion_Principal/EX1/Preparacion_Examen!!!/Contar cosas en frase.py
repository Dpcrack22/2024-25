# Solicitar al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Inicializar contadores
contador_letras = 0
contador_espacios = 0

# Recorrer cada carácter de la frase
for caracter in frase:
    if caracter.isalpha():  # Comprobar si el carácter es una letra
        contador_letras += 1
    elif caracter == " ":  # Comprobar si el carácter es un espacio
        contador_espacios += 1

# Imprimir resultados
print("Letras:", contador_letras)
print("Espacios:", contador_espacios)
