"""
Funciones recursivas

1. Crea una función recursiva que calcule el factorial de un número.

2. Crea una función recursiva que sume los números del 1 hasta n.

3. Crea una función recursiva que cuente cuántos dígitos tiene un número entero positivo.

4. Crea una función recursiva que reciba una cadena de texto y devuelva la cadena invertida.

"""

def ejercicio1(n):
    if n == 0:
        return 1
    else:
        return n * ejercicio1(n - 1)

print("Factorial de 5:", ejercicio1(5))

def ejercicio2(n):
    resultado = 0
    if n == 0:
        return resultado
    else:
        resultado += n + ejercicio2(n-1)
    return resultado
print("Suma de números del 1 hasta 5:", ejercicio2(5))

def ejercicio3(n):
    resultado = 0
    n= str(n)
    if len(n) == 0:
        return resultado
    else:
        n = int(n)
        resultado += 1 + ejercicio3(n // 10)
    return resultado
#print("Número de dígitos en 12345:", ejercicio3(12345))

def ejercicio4(cadena):
    resultado = ""
    if len(cadena) == 0:
        return resultado
    else:
        resultado += cadena[-1] + ejercicio4(cadena[:-1])
    return resultado
print("Cadena invertida de 'Hola':", ejercicio4("Hola"))

"""
Donada una paraula, crear un algoritmo recursiu que realitzi lo següent:
Si l’usuari escriu Benvinguts:
Per pantalla sortirà:
B
Be
Ben
Benv
Benvi
Benvin
Benving
Benvingu
Benvingut
Benvinguts
"""

def ejercicio5(palabra):
    resultado = ""
    if len(palabra) == 0:
        return resultado
    else:
        resultado += palabra[-1] + ejercicio5(palabra[:-1])
        
    return resultado
print("Imprimiendo palabra 'Benvinguts':")
print(ejercicio5("Benvinguts"))

