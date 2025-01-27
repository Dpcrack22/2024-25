bacteria_inicial = 1 
objectiu = 10000000
temps_per_duplicacio = 3 

minuts = 0

while bacteria_inicial < objectiu:
    bacteria_inicial *= 2 
    minuts += temps_per_duplicacio 

hores = minuts / 60

print("La bactèria triga {:.2f} hores a arribar als 10 milions.".format(hores))
