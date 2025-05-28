#TIpos de excepciones:
# ZeroDivisionError: Ocurre cuando se intenta dividir por cero.
# ValueError: Ocurre cuando una operación recibe un argumento con el tipo correcto pero un valor inapropiado.
# TypeError: Ocurre cuando se intenta realizar una operación con un tipo de dato inapropiado.
# AssertionError

def funcion(a):
    #assert a > 5, "a ha de ser mayor que 5"
    try:
        #val = a/0
        
        if a == 5:
            raise ZeroDivisionError("Has enviado a = 5")
        print("a =", a)

    except ZeroDivisionError as e:
        print("ansfhdbaj")
        print(e)
    except:
        print("Ha pasado algo")
    finally:
        print("Se ejecuta SI O SI")

        
    print("Fin de la funcion")

funcion(5)