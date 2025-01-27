from multiprocessing.forkserver import read_signed


#
# def funcionA(lista):
#     print(lista[0])
#     funcionA(lista[1:])
#     print("Hola soy la funcion A")

# def funcionB(a,b):
#     suma = a + b
#     print("Hola soy la funcion B")
#     c = 10
#     funcionA()
#     return suma
# def funcionC():
#     a = 1
#     b = 2
#     print("Hola soy la funcion C")
#
# print("a")
# funcionA([1,2,3,4])
# print("FIn")


#Estro esta mal
# def suma_lista(suma,lista):
#     print(lista)
#     suma +=  lista[0] + lista[1]
#     suma_lista(lista[1:])
#     print(suma)
#
# print("")
# suma_lista(0,[2,2,2,4,4,2])
# print("FI")


# def suma_lista(lista):
#     resultado = 0
#     if len(lista)!=0:
#         resultado = resultado + lista[0]
#         resultado = resultado + suma_lista(lista[1:])
#     return resultado
#
# print("")
# suma_lista([2,2,2,4,4,2])
# print()
# print("FI")

# def suma_pares(lista):
#     resultado = 0
#     if len(lista)!=0:
#         if lista[0]%2 == 0:
#             resultado = resultado + lista[0]
#         resultado = resultado + suma_pares(lista[1:])
#
#     return resultado
#
#
# print("a")
# suma_pares([1,2,3,4,5,6,7,1,2,3,4,5,6,8])
# print("FIn")

#Doy una frase y una vocal y sale desde la primera vocal que pones hasta el final de la frase
# def funcionA(string, Vocales):
#     resultado = ""
#     if string[0]==Vocales:
#         resultado = string
#     else:
#         resultado = funcionA(string[1:], Vocales)
#     return resultado
#
# print(".")
# print(funcionA("La casa de pepe es azul y rosita", "e"))
# print("FIN")

#Lo Mismo que antes pero al reves
# dada una frase y una vocal que devuelva la frase al reves
#
# def funcion1(frase,letra):
#     resultado=""
#     if len(frase)!=0:
#         if frase[-1].lower()==letra.lower():
#             resultado=frase
#         else:
#             resultado=funcion1(frase[:-1],letra)
#     return resultado
#
# print(funcion1("tres tristes tigres comen trigo en un trigal","a"))

#
# def funcionC(frase,letra):
#     resultado = ""
#     if len(frase) == 0:
#         return  resultado
#     frase_acortada = frase[:-1]
#     resultado += frase[:-1] + funcionC(frase_acortada)
#     return resultado
#
# frase = "tres tristes tigres comen trigo en un trigal"
# vocales = "a"
# funcionC("tres tristes tigres comen trigo en un trigal","a")

#
#
# def funcionC(frase,letra):
#     resultado = ""
#     if len(frase) == 0:
#         return  resultado
#     elif frase[0] in vocales:
#         resultado = frase[0] + funcionC(frase[1:])
#     else:
#         resultado = funcionC(frase[1:]) + frase[0]
#     return resultado


#dada una frase devolver la frase con vocales a mayúsculas y consonantes en minúsculas
# def funcionC(frase):
#     resultado = ""
#     vocales = "aeiou"
#     if len(frase) != 0:
#         if frase[0] in vocales:
#             resultado = frase[0].upper() + funcionC(frase[1:])
#         else:
#             resultado = frase[0].lower() + funcionC(frase[1:])
#     return resultado
#
# print("")
# print(funcionC(frase = "La casita de papel"))


#Dda una frase contar el numero de vocales
# def funcionVocales(frase):
#     vocales = "aeiou"
#     resultado = 0
#     if len(frase) != 0:
#         if frase[0].lower() in vocales:
#             resultado += 1 + funcionVocales(frase[1:])
#         else:
#             resultado += funcionVocales(frase[1:])
#     return resultado
#
# print(funcionVocales("La casa de monachina"))

#Dado un string devolver una lista con todas las vocales
# def ListaVocales(frase):
#     resultado = []
#     vocales = "aeiou"
#     if len(frase) != 0:
#         if frase[0] in resultado:
#             resultado += ListaVocales(frase[1:])
#         if frase[0] in vocales:
#             resultado.append(frase[0])
#             resultado += ListaVocales(frase[1:])
#         else:
#             resultado += ListaVocales(frase[1:])
#     return resultado
#
# print("")
# print(ListaVocales("La casa de lola"))

#Dado un string devolver una lista con las vocales de la frase sin que se repitan las vocales
# def ListaVocales(frase):
#     vocales = "aeiou"
#     resultado = []
#     if len(frase) != 0:
#         resultado += ListaVocales(frase[1:])
#         if frase[0] in vocales:
#             if frase[0] not in resultado:
#                 resultado.append(frase[0])
#     return resultado
#
# print("")
# print(ListaVocales("Tia paola"))

#dada una frase, devolver un diccionario donde las claves sean cada una de las letras de la frase, y los valores las veces que aparece dicha letra en la frase.
# def diccionarioConVocales(frase):
#     resultado = {}
#     cantidad = 0
#     if len(frase) != 0:
#         resultado = diccionarioConVocales(frase[1:])
#         if frase[0] in resultado:
#             resultado[frase[0].lower()] += 1
#         else:
#             resultado[frase[0].lower()] = 1
#     return resultado
#
# print("")
# print(diccionarioConVocales("Tia paola"))

# def factorial(n):
#     resultado = 1
#     if n == 0:
#         return resultado
#     else:
#         resultado = n * factorial(n-1)
#
#     return resultado

# def factorial(n):
#     resultado = 1
#     if n == 0:
#         return resultado
#     else:
#         resultado = n * factorial(n-1)
#     return resultado
#
# print("")
# print(factorial(4))

# def lineaN(n):
#     resultado = 0
#     if n == 1:
#         print("Linea {}".format(n))
#         return resultado
#     else:
#         print("Linea {}".format(n))
#         resultado = lineaN(n-1)
#
#     return resultado
#
# lineaN(3)

#Creamos una linea n hasta q n sea 1
# def lineaN(n):
#     if n > 0:
#         print("Linea {}".format(n))
#         lineaN(n-1)
#
#
# lineaN(3)

#Lo mismo pero al reves
# def lineaN(n):
#     if n > 0:
#         lineaN(n - 1)
#         print(n)
#
# lineaN(3)

# def fimonachi(n):
#     resultado = 0
#     if n == 0:
#         resultado = 0
#     elif n == 1:
#         resultado = 1
#     else:
#         resultado = fimonachi(n-1) + fimonachi(n-2)
#     return resultado
# for i in range(10):
#     print(fimonachi(i))


#fimonatchi
# def fimonatcchi(n):
#     dict = {}
#     resultado = 0
#
#     if n > 0:
#         dict = fimonatcchi(n-1)
#         if n == 1:
#             resultado = 1:
#

#ordenal lista de numeros comines sin repeticion
# def num_comunes(lista1,lista2):
#     resultado = []
#     if len(lista1) != 0:
#         resultado += num_comunes(lista1[1:],lista2)
#         if lista1[0] in lista2 and lista1[0] not in resultado:
#             resultado.append(lista1[0])
#     return resultado
# lista1 = [1,1,1,2,3,4,5,6,5,4,3,4,5,6,767,67,54,34]
# lista2 = [2,2,2,4,5,43,43,56,75,3,2]
# print(num_comunes(lista1,lista2))
