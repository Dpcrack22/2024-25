
#divisio amb restes recursives y muestra las veces que resta para dividirlo
def divisioRec(dividendo,divisor):
    resultado = 0
    if dividendo >= divisor:
        resultado += 1 + divisioRec(dividendo-divisor,divisor)
    return resultado
print("")
print(divisioRec(100,5))


def sumadigitos(numero):
    resultado = 0
    if numero <10:
        resultado += numero
    else:
        resultado = numero%10 + sumadigitos(numero//10)
    return resultado
print("")
print(sumadigitos(1475))


def potencia(base, exponente):
    resultado = 1
    if exponente > 0:
        resultado = 2*potencia(base,exponente-1)
    return resultado
print(potencia(2,8))

#Hacer una multiplicacion con sumas
def multiplicacion(num1, num2):
    resultado = 0
    if num2 >= 0:
        resultado += num1 + divisioRec(num1, num2-1)
    return resultado

print(multiplicacion(2,3))

#.Programar una funció recursiva que permeti multiplicar els elements d’un Array
def multiplicacionarray(lista):
    resultado = 1
    if len(lista) > 0 :
        resultado += lista[0] + multiplicacionarray(lista[1:])

    return resultado

print(multiplicacionarray([1,2,3,4]))


#7).Escriure un programa que trobi la suma dels enters positius parells des de N fins a 2.

def suma_pares(n):
    resultado = 0
    if n == 2:
        resultado = 2
    elif n%2 == 0:
        resultado = n + suma_pares(n-1)
    else:
        resultado = suma_pares(n-1)
    return resultado

print(suma_pares(11))

#8).Escriure una funció recursiva que imprimeixi per pantalla els valors des de 1 fins a un número introduït per l’usuari.

#9). Dissenyeu una funció recursiva tal que, donats dos vectors de número sencers, retorni un booleà indicant si són iguals, és a dir, si tenen els mateixos valors a les mateixes posicions.

def vectores_iguales(lista1, lista2):
    iguales = False
    if len(lista1) != len(lista2):
        return iguales
    elif len(lista1) == 0:
        iguales = True
        return iguales
    elif lista1[0] != lista2[0]:
        return iguales
    else:
        iguales = vectores_iguales(lista1[1:],lista2[1:])
    return iguales

lista1 = [1,2,3,4]
lista2 = [1,2,3,4]
print(vectores_iguales(lista1,lista2))

#10)Donat un vector de números enters ordenat decreixentment, dissenyeu un programa
# recursiu que comprovi si el valor d’algun dels elements del vector coincideix amb el seu índex.

def coincidencia_indice(lista):
    resultado = False
    if len(lista) == 0:
        return resultado
    elif lista[-1] == len(lista)-1:
        resultado = True
    else:
        resultado = coincidencia_indice(lista[:-1])
    return resultado

lista = [111,222,2,444]
print(coincidencia_indice(lista))

#11)Programa recursiu que demani a l’usuari una frase i la repeteixi un determinat número de vegades.

#13). Programa recursiu que comprovi si un número està en un rang de valors.

#14). Escriure un programa recursiu que insereixi valors aleatoris en una llista

#15). Escriure un programa recursiu que insereixi valors aleatoris sense repetició en una llista.

#Metodo burbuja decreciente recursibo
