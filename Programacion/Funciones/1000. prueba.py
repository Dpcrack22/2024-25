def hanoi(n, origen, destino, auxiliar, lista_origen, lista_destino, lista_auxiliar):
    # Caso base: Si solo hay un disco, lo movemos directamente de la torre origen a la torre destino
    if n == 1:
        # Mover el disco de la torre origen a la torre destino
        lista_destino.append(lista_origen[0])  # Añadimos el disco a la torre destino
        lista_origen = lista_origen[1:]  # Eliminamos el disco de la torre origen
        print(f'Movimiento de {origen} a {destino}: {lista_origen}, {lista_destino}, {lista_auxiliar}')
        return lista_origen, lista_destino, lista_auxiliar
    else:
        # Mover los n-1 discos de la torre origen a la torre auxiliar
        lista_origen, lista_auxiliar, lista_destino = hanoi(n - 1, origen, auxiliar, destino, lista_origen,
                                                            lista_auxiliar, lista_destino)

        # Mover el disco más grande de la torre origen a la torre destino
        lista_destino.append(lista_origen[0])  # Añadimos el disco más grande a la torre destino
        lista_origen = lista_origen[1:]  # Eliminamos el disco de la torre origen
        print(f'Movimiento de {origen} a {destino}: {lista_origen}, {lista_destino}, {lista_auxiliar}')

        # Mover los n-1 discos de la torre auxiliar a la torre destino
        lista_auxiliar, lista_destino, lista_origen = hanoi(n - 1, auxiliar, destino, origen, lista_auxiliar,
                                                            lista_destino, lista_origen)

    return lista_origen, lista_destino, lista_auxiliar


# Inicialización de las torres
n = 3  # Número de discos
lista_origen = [3, 2, 1]  # Torre origen tiene los discos en orden descendente, las otras están vacías
lista_destino = []
lista_auxiliar = []

# Llamar a la función con el número de discos, y las torres origen, destino y auxiliar
final_origen, final_destino, final_auxiliar = hanoi(n, 'Origen', 'Destino', 'Auxiliar', lista_origen, lista_destino,
                                                    lista_auxiliar)
print(f'Torres finales: {final_origen}, {final_destino}, {final_auxiliar}')