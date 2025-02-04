# Solicitar al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Inicializar variables
palabra = ""
frase_invertida = ""

# Recorrer cada carácter de la frase
for caracter in frase:
    if caracter != " ":  # Si no es un espacio, seguimos formando la palabra
        palabra += caracter
    else:  # Cuando encontramos un espacio, añadimos la palabra a la frase invertida
        frase_invertida = palabra + " " + frase_invertida
        palabra = ""  # Reiniciamos la variable para la siguiente palabra

# Añadir la última palabra si no está vacía
if palabra:
    frase_invertida = palabra + " " + frase_invertida

# Imprimir la frase invertida
print("Frase invertida:", frase_invertida.strip())  # strip() para eliminar el espacio extra al final
