import random

dimension = random.randint(5,10)

lista = []


for i in range(dimension):
    lista.append(random.randint(7,100))
#
# print(lista)
comparaciones = 0
#
# for i in range(len(lista)-1):
#     print(lista[i])
#     for j in range(i+1,len(lista)):
#         print(lista[i], lista[j])
#         comparaciones += 1
#         if lista[i] > lista[j]:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
# print(lista)
# print(comparaciones)
# print("*"*50)
print(lista)
for pasadas in range(len(lista)-1):
    for i in range(len(lista)-1 - pasadas):
        comparaciones += 1
        if lista[i] > lista[i +1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
print(lista)
print(comparaciones)