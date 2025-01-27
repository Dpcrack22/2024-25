import time

# Guardamos el tiempo inicial
tiempo_inicial = time.time()

# Definimos los tiempos de referencia para cada evento
ultimo_tiempo_2s = tiempo_inicial
ultimo_tiempo_3s = tiempo_inicial

while True:
    tiempo_actual = time.time()
    # Si han pasado 2 segundos desde la última vez que se imprimió el primer texto
    if tiempo_actual - ultimo_tiempo_2s >= 2:
        print("Texto que aparece cada 2 segundos")
        ultimo_tiempo_2s = tiempo_actual  # Actualizamos el tiempo
    # Si han pasado 3 segundos desde la última vez que se imprimió el segundo texto
    if tiempo_actual - ultimo_tiempo_3s >= 3:
        print("Texto que aparece cada 3 segundos")
        ultimo_tiempo_3s = tiempo_actual  # Actualizamos el tiempo
    # Pequeña pausa para evitar que el bucle consuma demasiada CPU
    time.sleep(0.1)