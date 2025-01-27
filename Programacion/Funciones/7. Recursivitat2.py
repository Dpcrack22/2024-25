import random

# 1. Una fórmula interessant i que es pot deduir amb eines avançades de càlcul
# és la fórmula de Wallis, que permet tenir una expressió del número П a partir
# d'aquests productes: П = 2 *2/1 *2/3 *4/3 4/5 *6/5 *6/7 *8/7 *8/9


# def wallis(x):
#     y = 1
#     if x == 0:
#         return 2 * y
#     else:
#         y = (wallis(x-1)*((2 * x) / (2 * x - 1)) * (2 * x) / (2 * x + 1))
#     return y
#
# print(wallis(10))

# def wallis(n):
#     resultado = 1
#
#     if n == 0:
#         resultado = 2
#     else:
#         resultado *= (4*n**2)/((2*n-1)*(2*n+1))*wallis(n-1)
#     return resultado
# print(wallis(10))

#Algo de burbuja
# lista = [1,2,3]
# def funcionA(lista):
#     lista[0] = 1000
#
# funcionA(lista)
# print(lista)
# lista = [1,2,3]
# funcionA(lista[:-1])
# print(lista)

#. Programar una funció recursiva que permeti invertir un número.
#Exemple: Entrada: 123 Sortida: 321

# def invertir_numero(num):
#     resultado = 0
#     if num < 10:
#         resultado = num
#     else:
#         resultado = int(str(num%10) + str(invertir_numero(num/10)))
#     return resultado
#
# print(invertir_numero(567))


# #Programar un algoritme recursiu que permeti fer una multiplicació, utilitzant
# el mètode Rus. Consisteix en:
#  Escriure els números (A i B) que es desitja multiplicar a la part superior
# de les columnes.
#  Dividir A entre 2, successivament, ignorant la resta, fins a arribar a la
# unitat. Escriure els resultats en la columna A.
#  Multiplicar B per 2 tantes vegades com vegades s’ha dividit A entre 2.
# Escriure els resultats successius en la columna B.
#  Sumar tots els números de la columna B que estan al costat d’un número
# senar de la columna A.
#  Aquest és el resultat:
# A
# def multiplicar_ruso(a, b):
#     resultado = 0
#     if a == 1:
#         resultado = b
#
#     elif a % 2 == 0:
#         resultado += multiplicar_ruso(a//2,b*2)
#     else:
#         resultado += b + multiplicar_ruso(b//2,b*2)
#     return resultado
#
# print(multiplicar_ruso(2, 3))


# def curiosidad_matematica(n):
#     if n == 0:
#         return
#     num = 0
#     if n> 0:
#         num = int("1"*n)
#         curiosidad_matematica(n-1)
#
# print(curiosidad_matematica(20))+

#5. Endevina el número
# El programa generarà un numero aleatori entre 1 i 1000 i l’usuari mira d’endevinarlo. L’aplicació en tot moment recolzarà a l’usuari, a partir del número que creu que
# és, mostrant entre quins números es troba la dada a endevinar.

# num = random.randrange(0,1000)
# def adivinar_numero(a,b):
#     intento = 1
#
#     num1 = imt(input("Dame un numero"))
#     if num1 == num:
#         print("Felicidades has adivinado el numero en {} intentos".format(intento))
#     elif num>num1:
#         print("Numero esta entre {} y {}".format(num1,b))
#         intento += 1 + adivinar_numero(num1,b)
#     else:
#         print("El numero esta entre {} y {}".format(a,num1))
#         intento += 1 + adivinar_numero(a,num1)
#     return intento

# def listas_iguales(lista,lista_fin1,lista_fin2):
#     if len(lista_fin1) == 0 or lista[-1] < lista_fin1[-1]:
#         lista_fin1.append(lista[-1])
#         lista.remove(lista[-1])
#         listas_iguales(lista,lista_fin1,lista_fin2)
#
#     if len(lista_fin2) == 0 or lista[-1] < lista_fin2[-1]:
#         lista_fin2.append(lista[-1])
#         lista.remove(lista[-1])
#         listas_iguales(lista, lista_fin1, lista_fin2)
#
#
#     if lista_fin1[-1] < lista_fin2[-1]:
#         lista_fin2.append(lista_fin1[-1])
#         lista_fin1.remove(lista_fin1[-1])
#         listas_iguales(lista, lista_fin1, lista_fin2)
#
#     if lista_fin2[-1] < lista[-1]:
#         lista.append(lista_fin2[-1])
#         lista_fin2.remove(lista_fin2[-1])
#         listas_iguales(lista, lista_fin1, lista_fin2)
#
#     if lista_fin2[-1] < lista_fin1[-1]:
#         lista_fin1.append(lista_fin2[-1])
#         lista_fin2.remove(lista_fin2[-1])
#         listas_iguales(lista, lista_fin1, lista_fin2)
#
# #         elif lista_fin1[-1] < lista[-1]:
# #         lista.append(lista_fin1[-1])
# #         lista_fin1.remove(lista_fin1[-1])
# #         listas_iguales(lista, lista_fin1, lista_fin2)
# #     elif lista_fin2[-1] < lista[-1]:
# #         lista.append(lista_fin2[-1])
# #         lista_fin2.remove(lista_fin2[-1])
# #         listas_iguales(lista, lista_fin1, lista_fin2)
#
# print("")
# print(listas_iguales(lista=[5,4,3,2,1],lista_fin1=[], lista_fin2=[]))


#Hacer metodo de burbuja de recursividad solo una pasada
def burbuja_pasada(lista):
    resultado = []
    if len(lista) == 1:
        resultado.append(lista[0])
        return resultado
    if lista[0] > lista[1]:
        aux = lista[0]
        lista[0] = lista[1]
        lista[1] = aux
    resultado.append(lista[0])
    resultado = resultado + burbuja_pasada(lista[1:])
    return resultado

    # resultado = []
    # if len(lista) == 1:
    #     resultado.append(lista[0])
    #     return resultado
    # elif lista[0] > lista[1]:
    #     resultado.append(lista[1])
    #     lista.remove(lista[1])
    #     burbuja_pasada(lista)
    # else:
    #     resultado.append(lista[0])
    #     lista.remove(lista[0])
    #     burbuja_pasada(lista)
    # return resultado


def doBurbuja():
    burbuja_pasada(lista=[100,1,45,32,23,43])


print("")
print(doBurbuja())

