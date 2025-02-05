# Pràctica 1 recursivitat:
# 1) Programar un algoritme recursiu que permeti fer la divisió per restes successives.
def divisio_restes(dividend, divisor):
    if divisor == 0:
        raise ValueError("El divisor no pot ser zero.")
    resultado = 0
    if dividend >= divisor:
        resultado = 1 + divisio_restes(dividend - divisor, divisor)
    return resultado

# 2). Programar un algoritme recursiu que permeti sumar els dígits d’un número.
def suma_digits(n):
    resultado = 0
    if n > 0:
        resultado = n % 10 + suma_digits(n // 10)
    return resultado

# 3). Programar un algoritme recursiu que permeti sumar els elements d’una llista.
def suma_llista(llista):
    resultado = 0
    if llista:
        resultado = llista[0] + suma_llista(llista[1:])
    return resultado

# 4). Escriure la funció Potencia(x, y) = x^y de manera recursiva. Ajuda: pot(x,n)=x*pot(x,n-1); pot(x,0)=1;
def potencia(base, exponente):
    resultado = 1
    if exponente > 0:
        resultado = base * potencia(base, exponente - 1)
    return resultado

# 5). Escriure el producte de dos números de manera recursiva. Ajuda: 2x3 implica sumar tres vegades el número dos.
def producte(a, b):
    resultado = 0
    if b > 0:
        resultado = a + producte(a, b - 1)
    return resultado

# 6).Programar una funció recursiva que permeti multiplicar els elements d’un Array.
def producte_llista(llista):
    resultado = 1
    if llista:
        resultado = llista[0] * producte_llista(llista[1:])
    return resultado

# 7).Escriure un programa que trobi la suma dels enters positius parells des de N fins a 2.
def suma_parells(n):
    resultado = 0
    if n >= 2:
        if n % 2 == 0:
            resultado = n + suma_parells(n - 2)
        else:
            resultado = suma_parells(n - 1)
    return resultado
    
# 8).Escriure una funció recursiva que imprimeixi per pantalla els valors des de 1 fins a un número introduït per l’usuari.
def imprimir_ascendent(n):
    if n >= 1:
        imprimir_ascendent(n - 1)
        print(n)

# 9). Dissenyeu una funció recursiva tal que, donats dos vectors de número sencers, retorni un booleà indicant si són iguals, és a dir, si tenen els mateixos valors a les mateixes posicions.
def vectors_iguals(v1, v2):
    resultado = False
    if len(v1) == len(v2):
        if not v1:
            resultado = True
        else:
            resultado = v1[0] == v2[0] and vectors_iguals(v1[1:], v2[1:])
    return resultado

# 10)Donat un vector de números enters ordenat decreixentment, dissenyeu un programa recursiu que comprovi si el valor d’algun dels elements del vector coincideix amb el seu índex.
def coincideix_index(vector, inici=0, fi=None):
    resultado = False
    if fi is None:
        fi = len(vector) - 1
    if inici <= fi:
        mig = (inici + fi) // 2
        if vector[mig] == mig:
            resultado = True
        elif vector[mig] > mig:
            resultado = coincideix_index(vector, inici, mig - 1)
        else:
            resultado = coincideix_index(vector, mig + 1, fi)
    return resultado
    
# 11)Programa recursiu que demani a l’usuari una frase i la repeteixi un determinat número de vegades.
def repetir_frase(frase, n):
    if n > 0:
        print(frase)
        repetir_frase(frase, n - 1)

# 13). Programa recursiu que comprovi si un número està en un rang de valors.
def en_rang(num, minim, maxim):
    resultado = False
    if minim <= maxim:
        if num == minim:
            resultado = True
        else:
            resultado = en_rang(num, minim + 1, maxim)
    return resultado

# 14). Escriure un programa recursiu que insereixi valors aleatoris en una llista.
import random

def inserir_aleatoris(llista, mida):
    if len(llista) < mida:
        llista.append(random.randint(0, 100))  # Rango de ejemplo
        inserir_aleatoris(llista, mida)
    return llista

# 15). Escriure un programa recursiu que insereixi valors aleatoris sense repetició en una llista.

def inserir_aleatoris_unics(llista, mida):
    if len(llista) < mida:
        num = random.randint(0, 100)
        if num not in llista:
            llista.append(num)
        inserir_aleatoris_unics(llista, mida)
    return llista



##  Practica2  ##
# 1. Fórmula de Wallis (aproximació de π)
def wallis(n, acumulat=1.0):
    if n == 0:
        return 2 * acumulat
    terme = (4 * n**2) / (4 * n**2 - 1)
    return wallis(n - 1, acumulat * terme)

n = 1000  # Nombre de termes per a l'aproximació
print("Aproximació de π:", wallis(n))

# 2. Invertir un número
def invertir_numero(n, invertit=0):
    if n == 0:
        return invertit
    return invertir_numero(n // 10, invertit * 10 + n % 10)

print("Número invertit:", invertir_numero(123))  # Sortida: 321

# 3. Multiplicació Russa
def multiplicacio_russa(a, b, acumulat=0):
    if a == 0:
        return acumulat
    if a % 2 != 0:
        acumulat += b
    return multiplicacio_russa(a // 2, b * 2, acumulat)

print("Multiplicació Russa:", multiplicacio_russa(27, 82))

# 4. Curiositat matemàtica
def curiosidad_matematica(n):
    if n == 0:
        return
    num = 0
    if n> 0:
        num = int("1"*n)
        curiosidad_matematica(n-1)

print(curiosidad_matematica(20))

# 5. Endevina el número
import random

def endevina_numero(minim=0, maxim=1000, intents=0):
    if minim == maxim:
        print(f"CORRECTE. Has endevinat el número en {intents} intents.")
        return
    intent = int(input(f"Quin creus que és? ({minim}-{maxim}): "))
    if intent < minim or intent > maxim:
        print("Fora de rang. Torna a intentar.")
        endevina_numero(minim, maxim, intents)
    else:
        if intent == minim == maxim:
            print(f"CORRECTE. Has endevinat el número en {intents + 1} intents.")
        elif intent < (minim + maxim) // 2:
            print(f"El número es troba entre {intent} i {maxim}")
            endevina_numero(intent, maxim, intents + 1)
        else:
            print(f"El número es troba entre {minim} i {intent}")
            endevina_numero(minim, intent, intents + 1)

numero_secret = random.randint(1, 1000)
print("El programa ha generat un número entre 0 i 1000")
endevina_numero()

# 6. Separar paraules d’una frase
def separar_paraules(frase, index=0, paraula=""):
    if index >= len(frase):
        if paraula:
            print(paraula)
        return
    if frase[index] == " ":
        if paraula:
            print(paraula)
        separar_paraules(frase, index + 1, "")
    else:
        separar_paraules(frase, index + 1, paraula + frase[index])

separar_paraules("Hola món recursiu")

# 7. Eliminar vocals d’una frase
def eliminar_vocals(frase, index=0, resultat=""):
    if index >= len(frase):
        return resultat
    if frase[index].lower() not in "aeiou":
        resultat += frase[index]
    return eliminar_vocals(frase, index + 1, resultat)

print("Frase sense vocals:", eliminar_vocals("Hola món recursiu"))

# 8. Mostrar paraula progressivament
def mostrar_paraula(paraula, index=0):
    if index >= len(paraula):
        return
    print(paraula[:index + 1])
    mostrar_paraula(paraula, index + 1)

mostrar_paraula("Benvinguts")