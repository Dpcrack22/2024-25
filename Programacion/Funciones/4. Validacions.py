# ZeroDivisionError, ValueError , AssertionError = La probocamos con el assert


## AssertionError ##
# def funcionA():
#     print("Dame un numero")
#     num = int(input("Numero: "))
#     assert num > 5 , "Solo queremos numeros mayores a 5"
#
# funcionA()

## Try y Except
# def funcionA():
#     try:
#         print("Dame un numero")
#         num = int(input("Numero: "))
#         assert num > 5 , "Solo queremos numeros mayores a 5"
#     except:
#         print("Se ha provocado una excepcion")
#
# funcionA()

## Try y except con except asignado(Assert) ##
# Esto hace que solo selecciones la opcion de assert y no las demas eso hace que si pones una letra PETE #
# def funcionA():
#     try:
#         print("Dame un numero")
#         num = int(input("Numero: "))
#         assert num > 5 , "Solo queremos numeros mayores a 5"
#     except AssertionError:
#         print("Se ha provocado una excepcion")
#
# funcionA()

## Try y except con exception value error ##
# def funcionA():
#     try:
#         print("Dame un numero")
#         num = int(input("Numero: "))
#         assert num > 5 , "Solo queremos numeros mayores a 5"
#     except ValueError:
#         print("Se ha provocado una excepcion")
#
# funcionA()

## Try y except con alias ##
# def funcionA():
#     try:
#         print("Dame un numero")
#         num = int(input("Numero: "))
#         assert num > 5 , "Solo queremos numeros mayores a 5"
#         assert num != 10 , "No queremos el 10"
#     except AssertionError as e:
#         print("Se ha produciodo una excepcion")
#         print(e)
#     except ValueError:
#         print("Se ha provocado una excepcion")
#
# funcionA()

## Excepciones con raise ##
# Sirve para provocar una rxcepcion en este caso la de ZeroDividionError #
# def funcionA():
#     try:
#         print("Dame un numero")
#         num = int(input("Numero: "))
#         if num < 10:
#             raise ZeroDivisionError("Solo queremos numeros mayores a 10")
#     except AssertionError as e:
#         print("Se ha produciodo una excepcion")
#         print(e)
#     except ValueError:
#         print("Se ha provocado una excepcion")
#     except ZeroDivisionError as e:
#         print("Excecepcion indefinida")
#         print(e)
# funcionA()

menu00 = ("Opcion1","Opcion2","Opcion3")
def getOpc(tupla):
    menu = ""
    for i in range(len(tupla)):
        menu += str(i+1) + ")" +tupla[i] + "\n"

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