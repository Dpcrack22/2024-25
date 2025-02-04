
# Ejercicio 2: Escriure el codi de la funció que imprimeixi per pantalla tants asteriscs como
# indiqui el número que rep com argument. 

def asteriscos(numero):
    asteriscos = "*"
    for i in range(numero):
        print( i+1 , asteriscos)
    return asteriscos

asteriscos(10)

# Ejercicio 3: Escriure el codi de la funció que imprimeixi per pantalla tots els divisors del
# número que rep com argument. 

def imprimir_divisores(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

num = int(input("Ingresa un número: "))
imprimir_divisores(num)

#Ejercicio 4: Definir una funció superposicio() que tomi dos llistes i retorni true si tenen al menys 1
# membre en comú o retorni false de lo contrari.

def superposicio(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 3, 8]

print(superposicio(lista_a, lista_b))
 
# Ejercicio 5:  Definir un histograma procedimient() que tomi una llista de números enters i
# imprimeixi un histograma en la pantalla

def procedimient(llista):
    for num in llista:
        print("*" * num)

procedimient([4, 9, 7])

# Ejercicio 6: Definir una funció generar_n_caracters() que tomi un enter n i retorni el caràcter
# multiplicat per n. Per exemple: generar_n_caracters(5, "x") hauria de tornar "xxxxx". 
def generar_n_caracters(n, c):
    return c * n

resultat = generar_n_caracters(5, "x")
print(resultat)


# Ejerecicio 7: Escriure una funcio sum() i una funció multip() que sumen i multipliquin
# respectivament tots els números d’una llista.

def sum(llista):
    total = 0
    for num in llista:
        total += num
    return total

def multip(llista):
    total = 1
    for num in llista:
        total *= num
    return total

print(sum([1, 2, 3, 4]))
print(multip([1, 2, 3, 4]))

# Ejercicio 8: Escriu un programa que tingui una funció que demani dos anys i retorni quants anys de
# traspàs hi ha entre les dos dates (inclosos els dos anys):

def es_traspas(any):
    return (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)

def comptar_anys_traspas(any1, any2):
    if any1 > any2:
        any1, any2 = any2, any1  # Intercanviar si estan desordenats

    comptador = sum(1 for any in range(any1, any2 + 1) if es_traspas(any))
    
    return comptador

# Entrada d'usuaris
any1 = int(input("Escriu un any: "))
any2 = int(input(f"Escriu altre any posterior a {any1}: "))

while any2 <= any1:
    any2 = int(input(f"{any2} no és major que {any1}. Torna de nou: "))

# Resultats
total_anys = any2 - any1 + 1
anys_traspas = comptar_anys_traspas(any1, any2)

print(f"De {any1} a {any2} hi ha {total_anys} anys, {anys_traspas} d'ells de traspàs.")