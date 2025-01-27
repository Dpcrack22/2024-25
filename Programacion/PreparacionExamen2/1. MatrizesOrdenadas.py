import random  # Importa el módulo random para generar números aleatorios

# Define el tamaño de la matriz cuadrada (4x4)
dimension = 4

# Crea una lista vacía que representará la matriz
matriz = []

# Generar la matriz con números aleatorios
for i in range(dimension):  # Recorre cada fila
    matriz.append([])  # Agrega una nueva fila como lista vacía
    for j in range(dimension):  # Recorre cada columna
        # Genera un número aleatorio entre 0 y 39 y lo agrega a la fila actual
        matriz[i].append(random.randrange(40))

# Imprimir la matriz original
for i in range(dimension):  # Recorre cada fila
    for j in range(dimension):  # Recorre cada columna
        # Imprime cada elemento alineado a la derecha con 4 espacios
        print(str(matriz[i][j]).rjust(4), end="")
    print()  # Salta a la siguiente línea después de imprimir una fila

# Ordenamiento inverso con el algoritmo de burbuja en las filas
for fila in range(dimension):  # Recorre cada fila
    for pasadas in range(dimension - 1):  # Itera el número de pasadas necesarias
        for i in range(dimension - 1, pasadas, -1):  # Recorre de derecha a izquierda
            # Si el elemento actual es mayor que el anterior, intercambia los valores
            if matriz[fila][i] > matriz[fila][i - 1]:
                aux = matriz[fila][i]  # Guarda el valor actual en una variable auxiliar
                matriz[fila][i] = matriz[fila][i - 1]  # Intercambia los valores
                matriz[fila][i - 1] = aux  # Asigna el valor guardado al lugar correcto

# Imprimir la matriz ordenada por filas en orden descendente
print("******************************")
for i in range(dimension):  # Recorre cada fila
    for j in range(dimension):  # Recorre cada columna
        # Imprime cada elemento alineado a la derecha con 4 espacios
        print(str(matriz[i][j]).rjust(4), end="")
    print()  # Salta a la siguiente línea después de imprimir una fila

# Ordenamiento inverso con el algoritmo de burbuja en las columnas
for columna in range(dimension):  # Recorre cada columna
    for pasadas in range(dimension - 1):  # Itera el número de pasadas necesarias
        for i in range(dimension - 1, pasadas, -1):  # Recorre de abajo hacia arriba
            # Si el elemento actual es mayor que el de la fila superior, intercambia los valores
            if matriz[i][columna] > matriz[i - 1][columna]:
                aux = matriz[i][columna]  # Guarda el valor actual en una variable auxiliar
                matriz[i][columna] = matriz[i - 1][columna]  # Intercambia los valores
                matriz[i - 1][columna] = aux  # Asigna el valor guardado al lugar correcto

# Imprimir la matriz ordenada por columnas en orden descendente
print("******************************")
for i in range(dimension):  # Recorre cada fila
    for j in range(dimension):  # Recorre cada columna
        # Imprime cada elemento alineado a la derecha con 4 espacios
        print(str(matriz[i][j]).rjust(4), end="")
    print()  # Salta a la siguiente línea después de imprimir una fila
