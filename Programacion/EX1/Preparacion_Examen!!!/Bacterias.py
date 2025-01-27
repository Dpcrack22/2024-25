import time  # Importa la librería time para manejar retrasos en la ejecución del programa.

# Inicializamos las poblaciones
B1 = 100  # Población inicial de B1
B2 = 400  # Población inicial de B2
CA = 1000  # Población inicial de CA (células)
segundos = 1  # Contador de tiempo en segundos

# Bucle que se ejecuta mientras haya al menos una población viva
while (B1 > 0 and B2 > 0) or (B1 > 0 and CA > 0) or (B2 > 0 and CA > 0):
    # Imprime el encabezado del segundo actual
    print("********************************** Segundos = {} **********************************".format(segundos))

    # Evento cada 2 segundos: B1 se come B2 y se duplica
    if segundos % 2 == 0:
        print("2) Cada 2 segundos, cada B1 se come 2 B2 y se duplica.")
        if 2 * B1 <= B2:  # Verifica si todas las B1 pueden comer B2
            # Todas las B1 comen
            B2_comidas_por_B1 = 2 * B1  # Calcula cuántas B2 se comerán
            B2 -= B2_comidas_por_B1  # Resta las B2 comidas de la población de B2
            B1 *= 2  # Duplica la población de B1
        else:
            # No todas las B1 pueden comer
            B1_comen_B2 = B2 // 2  # Calcula cuántas B1 pueden comer B2
            B1_no_comen_B2 = B1 - B1_comen_B2  # Las B1 que no comen
            B1 = B1_no_comen_B2 + B1_comen_B2 * 2  # Actualiza la población de B1
            B2 = 0  # Todas las B2 se han comido

        print("=> Quedan {} B1, {} B2".format(B1, B2))

    # Evento cada 3 segundos: B2 se come CA y se triplica
    if segundos % 3 == 0:
        print("3) Cada 3 segundos, 1 B2 se come una CA y se triplica.")
        if CA >= B2:  # Verifica si hay suficiente CA para que B2 coma
            CA -= B2  # Resta la cantidad de CA comida por B2
            B2 *= 3  # Triplica la población de B2
        else:
            # No todas las B2 pueden comer CA
            B2_comen_CA = CA  # B2 come todo el CA disponible
            B2_no_comen_CA = B2 - B2_comen_CA  # B2 que no come
            B2 = B2_no_comen_CA + 3 * B2_comen_CA  # Actualiza la población de B2
            CA = 0  # Se acaban las células CA

        print("=> Quedan {} B2, {} CA".format(B2, CA))

    # Evento cada 4 segundos: Las CA se duplican
    if segundos % 4 == 0:
        print("4) Cada 4 segundos, las CA se duplican.")
        CA *= 2  # Duplicar la población de CA
        print("=> Quedan {} CA".format(CA))

    # Evento cada 5 segundos: CA mata B1
    if segundos % 5 == 0:
        print("5) Cada 5 segundos, cada 5 CA matan una B1.")
        B1_matadas_por_CA = CA // 5  # Calcula cuántas B1 serán asesinadas
        B1 -= B1_matadas_por_CA  # Resta las B1 asesinadas
        if B1 < 0:  # Si B1 es menor que 0, lo establece en 0
            B1 = 0

        print("=> Quedan {} B1".format(B1))

    # Mostrar el estado actual de las poblaciones
    print("Segundos {} --> Quedan {} B1, {} B2, {} CA".format(segundos, B1, B2, CA))
    
    # Esperar 1 segundo (para simular el tiempo)
    time.sleep(1)  # Pausa la ejecución del programa por 1 segundo.

    segundos += 1  # Incrementa el contador de tiempo.
