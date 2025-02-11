import os.path
# Exercici 1.
# Escriure un programa, que rebi un arxiu i un nombre N i imprimeixi les primeres N línies de l'arxiu. 
def imprimir_n_lineas(nombre_archivo, n):
    try:
        archivo = open(nombre_archivo, "r")
        i = 0  # Inicializamos un contador manual
        for linea in archivo:
            if i >= n:
                break
            print(linea, end="")
            i += 1  # Incrementamos el contador
        archivo.close()  # Cerramos el archivo después de leerlo
    except FileNotFoundError:
        print("Error: No se encontró el archivo '{}'.".format(nombre_archivo))
    except ValueError:
        print("Error: N debe ser un número entero positivo.")
    except Exception as e:
        print("Ocurrió un error inesperado: {}".format(e))

# nombre_archivo = input("Introduce el nombre del archivo: ")
# n = int(input("Introduce el número de líneas a imprimir: "))


# Exercici 2.
# Escriure un programa que copiï tot el contingut d'un arxiu (sigui de text o binari) a un altre, de manera que quedi exactament igual.
# Nota: Utilitzar la funció read(Numbytes) per llegir com a màxim una quantitat de bytes. 
def copiar_arxiu(origen, desti, num_bytes=1024):
    try:
        archivo_origen = open(origen, "rb")
        archivo_desti = open(desti, "wb")
        while True:
            bloque = archivo_origen.read(num_bytes)
            if not bloque:
                break
            archivo_desti.write(bloque)
        print("El archivo '{}' se ha copiado correctamente a '{}'.".format(origen, desti))
    except FileNotFoundError:
        print("Error: No se encontró el archivo '{}'.",format(origen))
    except Exception as e:
        print("Ocurrió un error inesperado: {}".format(e))

# origen = input("Introduce el nombre del archivo de origen: ")
# desti = input("Introduce el nombre del archivo de destino: ")

# Exercici 3.
# Escriure un programa que donat un arxiu de text, un delimitador, i una llista de
# camps, imprimeixi solament aquests camps, separats per aquest delimitador. 
def imprimir_campos_contactos(nombre_archivo, delimitador, campos):
    try:
        archivo = open(nombre_archivo, "r")
        for linea in archivo:
            # Dividir la línea usando el delimitador "*"
            parts = linea.split(delimitador)
            
            # Para cada campo que queremos imprimir
            selected_fields = []
            for campo in campos:
                # Buscar el campo solicitado en cada "part" y añadirlo a la lista
                for part in parts:
                    if campo in part:  # Si el campo está en la parte, lo agregamos
                        selected_fields.append(part.strip())  # Añadir campo limpio

            # Imprimir los campos seleccionados
            for i, field in enumerate(selected_fields):
                if i > 0:
                    print(" *", end="")  # Añadir el delimitador entre campos
                print(field, end="")
            print()  # Nueva línea al final de cada conjunto de campos seleccionados

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# nombre_archivo = input("Introduce el nombre del archivo: ")
# delimitador = " *"
# campos = input("Introduce los campos (por ejemplo, dni nombre tfn): ").split()


# Exercici 4.
# Escriure un programa que rebi un arxiu, ho llegeixi i imprimeixi per pantalla
# quantes línies, quantes paraules i quants caràcters conté l'arxiu. 
def contar_lineas_palabras_caracteres(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r")
        num_lineas = 0
        num_palabras = 0
        num_caracteres = 0
        
        for linea in archivo:
            num_lineas += 1
            num_caracteres += len(linea)  
            num_palabras += len(linea.split()) 

        print(f"Líneas: {num_lineas}")
        print(f"Palabras: {num_palabras}")
        print(f"Caracteres: {num_caracteres}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# nombre_archivo = input("Introduce el nombre del archivo: ")
# contar_lineas_palabras_caracteres(nombre_archivo)

# Exercici 5.
# Escriure un programa que rebi un arxiu de text d'origen i un de destinació, de manera que per a cada línia de l'arxiu origen, es guardi una línia xifrada en l'arxiu destí.
# L'algorisme de xifrat a utilitzar serà molt senzill: a cada caràcter comprès entre l'a i la z, se li sumeixi 13 i després s'aplica el mòdul 26, per obtenir un nou caràcter. 
def cifrar_rot13(texto):
    alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    texto_cifrado = ""

    for char in texto:
        if char in alfabeto_minusculas:  # Si el carácter está en el alfabeto minúsculo
            indice = alfabeto_minusculas.index(char)  # Buscamos el índice de la letra
            nuevo_indice = (indice + 13) % 26  # Desplazamos 13 posiciones en el alfabeto
            texto_cifrado += alfabeto_minusculas[nuevo_indice]  # Concatenamos el nuevo carácter
        elif char in alfabeto_mayusculas:  # Si el carácter está en el alfabeto mayúsculo
            indice = alfabeto_mayusculas.index(char)  # Buscamos el índice de la letra
            nuevo_indice = (indice + 13) % 26  # Desplazamos 13 posiciones en el alfabeto
            texto_cifrado += alfabeto_mayusculas[nuevo_indice]  # Concatenamos el nuevo carácter
        else:
            texto_cifrado += char  # Si el carácter no es letra, lo agregamos tal cual (espacios, puntuación, etc.)

    return texto_cifrado

def cifrar_archivo(origen, destino):
    try:
        archivo_origen = open(origen, 'r')
        archivo_destino = open(destino, 'w')
        for linea in archivo_origen:
            linea_cifrada = cifrar_rot13(linea)
            archivo_destino.write(linea_cifrada)
        print(f"Archivo cifrado guardado en '{destino}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

origen = input("Introduce el nombre del archivo de origen: ")
destino = input("Introduce el nombre del archivo de destino: ")
cifrar_archivo(origen, destino)

# Exercici 6. Persistència d'un diccionari
# Escriure una funció carregar_dades que rebi un nom d'arxiu, el contingut del qual té el format clau, valor i retorni un diccionari amb el primer camp com a clau i el segon com a valor.
# Escriure una funció guardar_dades que rebi un diccionari i un nom d'arxiu, i guardi el contingut del diccionari en l'arxiu, amb el format clau, valor. 
