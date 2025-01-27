import random

matriz = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]

filas = len(matriz)
columnas = len(matriz[0])

matriz_sumada = [[0] * columnas for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        suma = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < filas and 0 <= y < columnas and (x != i or y != j):
                    suma += matriz[x][y]
        matriz_sumada[i][j] = suma

print("Matriz original (4x4) con números aleatorios:")
for fila in matriz:
    print(fila)

print("\nMatriz con la suma de los vecinos:")
for fila in matriz_sumada:
    print(fila)

