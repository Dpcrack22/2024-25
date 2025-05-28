#1) Programar un algoritme recursiu que permeti fer la divisió per restes successives.
def divisio_amb_resta_recursiva(a,b):
    resultado = 0
    if a < b:
        return resultado
    else:
        resultado = 1 + divisio_amb_resta_recursiva(a-b,b)
    return resultado


print(divisio_amb_resta_recursiva(15,4))

#2). Programar un algoritme recursiu que permeti sumar els dígits d’un número.
def suma_digitos_recursiva(n):
    resultado = 0
    
    if n < 10:
        resultado = n
    else:
        resultado = n % 10 + suma_digitos_recursiva(n // 10)

    return resultado
print(suma_digitos_recursiva(12345))

#3). Programar un algoritme recursiu que permeti sumar els elements d’una llista.
def suma_digitos_lista_recursiva(lista):
    resultado = 0
    if len(lista) == 1:
        resultado = lista[0]
    else:
        resultado = lista[0] + suma_digitos_lista_recursiva(lista[1:])
    return resultado


print(suma_digitos_lista_recursiva([1, 2, 3, 4, 5]))

#4). Escriure la funció Potencia(x, y) = x^y de manera recursiva.
def calcular_potencia(x,y):
    resultado = 1
    if y == 0:
        return resultado
    else:
        resultado = x*calcular_potencia(x,y-1)
    return resultado
print(calcular_potencia(2,8))

#5). Escriure el producte de dos números de manera recursiva. Ajuda: 2x3 implica sumar tres vegades el número dos.
def producto_recursivo(a, b):
    resultado = 0
    if b == 1:
        resultado = a
    else:
        resultado = a + producto_recursivo(a, b - 1)
    return resultado
    
print(producto_recursivo(2, 3))

#6).Programar una funció recursiva que permeti multiplicar els elements d’un Array.


#7).Escriure un programa que trobi la suma dels enters positius parells des de N fins a 2.
def suma_pares(n):
    resultado = 0
    if n == 2:
        resultado = 2
    
    else:
        if n % 2 == 0:
            resultado = n + suma_pares(n-2)
        else:
            resultado = suma_pares(n-2)
    return resultado

    suma_pares(n-1)

print(suma_pares(10))

#8).Escriure una funció recursiva que imprimeixi per pantalla els valors des de 1 fins a un número introduït per l’usuari.
def imprimir_hasta_n(n):
    if n > 1:
        resultado = imprimir_hasta_n(n - 1)
    print(n)
    
imprimir_hasta_n(5)

#9). Dissenyeu una funció recursiva tal que, donats dos vectors de número sencers, retorni un booleà indicant si són iguals, és a dir, si tenen els mateixos valors a les mateixes posicions.
def vectores_iguales(v1,v2):
    resultado = True
    if len(v1) != len(v2):
        resultado = False
    if len(v1) == 0 or len(v2) == 0:
        resultado = True
    elif v1[0] != v2[0]:
        resultado = False
    else:
        resultado = vectores_iguales(v1[1:], v2[1:])
    return resultado

print(vectores_iguales([1, 2, 3], [1, 2, 3]))  # True
print(vectores_iguales([1, 2, 3], [1, 2, 4]))  # False

