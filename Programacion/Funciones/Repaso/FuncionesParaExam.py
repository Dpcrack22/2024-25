##  Unir dos listas sin duplicados ##
def unir_listas_sin_duplicados(lista1, lista2):
    """
    Une dos listas en una sola, eliminando duplicados.
    """
    lista_unida = []
    
    for lista in [lista1, lista2]:
        for elemento in lista:
            if elemento not in lista_unida:
                lista_unida.append(elemento)
    
    return lista_unida

lista1 = [1,2,3,4,5,6,7,8]
lista2 = [2,4,6,8,10,12,14]


##   Unir dos listas sin cosas iguales de forma recursiva   ##
def unir_listas_sin_duplicados_r(lista1, lista2, resultado=None):

    if resultado is None:
        resultado = []

    if not lista1 and not lista2: 
        return resultado

    if lista1: 
        elemento = lista1[0]
        if elemento not in resultado:
            resultado.append(elemento)
        return unir_listas_sin_duplicados_r(lista1[1:], lista2, resultado)

    if lista2:
        elemento = lista2[0]
        if elemento not in resultado:
            resultado.append(elemento)
        return unir_listas_sin_duplicados_r(lista1, lista2[1:], resultado)

    return resultado


print(unir_listas_sin_duplicados_r(lista1, lista2))


##  Crear un menu a partir de una tupla ##
menu00 = ("Opcion1","Opcion2","Opcion3","Opcion4","Opcion5")
def menus(tupla):
    menu = ""
    for i in range(len(tupla)):
        menu += str(i+1)+")"+tupla[i] + "\n"
    while True:
        print(menu)
        opc = input("Dame una opcion: ")
        if not opc.isdigit():
            print("Only numerical Options")
            input("Retry: ")
        else:
            if int(opc) not in range(1,len(tupla)+1):
                print("Opcion out of range:")
                input("Retry: ")
            else:
                return int(opc)


opcion = menus(menu00)
print(opcion)
menus(menu00)
def funcion_menucito(titulo="",*opciones):
    menu = ""
    if titulo != "":
        print(titulo.center(10, "*"))
    for i in range(len(opciones)):
        menu += str(i+1)+")"+opciones[i]+"\n"

    while True:
        print(menu)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("numeros gracias")
        elif int(opc) not in range(1, len(opciones) + 1):
            print("Opcion fuera de rango chato")
        else:
            opc = int(opc)
            return opc
funcion_menucito("Titulo","Opcion1","Opcion2","Opcion2")


##  Try y Except  ##
def funcionA():
    try:
        print("Dame un numero")
        num = int(input("Numero: "))
        assert num > 5, "Solo queremos numeros mayores a 5"
        assert num != 10, "No queremos el 10"
    except AssertionError as e:
        print("Se ha producido una excepcion")
        print(e)
    except ValueError:
        print("Se ha provocado una excepcion")
'''
Si se produce un AssertionError, captura el mensaje exacto con as e.
Si se ingresa algo que no es un número, captura ValueError e imprime un mensaje genérico.
'''

def funcionA():
    try:
        print("Dame un numero")
        num = int(input("Numero: "))
        if num < 10:
            raise ZeroDivisionError("Solo queremos numeros mayores a 10")
    except AssertionError as e:
        print("Se ha producido una excepcion")
        print(e)
    except ValueError:
        print("Se ha provocado una excepcion")
    except ZeroDivisionError as e:
        print("Excepcion indefinida")
        print(e)
'''
¿Qué hace?
Si el número ingresado es menor que 10, fuerza un ZeroDivisionError con raise.
Captura y maneja diferentes excepciones (AssertionError, ValueError, ZeroDivisionError).
¿Para qué sirve raise?
Permite lanzar errores personalizados en ciertas condiciones.
Es útil cuando queremos definir nuestras propias reglas de validación.
'''

menu00 = ("Opcion1", "Opcion2", "Opcion3")

def getOpc(tupla):
    menu = ""
    for i in range(len(tupla)):
        menu += str(i+1) + ")" + tupla[i] + "\n"

    while True:
        try:
            print(menu)
            opc = input("Dame una opcion: ")
            if not opc.isdigit():
                raise ValueError("Solo se admiten numeros")
            elif not int(opc) in range(len(tupla)+1):
                raise ValueError("Numerito fuera de rango")
            else:
                return int(opc)
        except ValueError as e:
            print(e)

print(getOpc(menu00))
'''
¿Qué hace?
Muestra un menú con opciones numeradas.
Pide al usuario que ingrese un número.
Validaciones:
Si la entrada no es un número, lanza un ValueError con "Solo se admiten numeros".
Si el número ingresado está fuera del rango, lanza otro ValueError con "Numerito fuera de rango".
Si todo es correcto, devuelve la opción seleccionada.
Mejoras posibles
Mostrar el mensaje "Elige un número entre 1 y X", en lugar de "Numerito fuera de rango".
Usar try-except fuera del bucle while y solo capturar la excepción ValueError cuando sea realmente necesario.
'''

