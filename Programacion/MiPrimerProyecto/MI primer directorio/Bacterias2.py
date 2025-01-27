import time
from tty import IFLAG
from xml.dom.minidom import ProcessingInstruction

B1=int(100)
B2=int(50)
CA=int(100)
t=0

while (B1 >0 and B2 >0) or (CA >0 and B2 >0) or (B1 >0 and CA >0):
    CA = CA*2
    print("Las celulas CA se duplican\n")
    print("Bacterias B1 = {} , Bacterias B2 = {} , Bacterias CA = {}".format(B1,B2,CA))

    #Cada 2 segundos
    if t%2==0:
        if CA >= 3*B1:
            print("\t(Todas las bacterias B1 comeran Celulas CA)")
            CA = CA - 3*B1
        else:
            Bacterias_B1_CA = CA // 3
            B1 = B1 * 2
            B1 = Bacterias_B1_CA * 2


        # ComerB1 = 3*B1
        # if CA >= B1:
        #     CA-=ComerB1
        #     B1*=2
        #     print("Todas las bacterias B1 comeran Celulas CA")
        # else :
        #     MorirB1 = (ComerB1-CA) // 3
        #     B1-=MorirB1
        #     CA=0
        #     print("No todas las bacterias B1 comeran Celulas CA")

    if t%3==0:
        bacterias_muertas_B1_por_B2 = B2 // 2
        if bacterias_muertas_B1_por_B2 >= B1:
            B1=0
            print("\t(Todas las bacterias B1 mueren por bacterias B2)")
        else:
            B1 -= bacterias_muertas_B1_por_B2



    #Cada 4 segundos
    if t%4==0:
        Bacterias_B1_Muertas_por_CA = CA // 5
        if Bacterias_B1_Muertas_por_CA >= B1:
            B1=0
        else:
            B1 = B1 - Bacterias_B1_Muertas_por_CA
            print("")

        Bacterias_B2_muertas_por_B1 = B1 // 3
        if Bacterias_B2_muertas_por_B1 >= B2:
            B2=0
        else:
            B2=B2 - Bacterias_B2_muertas_por_B1

        # if B2 >= 0:
        #     MatarB2 = B1 // 2
        #     if MatarB2 >=B2:
        #         B1 -= MatarB2
        #         B2=0
        #     else:
        #         continue
        #
        #     ComerB1 = 3 * B1
        #     if CA >= B1:
        #         CA-=ComerB1
        #         B1*=2
        #         print("Todas las bacterias B1 comeran Celulas CA")
        #     else :
        #         MorirB1 = (ComerB1-CA) // 3
        #         B1-=MorirB1
        #         CA=0
        #         print("No todas las bacterias B1 comeran Celulas CA")

    time.sleep(1)
    t = t + 1
# tiempo_inicial = time.time()
# ultimo_tiempo_1s = tiempo_inicial
# ultimo_tiempo_2s = tiempo_inicial
# ultimo_tiempo_3s = tiempo_inicial
# ultimo_tiempo_4s = tiempo_inicial
#
#
# while True:
#     tiempo_actual = time.time()
#
#     if tiempo_actual - ultimo_tiempo_1s >= 1:
#         CA = CA*2
#         print("Las celulas CA se duplican\n")
#         print("Bacterias B1 = {} , Bacterias B2 = {} , Bacterias CA = {}".format(B1,B2,CA))
#         ultimo_tiempo_2s = tiempo_actual  # Actualizamos el tiempo
#
#     # Si han pasado 2 segundos desde la última vez que se imprimió el segundo texto
#     if tiempo_actual - ultimo_tiempo_2s >= 2:
#          print("Texto que aparece cada 3 segundos")
#          ultimo_tiempo_3s = tiempo_actual
#
#      # Pequeña pausa para evitar que el bucle consuma demasiada CPU
#     time.sleep(1)


