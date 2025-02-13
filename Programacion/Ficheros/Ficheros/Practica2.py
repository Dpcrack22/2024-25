def llegir_clients(nom_arxiu):
    """
    Llegeix un fitxer i retorna una llista amb tuples (codi_client, informació).
    """
    clients = []
    try:
        with open(nom_arxiu, 'r') as f:
            for linia in f:
                if linia != "\n":  # Evitar línies completament buides
                    parts = linia.split("  ", 1)  # Separa només pel primer espai doble
                    if len(parts) == 2:
                        codi, info = parts[0], parts[1]  # Guarda la línia tal qual
                        clients.append((codi, info))
        return clients
    except FileNotFoundError:
        print("Error: No s'ha trobat l'arxiu", nom_arxiu)
        return []

def fusionar_clients(archivo1, archivo2):
    """
    Fusiona les dades de dos fitxers i les ordena pel codi de companyia.
    """
    clients1 = llegir_clients(archivo1)
    clients2 = llegir_clients(archivo2)

    tots_els_clients = clients1 + clients2  # Fusionem les llistes
    tots_els_clients.sort(key=lambda x: x[0])  # Ordenem pel codi de companyia

    return tots_els_clients

def guardar_clients(nom_arxiu, clients):
    """
    Guarda la llista de clients en un fitxer.
    """
    try:
        with open(nom_arxiu, 'w') as f:
            f.write("1  7  38  69\n")  # Escrivim la capçalera
            for client in clients:
                f.write(client[0] + "  " + client[1])  # Sense join ni strip
        print("Clients fusionats guardats en", nom_arxiu)
    except Exception as e:
        print("Error en guardar l'arxiu:", e)

# -------------------- #
#       EXECUCIÓ       #
# -------------------- #

arxiu_cara = "Cara.txt"
arxiu_dura = "Dura.txt"
arxiu_sortida = "CLIENTS.TXT"

clients_ordenats = fusionar_clients(arxiu_cara, arxiu_dura)
guardar_clients(arxiu_sortida, clients_ordenats)
