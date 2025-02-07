# 1. Fórmula de Wallis para calcular π
# La fórmula de Wallis es un producto infinito que converge a π/2. Aquí tienes una implementación en
def wallis(x):
    y = 1
    if x == 0:
        return 2 * y
    else:
        y = (wallis(x-1)*((2 * x) / (2 * x - 1)) * (2 * x) / (2 * x + 1))
    return y

print(wallis(10))

# 2. Función recursiva para invertir un número
# Vamos a invertir un número utilizando recursividad.
def invertir_numero(numero):
    if numero < 10:
        return numero  # Caso base: si el número tiene un solo dígito
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        return int(str(ultimo_digito) + str(invertir_numero(resto)))


print(invertir_numero(123))

# 3. Multiplicación rusa recursiva
# Implementación del método de multiplicación rusa usando recursividad.
def multiplicacion_rusa(a, b, suma=0):
    if a == 0:
        return suma  # Caso base
    else:
        if a % 2 != 0:  # Si A es impar, sumamos B
            suma += b
        return multiplicacion_rusa(a // 2, b * 2, suma)  # Llamada recursiva

print(multiplicacion_rusa(27, 82))  # Salida: 2214

# 4. Curiosidad matemática (Pirámide de números)
# Vamos a generar la pirámide de números usando recursividad.
def curiosidad_matematica(n):
    if n == 0:
        return
        num = 0
    if n> 0:
        num = int("1"*n)
        curiosidad_matematica(n-1)

print(curiosidad_matematica(20))

# 5. Juego "Adivina el número"
# Implementación del juego usando recursividad.
import random

def adivina_numero(minimo=0, maximo=1000, intentos=0):
    if minimo == maximo:
        print(f"¡CORRECTO! Has adivinado el número en {intentos} intentos.")
        return
    else:
        intento = int(input(f"Quin creus que és? (entre {minimo} i {maximo}): "))
        if intento < minimo or intento > maximo:
            print("Número fuera de rango. Intenta de nuevo.")
            adivina_numero(minimo, maximo, intentos)
        elif intento < numero_secreto:
            print(f"El número es troba entre {intento} i {maximo}")
            adivina_numero(intento, maximo, intentos + 1)
        elif intento > numero_secreto:
            print(f"El número es troba entre {minimo} i {intento}")
            adivina_numero(minimo, intento, intentos + 1)
        else:
            print(f"¡CORRECTO! Has adivinado el número en {intentos + 1} intentos.")

numero_secreto = random.randint(0, 1000)
print("El programa ha generat un número entre 0 i 1000")
#adivina_numero()

# 6. Separar palabras de una frase recursivamente
# Vamos a separar las palabras de una frase y mostrarlas una a una.

def separar_palabras(frase, palabras=None, index=0):
    if palabras is None:
        palabras = frase.split()  # Dividimos la frase solo una vez al inicio

    if index == len(palabras):  
        return  # Caso base: terminamos cuando ya no hay más palabras
    
    print(palabras[index])  # Imprimir la palabra actual
    separar_palabras(frase, palabras, index + 1)  # Recursión avanzando en la lista

separar_palabras("Hola món, com estàs?")

# 7. Eliminar vocales de una frase recursivamente
# Vamos a eliminar las vocales de una frase usando recursividad.
def eliminar_vocales(frase):
    if not frase:
        return ""  # Caso base
    else:
        primera_letra = frase[0]
        if primera_letra.lower() in "aeiou":
            return eliminar_vocales(frase[1:])  # Si es vocal, no la incluimos
        else:
            return primera_letra + eliminar_vocales(frase[1:])  # Llamada recursiva

print(eliminar_vocales("Benvinguts"))

# 8. Mostrar una palabra progresivamente
# Vamos a mostrar una palabra progresivamente, letra por letra.
def mostrar_progresivo(palabra, n=1):
    if n > len(palabra):
        return  # Caso base
    else:
        print(palabra[:n])
        mostrar_progresivo(palabra, n + 1)  # Llamada recursiva

mostrar_progresivo("Benvinguts")

# 9. Ordenar una lista de listas usando el método de la burbuja
# Implementación del método de la burbuja para ordenar una lista de listas.
def ordenar_burbuja(lista):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Realizamos una pasada del bubble sort
    for i in range(len(lista) - 1):
        # Comparamos los primeros elementos de las sublistas
        if lista[i][0] > lista[i + 1][0]:
            # Intercambiamos usando una variable auxiliar (aux)
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
    
    # Llamada recursiva para ordenar el resto de la lista (excluyendo el último elemento)
    lista_ordenada = ordenar_burbuja(lista[:-1]) + [lista[-1]]
    
    return lista_ordenada

lista = [[3, 1], [1, 4], [2, 2], [4, 1]]
print("Lista original:", lista)
print("Lista ordenada:", ordenar_burbuja(lista))