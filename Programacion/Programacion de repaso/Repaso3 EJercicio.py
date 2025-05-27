#Vamos a tener una lista que tendra entre 5 y 10 elementos incluidos
#Cada uno de los elementos sera una lista que tendra entre 1 y 5 numeros aleatorios
import random

num_lista_elementos = random.randrange(5,11)
num_lista_de_listas = random.randrange(1,6)
lista = []

for i in range(num_lista_elementos):
    num_lista_de_listas = random.randrange(1,6)
    listas = []
    for j in range(num_lista_de_listas):
        listas.append(random.randrange(1,100))
    lista.append(listas)

print(lista)

lista_ordenada = []


for i in range(len(lista)):
    for j in range(len(lista[i]) - 1):
        for k in range(len(lista[i]) - 1 - j):
            if lista[i][k] > lista[i][k + 1]:
                aux = lista[i][k]
                lista[i][k] = lista[i][k + 1]
                lista[i][k + 1] = aux

print(lista)

for pasada in range(len(lista)-1):
    for i in range(len(lista)-pasada-1):
        suma_i = 0
        suma_i1 = 0
        for j in range(len(lista[i])):
            
            suma_i += lista[i][j]

        for j in range(len(lista[i+1])):
            suma_i1 += lista[i+1][j]
        
        if suma_i  < suma_i1:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux

print(lista)