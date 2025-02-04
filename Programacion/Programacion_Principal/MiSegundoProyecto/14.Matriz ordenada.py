import  random

dimension = 4
matriz = []
for i in range(dimension):
    matriz.append([])
    for j in range(dimension):
        matriz[i].append(random.randrange(40))

for i in range(dimension):
    for j in range(dimension):
        print(str(matriz[i][j]).rjust(4),end="")
    print()


# for fila in range(dimension):
#     for pasadas in range(dimension-1):
#         for i in range(dimension - 1 - pasadas):
#             if matriz[fila][i] > matriz[fila][i+1]:
#                 aux = matriz[fila][i]
#                 matriz[fila][i] = matriz[fila][i+1]
#                 matriz[fila][i+1] = aux


#Ordenar incersamente con burbuja en filas
for fila in range(dimension):
    for pasadas in range(dimension-1):
        for i in range(dimension - 1,  pasadas,-1):
            #print(i , i-1)
            if matriz[fila][i] > matriz[fila][i-1]:
                aux = matriz[fila][i]
                matriz[fila][i] = matriz[fila][i-1]
                matriz[fila][i-1] = aux

print("******************************")
for i in range(dimension):
    for j in range(dimension):
        print(str(matriz[i][j]).rjust(4),end="")
    print()


#Ordenar incersamente con burbuja en columnas
for columna in range(dimension):
    for pasadas in range(dimension-1):
        for i in range(dimension - 1,  pasadas,-1):
            #print(i , i-1)
            if matriz[i][columna] > matriz[i-1][columna]:
                aux = matriz[i][columna]
                matriz[i][columna] = matriz[i-1][columna]
                matriz[i-1][columna] = aux
print("******************************")
for i in range(dimension):
    for j in range(dimension):
        print(str(matriz[i][j]).rjust(4),end="")
    print()



