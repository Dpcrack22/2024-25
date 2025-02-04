# Definimos nuevamente las condiciones iniciales y ajustamos el formato solicitado
celulas_CA = 100
bacterias_B1 = 10
bacterias_B2 = 5
tiempo_total = 12  # Total de tiempo en segundos


# Función para generar el reporte en el formato solicitado
def generar_reporte(t, celulas_CA, bacterias_B1, bacterias_B2, evento):
    return f"""
**********************************Segundos = {t}**********************************
1)Las Celulas CA se duplican
=>Bacterias B1 = {bacterias_B1},Bacterias B2 = {bacterias_B2},Celulas CA = {celulas_CA}
{evento}
"""


reporte_completo = ""

# Simulamos cada segundo hasta el tiempo total
for t in range(1, tiempo_total + 1):
    evento = ""

    # Evento 1: Las células CA se duplican cada segundo
    celulas_CA = duplicar_CA(celulas_CA)

    # Evento 2: Cada 2 segundos las bacterias B1 se comen 3 células CA y se duplican
    if t % 2 == 0:
        evento += "2)Cada bacteria B1 se come 3 celulas CA y se dublica, en caso de no tener suficientes celulas para comer, se mueren.\n"
        celulas_CA, bacterias_B1 = bacterias_B1_comen_y_duplican(celulas_CA, bacterias_B1, 3)
        if bacterias_B1 > 0:
            evento += "(Todas las bacterias B1 comeran Celulas CA)\n"
        else:
            evento += "(Algunas bacterias B1 no comeran Celulas CA)\n"
        evento += f"=>Bacterias B1 = {bacterias_B1},Bacterias B2 = {bacterias_B2},Celulas CA = {celulas_CA}\n"

    # Evento 3: Cada 3 segundos las bacterias B2 matan a las B1 y las B1 comen 2 células CA
    if t % 3 == 0:
        evento += "3)Cada 2 bacterias B2 matan 1 bacteria B1. Cada bacteria B1 se come 2 celulas CA y se duplican, en caso de no tener suficientes celulas para comer, se mueren.\n"
        bacterias_B1 = B2_mata_B1(bacterias_B1, bacterias_B2)
        evento += "(Las bacterias B2 matan bacterias B1)\n"
        evento += f"=>Bacterias B1 = {bacterias_B1},Bacterias B2 = {bacterias_B2},Celulas CA = {celulas_CA}\n"
        celulas_CA, bacterias_B1 = bacterias_B1_comen_y_duplican(celulas_CA, bacterias_B1, 2, duplicacion=True)
        evento += "(Todas las bacterias B1 comeran Celulas CA)\n"
        evento += f"=>Bacterias B1 = {bacterias_B1},Bacterias B2 = {bacterias_B2},Celulas CA = {celulas_CA}\n"

    # Evento 4: Cada 4 segundos las células CA matan bacterias B1 y las B1 matan bacterias B2
    if t % 4 == 0:
        evento += "4)Cada 5 celulas CA matan una Bacteria B1. Cada 3 Bacterias B1 matan una B2.\n"
        bacterias_B1 = CA_mata_B1(celulas_CA, bacterias_B1)
        bacterias_B2 = B1_mata_B2(bacterias_B1, bacterias_B2)
        evento += f"=>Bacterias B1 = {bacterias_B1},Bacterias B2 = {bacterias_B2},Celulas CA = {celulas_CA}\n"

    # Agregamos el reporte para este segundo
    reporte_completo += generar_reporte(t, celulas_CA, bacterias_B1, bacterias_B2, evento)

reporte_completo
