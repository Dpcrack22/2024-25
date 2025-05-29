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


#10)Donat un vector de números enters ordenat decreixentment, dissenyeu un programa recursiu que comprovi si el valor d’algun dels elements del vector coincideix amb el seu índex.
v = [23,12,7,4,4,2,1]

def num_coincide_indice(lista):
    resultado = False

    if len(lista) == 0:
        return resultado
    if lista[-1] == len(lista) -1:
        resultado = True
    else:
        resultado = num_coincide_indice(lista[:-1])
    return resultado

print(num_coincide_indice(v))

    
# 15). Escriure un programa recursiu que insereixi valors aleatoris sense repetició en una llista.
import random
def valores_aleatorios_inLista(n):
    resultado = []

    if n == 0:
        return resultado
    
    
    resultado = resultado + valores_aleatorios_inLista(n-1)
    num_aleatorio = random.randrange(1,100)

    if num_aleatorio not in resultado:
        resultado.append(num_aleatorio)
    
    return resultado


    


    

print(valores_aleatorios_inLista(10))
    

#1. Una fórmula interessant i que es pot deduir amb eines avançades de càlcul és la fórmula de Wallis, que permet tenir una expressió del número П a partir d'aquests productes:
# П = 2 *2/1 *2/3 *4/3 4/5 *6/5 *6/7 *8/7 *8/9

def wallis(n):
    resultado = 1
    if n == 0:
        resultado = 2
    else:
        resultado *= (4*n**2)/((2*n-1)*(2*n+1))*wallis(n-1)
    return resultado
#print(wallis(2))


#2. Programar una funció recursiva que permeti invertir un número. Exemple: Entrada: 123 Sortida: 321

def invertir_num(n):
    resultado = 0
    if n < 10:
        resultado = n
    else:
        resultado = (n%10)*(10**(len(str(n))-1))+invertir_num(n//10)
    return resultado

print(invertir_num(1234567898765432))

#3. Programar un algoritme recursiu que permeti fer una multiplicació, utilitzantel mètode Rus. Consisteix en:
 # Escriure els números (A i B) que es desitja multiplicar a la part superior de les columnes.
 # Dividir A entre 2, successivament, ignorant la resta, fins a arribar a la unitat. Escriure els resultats en la columna A.
 # Multiplicar B per 2 tantes vegades com vegades s’ha dividit A entre 2. Escriure els resultats successius en la columna B.
 # Sumar tots els números de la columna B que estan al costat d’un número senar de la columna A.
 # Aquest és el resultat: 

def multiplicacion_rusa(a, b):
    resultado = 0
    if a == 0 or b == 0:
        return resultado
    if a == 1:
        resultado = b
    elif a % 2 == 0:
        resultado = multiplicacion_rusa(a // 2, b * 2)
    else:
        resultado = b + multiplicacion_rusa(a // 2, b * 2)
    return resultado
print(multiplicacion_rusa(27, 82))

def metodo_ruso(a,b):
    resultado = 0
    if a == 1:
        resultado = b
    elif a%2 == 1:
        resultado = b + metodo_ruso(a//2,b*2)
    else:
        resultado = metodo_ruso(a//2,b*2)
    return resultado

print(metodo_ruso(27, 82))

#4. Curiositat matemàtica
#Feu un programa recursiu que mostri una sortida com la captura de pantalla que teniu a continuació:

