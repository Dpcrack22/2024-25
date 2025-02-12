import os

# Exercici 1: Crear o esborrar una carpeta "Temp"
def gestiona_carpeta_temp():
    carpeta = os.path.abspath("Temp")
    if os.path.exists(carpeta):
        try:
            os.rmdir(carpeta)
            print(f"S'ha esborrat la carpeta {carpeta}.")
        except Exception as e:
            print(f"Error en esborrar la carpeta: {e}")
    else:
        try:
            os.mkdir(carpeta)
            print(f"S'ha creat la carpeta {carpeta}.")
        except Exception as e:
            print(f"Error en crear la carpeta: {e}")

# Exercici 2: Canviar extensions de fitxers
def canviar_extensio():
    antiga, nova = input("Introdueix dues extensions separades per espai (ex: txt jpg): ").split()
    for fitxer in os.listdir():
        if fitxer.endswith(f".{antiga}"):
            nom_sense_extensio = os.path.splitext(fitxer)[0]
            nou_nom = nom_sense_extensio + "." + nova
            os.rename(fitxer, nou_nom)
            print(f"{fitxer} -> {nou_nom}")

# Exercici 3: Buscar un fitxer en una jerarquia de carpetes
def cercar_fitxer():
    nom_fitxer = input("Quin és el nom del fitxer a cercar? ")
    carpeta = input("Escriu el nom d'una ruta a una carpeta: ")
    for arrel, subcarpetes, fitxers in os.walk(carpeta):
        if nom_fitxer in fitxers:
            ruta_fitxer = arrel + "/" + nom_fitxer
            print(f"S'ha trobat el fitxer a: {ruta_fitxer}")

# Exercici 4: Esborrar un fitxer i mostrar propietats
def delNomFitxer(nomFitxer):
    try:
        os.remove(nomFitxer)
        print(f"S'ha esborrat el fitxer {nomFitxer}.")
    except FileNotFoundError:
        print("El fitxer no existeix.")
    except Exception as e:
        print(f"Error: {e}")

def propNomFitxer(nomFitxer):
    try:
        mida = os.path.getsize(nomFitxer)
        print(f"El fitxer {nomFitxer} té una mida de {mida} bytes.")
    except FileNotFoundError:
        print("El fitxer no existeix.")
    except Exception as e:
        print("Error: {}".format(e))
