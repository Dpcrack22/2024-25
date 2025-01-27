import random
dimension = 4
matriz = []
for i in range(dimension):
    matriz.append([])
    for j in range(dimension):
        matriz[i].append(random.randrange(10))

for i in range(dimension):
    for j in range(dimension):
        print(str(matriz[i][j]).rjust(5),end="")
    print()

nueva_matriz = []
for i in range(dimension):
    nueva_matriz.append([])
    for j in range(dimension):
        suma = 0
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if (k >= 0 and l >=0 and k <= dimension-1 and l <= dimension -1 and (k!=i or l!=j)):
                    suma = suma + matriz[k][l]
        nueva_matriz[i].append(suma)
print("Nueva Matriz".center(30,"*"))
for i in range(dimension):
    for j in range(dimension):
        print(str(nueva_matriz[i][j]).rjust(5),end="")
    print()