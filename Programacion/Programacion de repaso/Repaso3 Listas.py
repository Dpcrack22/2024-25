import random
lista = []

for i in range(5):
    lista.append(random.randrange(1,11))


for pasada in range(len(lista)-1):
    for i in range(len(lista)-pasada-1):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux

print(lista)
    