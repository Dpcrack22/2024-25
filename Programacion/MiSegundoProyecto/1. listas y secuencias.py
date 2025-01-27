# llista = ["Cosa", 5, 5.6, True, ["a", "b", "c"]]
# print(len(llista))
# print(llista.count(5.6))
# llista1 = []
#
# print(len(llista1))
# print(type(llista1))
import random
from fileinput import lineno

# llista.append("Cosa2")
# llista.insert(1,"Cosa2")
# llista[2] = "Cosaaa"
# llista.remove(5.6)
# print(llista)

# llista1 = ["x","y","z"]
# llista2 = llista + llista1

# for i in range (len(llista)):
#     print(llista[i])
#
# for elemento in llista:
#     print(elemento)

# Cabezera = "Alumnos".center(40, "-") + "\n" + "Nombre".ljust(10) + "Nota".rjust(10) + "Literal".rjust(20) + "\n" + "".center(40 , "-")
# alumnos = [["Marcisa",4],["Anacleto",8],["Robustiana", 6]]
# datos = ""
# for alumno in alumnos:
#     literal = ""
#     if alumno[1] < 5:
#         literal = "suspendido"


#datos = datos + alumno[0].ljust(10) +

# print(Cabezera)
# print(alumnos)

#Sirve para poner los numeros en columnas y lineas
# lista = [[3,4,5],[6,7,8],[9,10,11]]
#
# for i in range(len(lista)):
#     for j in range(len(lista[i])):
#         print(str(lista[i][j]).rjust(6),end="")
#     print()


dimension = 4
lista = []

for i in range(dimension):
    lista.append([])
    for j in range(dimension):
        lista[i].append(random.randrange(10))

for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(str(lista[i][j]).rjust(6),end="")
    print()

fila = int(input("Dime una fila para sumar"))
suma_fila = 0
for i in range(len(lista[fila])):
    suma_fila = suma_fila + lista[fila][i]
print("la suma de los elementos de la fila {} es {}".format(fila,suma_fila))

columna = int(input("Dime una columna para sumar"))
suma_columna = 0
for i in range(dimension):
    suma_columna = suma_columna + lista[i][columna]
print("la suma de los elementos de la columna {} es {}".format(columna,suma_columna))