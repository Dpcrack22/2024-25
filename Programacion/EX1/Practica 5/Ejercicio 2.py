PREU_PER_HORA = 30.0  
PREU_PER_METRE = 0.5
IVA = 0.21 

hores_treballades = int(input("Introdueix les hores treballades: "))

metres_instal·lats = float(input("Introdueix el número de metres de cable instal·lats: "))

preu_brut = (hores_treballades * PREU_PER_HORA) + (metres_instal·lats * PREU_PER_METRE)

preu_amb_IVA = preu_brut * (1 + IVA)

print("El preu brut és: {:.2f} €".format(preu_brut))
print("El preu amb IVA és: {:.2f} €".format(preu_amb_IVA))
